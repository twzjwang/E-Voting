import numpy as np
import base64
from Crypto.Hash import keccak

def generateVoteString(choice):
    if choice >= 16:
        ValueError('choice must be 0 - 15')
    nonce = hex(np.random.randint(256))[2:4]
    if len(nonce) == 1:
        nonce = '0' + nonce
    voteString = hex(choice) + '0' + nonce
    return voteString

def hashVoteString(voteString):
    keccak224 = keccak.new(digest_bits=224)
    keccak224.update(voteString.encode('utf-8'))
    hashVoteString = keccak224.hexdigest()
    return hashVoteString