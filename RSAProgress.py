"""
# filename:RSAProgress.py
# author:heizhou
# No.:150420226
# date:17/10/12
# purpose:This file is to show how RSA works
"""
from generateRSAkey import generateKey as GK
from fastExponentialAlgorithm import fastCaculate as FC
class RSA:
    def __init__(self):
        self.key = GK()
        self.public_key = self.key['publicKey']
        self.private_key = self.key['privateKey']
        self.text = ""
        self.ciphertext = []
        self.plaintext = ""

    def encode(self):
        for i in self.text:
            self.ciphertext.append(FC(ord(i), self.public_key[1], self.public_key[0]))

    def decode(self):
        for i in range(len(self.ciphertext)):
            self.plaintext = self.plaintext+chr(FC(self.ciphertext[i], self.private_key[1], self.private_key[0]))

    def entry(self):
        print("please input test text:")
        self.text = raw_input()
        print("ciphertext is:")
        self.encode()
        ctext = ""
        for i in range(len(self.ciphertext)):
            ctext = ctext + str(self.ciphertext[i])
        print(ctext)
        print("after decrypt:")
        self.decode()
        print(self.plaintext)




if __name__ == '__main__':
    RSA().entry()