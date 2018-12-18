from web3 import Web3
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
import Config

if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider(Config.providerURL))
    contractInstance = web3.eth.contract(address=web3.toChecksumAddress(Config.contractAddress), abi=Config.contractABI)
