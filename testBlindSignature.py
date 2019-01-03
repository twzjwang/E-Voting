from web3 import Web3
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind

if __name__ == '__main__':
    pubkey, privkey = Blind.keygen(2 ** 128)
    print(pubkey.exponent, privkey.exponent, privkey.modulus)

    print('\n***Alice prepares ballot***')
    voteString = Ballot.generateVoteString(1)
    print('Vote String', voteString)

    hashV = Ballot.hashVoteString(voteString)
    print('Hashed Vote String ', '0x' + hashV)

    print('\n***Alice blinds the message***')
    r, blindedMsg = Blind.blind(hashV, pubkey)
    print(r, blindedMsg)

    print('\n***Bob receives the blind message and signs it***')
    signedBlindedMsg = Blind.signature(blindedMsg, privkey)
    print(signedBlindedMsg)

    print('\n***Alice recieves the signed message and unblinds it***')
    signedMsg = Blind.unblind(signedBlindedMsg, r, pubkey)
    print(signedMsg)

    print('\n***Verifier verefies the message***')
    print(Blind.verify(signedMsg, pubkey))