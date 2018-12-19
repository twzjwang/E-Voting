from web3 import Web3
from eth_account.messages import defunct_hash_message
import Ballot.ballot as Ballot
import Blind_Signature.RSA.blind as Blind

organizerPrivateKey = '0xfa79e432cb297c4ca8980285ee10e6bd7d0b629911b37ea3f94d1f66252dd2d4'
voterPrivateKeyA = '0x3e5eaaf662b3ed0bdbb95ced83f46da336bc3f9a4fd58f54d31e1b2598c3ebef'
voterPrivateKeyB = '0xade4af964b5729bdc8a02e0a78f5b17c4c10d0668620b82c940f0ad4ac193aa5'

web3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/"))
organizerAccount = web3.eth.account.privateKeyToAccount(organizerPrivateKey)
voterAccountA = web3.eth.account.privateKeyToAccount(voterPrivateKeyA)
voterAccountB = web3.eth.account.privateKeyToAccount(voterPrivateKeyB)


if __name__ == '__main__':
    pubkey, privkey = Blind.keygen(2 ** 128)
    print(pubkey.exponent, privkey.exponent, privkey.modulus)

    print('***Alice prepares ballot***')
    voteString = Ballot.generateVoteString(1)
    print('Vote String', voteString)

    hashV = Ballot.hashVoteString(voteString)
    print('Hashed Vote String ', '0x'+hashV)

    print('\n***Alice blinds the message***')
    r = Blind.blind(int(hashV, 16), pubkey)

    print('\n***Bob receives the blind message and signs it***')
    bf=open('blindmsg')
    m=bf.read()
    Blind.signature(m, privkey)

    print('\n***Alice recieves the signed message and unblinds it***')
    h = open('signedfile')
    signedmsg = h.read()
    Blind.unblind(signedmsg, r, pubkey)

    print('\n***Verifier verefis the message***')
    i = open('unblindsigned')
    ubsignedmsg = i.read()
    Blind.verefy(ubsignedmsg, r, pubkey)