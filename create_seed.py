#!/usr/bin/python3


# /* ###############################################################################
# © 2019 nodepacific tech All rights reserved
#
# Libra Generate nodes tool
# The tool to generate libra validator nodes for private Libra blockchain
#
#
# Created by https://www.nodepacific.com
#
###############################################################################  */


from mnemonic import Mnemonic
from sha3 import sha3_256


MNEMONIC = Mnemonic("english")
words = MNEMONIC.generate(128)
shazer = sha3_256()
shazer.update(MNEMONIC.to_entropy(words))
print(shazer.digest().hex())


