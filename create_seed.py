#!/usr/bin/python3

from mnemonic import Mnemonic
from sha3 import sha3_256

from pylibra.wallet.account import Account


MNEMONIC = Mnemonic("english")
words = MNEMONIC.generate(128)
shazer = sha3_256()
shazer.update(MNEMONIC.to_entropy(words))
print(shazer.digest().hex())


