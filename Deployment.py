from web3 import Web3
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
from solc import compile_files, link_code, compile_source
from configparser import ConfigParser
import Config
import json

config = ConfigParser()
config.read('Config.ini')

web3 = Web3(Web3.HTTPProvider(Config.providerURL))

web3.eth.defaultAccount = web3.eth.accounts[0]
Voting = web3.eth.contract(abi=config.get('Global', 'contractABI'), bytecode=config.get('Global', 'contractBytecode'))
txHash = Voting.constructor().transact()
txReceipt = web3.eth.waitForTransactionReceipt(txHash)
config.set('Global', 'contractAddress', txReceipt.contractAddress)

with open('Config.ini', 'w') as f:
    config.write(f)