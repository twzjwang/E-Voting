from web3 import Web3
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
from configparser import ConfigParser
import time
import Config

if __name__ == '__main__':

    config = ConfigParser()
    config.read('Config.ini')

    web3 = Web3(Web3.HTTPProvider(Config.providerURL))
    account1 = web3.eth.account.privateKeyToAccount(Config.voterConfig['voterPrivateKey1'])
    account2 = web3.eth.account.privateKeyToAccount(Config.voterConfig['voterPrivateKey2'])
    contractInstance = web3.eth.contract(address=web3.toChecksumAddress(config.get('Global', 'contractaddress')), abi=config.get('Global', 'contractABI'))
    blindPublicKey = int(contractInstance.functions.blindPublicKey().call())
    blindModulus = int(contractInstance.functions.blindModulus().call())

    print('***Alice prepares ballot***')
    voteString = Ballot.generateVoteString(Config.voterConfig['voterChoice'])
    print('Vote String', voteString)
    hashV = Ballot.hashVoteString(voteString)
    print('Hashed Vote String', hashV)

    print('\n***Alice blinds the message***')
    r, blindedMessage = Blind.blind(hashV, Blind.Key(blindPublicKey, blindModulus))
    print(blindedMessage)

    print('\n***Alice sends the blinded message to the smart contract***')
    web3.eth.defaultAccount = account1.address
    contractInstance.functions.sendBlindMessage(str(blindedMessage)).transact()

    print('\n***Alice listens to the smart contract to get signed blinded message***')
    event_filter = contractInstance.events.newSignedBlindMessage.createFilter(fromBlock='latest')
    isReceive = 0
    signedBlindedMsg = ''
    while not isReceive:
        for event in event_filter.get_new_entries():
            print(event)
            if event['args']['unsignedMsg'] == blindedMessage:
                signedBlindedMsg = event['args']['signedMsg']
                isReceive = 1
                break
        time.sleep(1)
    
    print('\n***Alice recieves the signed message and unblinds it***')
    signedMsg = Blind.unblind(signedBlindedMsg, r, Blind.Key(blindPublicKey, blindModulus))

    print('\n***Alice send the ballot and the signed message to the smart contrac***')
    web3.eth.defaultAccount = account2.address
    print(str(voteString), str(signedMsg))
    contractInstance.functions.sendBallot(str(voteString), str(signedMsg)).transact()

    print('\n***Alice has voted her ballot***')
