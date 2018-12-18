from web3 import Web3
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
import Config

if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(Config.providerURL))
    contractInstance = web3.eth.contract(address=web3.toChecksumAddress(Config.contractAddress), abi=Config.contractABI, ContractFactoryClass=ConciseContract)

    print('***Alice prepares ballot***')

    voteString = Ballot.generateVoteString(Config.voterConfig['voterChoice'])
    print('Vote String', voteString)

    hashV = Ballot.hashVoteString(voteString)
    print('Hashed Vote String', hashV)

    print('\n***Alice blinds the message***')
    r = Blind.blind(int(hashV, 16), Blind.Key(Config.Config['blindPublicKeyExponent'], Config.Config['blindModulus']))
