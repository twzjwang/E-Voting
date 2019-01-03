from web3 import Web3
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind
from configparser import ConfigParser
import numpy as np
import time
import Config

Count = np.zeros(16)

config = ConfigParser()
config.read('Config.ini')

web3 = Web3(Web3.HTTPProvider(Config.providerURL))
contractInstance = web3.eth.contract(address=web3.toChecksumAddress(config.get('Global', 'contractaddress')), abi=config.get('Global', 'contractABI'))
blindPublicKey = int(contractInstance.functions.blindPublicKey().call())
blindModulus = int(contractInstance.functions.blindModulus().call())

ballotNumber = contractInstance.functions.ballotNumber().call()
print("There are ", ballotNumber, " ballots on the contract.")
for i in range(0, ballotNumber):
    ballots = contractInstance.functions.ballots(i).call()
    print(ballots)
    hashV = "0x" + Ballot.hashVoteString(ballots[0])
    verification = Blind.verify(ballots[1], Blind.Key(blindPublicKey, blindModulus))
    if str(hashV) == str(verification) and ballots[0][3] == '0':
        print("Valid")
        Count[int(ballots[0][2], 16)] += 1
    else:
        print("Invalid")

print("\nResult:")
print(Count)