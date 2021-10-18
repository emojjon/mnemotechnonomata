#!/usr/bin/env python3

import mnemotechnonomata

print("Testing with default parameters")
for i in range(10):
    print(mnemotechnonomata_tmp.memoname())  

print("\n\nTesting with allow_hyphens set to False")
for i in range(10):
    print(mnemotechnonomata_tmp.memoname(False))  

print("\n\nTesting with category set to 'scientists'")
for i in range(10):
    print(mnemotechnonomata_tmp.memoname(category = 'scientists'))

print("\n\nTesting with category set to 'animals'")
for i in range(10):
    print(mnemotechnonomata_tmp.memoname(category = 'animals'))

print("\n\nTesting with category set to 'fungi'")
try:
    print(mnemotechnonomata_tmp.memoname(category = 'fungi'))
except Exception as e:
    print(f'Caught exception:\n    "{e}"')
