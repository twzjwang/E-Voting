from web3 import Web3
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
from configparser import ConfigParser
import time
import Config

config = ConfigParser()
config.read('Config.ini')

web3 = Web3(Web3.HTTPProvider(Config.providerURL))
contractInstance = web3.eth.contract(address=web3.toChecksumAddress(config.get('Global', 'contractaddress')), abi=config.get('Global', 'contractABI'))
account = web3.eth.account.privateKeyToAccount(Config.voterConfig['voterPrivateKey2'])

web3.eth.defaultAccount = account.address
print('\n***Maliciously votes invalid ballots***')
for i in range(0, 10):
    print(i, '0x4096', '0x4cf98256dcf11c88ac36094cc5e2b935adc86e931f766527301a0d44')
    contractInstance.functions.sendBallot('0x4096', '0x4cf98256dcf11c88ac36094cc5e2b935adc86e931f766527301a0d44').transact()