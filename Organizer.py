from web3 import Web3
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
from configparser import ConfigParser
import time
import Config

config = ConfigParser()
config.read('Config.ini')

web3 = Web3(Web3.HTTPProvider(Config.providerURL))
account = web3.eth.account.privateKeyToAccount(Config.organizerConfig['organizerPrivateKey'])
contractInstance = web3.eth.contract(address=web3.toChecksumAddress(config.get('Global', 'contractaddress')), abi=config.get('Global', 'contractABI'))
blindPublicKey = int(contractInstance.functions.blindPublicKey().call())
blindModulus = int(contractInstance.functions.blindModulus().call())

def handle_event(event):
    print('\n***Bob receives the blind message and signs it***')
    print(event)
    signedBlindedMsg = Blind.signature(event['args']['msg'], Blind.Key(Config.organizerConfig['blindPrivateKeyExponent'], blindModulus))
    print('\n***Bob sends the signed, blinded message to the smart contract***')
    print(event['args']['msg'], str(signedBlindedMsg))
    web3.eth.defaultAccount = account.address
    contractInstance.functions.sendSignedBlindMessage(event['args']['msg'], str(signedBlindedMsg)).transact()

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

if __name__ == '__main__':
    print('\n***Bob listens to the smart contract***')
    block_filter = contractInstance.events.newBlindMessage.createFilter(fromBlock='0x0')
    log_loop(block_filter, 1)


