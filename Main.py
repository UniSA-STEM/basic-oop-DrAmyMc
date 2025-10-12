"""
File: main.py
Description: Test code for running 'Into the Grid' game, using classes for Hackers, Rigs and Assets.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports each class from their files
from Hacker import Hacker
from Rig import Rig
from Asset import Asset

# Tests direct creation of each asset type and display of string method
def create_asset():
    asset1 = Asset('CryptoToken')
    asset2 = Asset('Data Spike')
    asset3 = Asset('Removable Drive')
    asset4 = Asset('Security Chip')
    asset5 = Asset('Hardware Patch')
    print(asset1)
    print(asset2)
    print(asset3)
    print(asset4)
    print(asset5)

# Tests direction creation of a rig and display of string method
def create_rig():
    rig = Rig('Mah Computer')
    print(rig)

# Tests creation of a hacker and display of string method
def create_hacker():
    hacker = Hacker('Neo')
    print(hacker)

# Tests acquisition of rig by hacker in exchange for one CryptoToken
def acquire_rig():
    hacker = Hacker('Neo')
    hacker.acquire_rig('Mah Rig')
    print(hacker)
    print(hacker.get_rig())

# Tests random asset generate function for rig (3 initial assets upon create, 10 new random assets)
def generate_asset():
    rig = Rig('Mah Computer')
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    print(rig)

# Runs testing functions for program
def main():
    create_asset()
    create_rig()
    create_hacker()
    acquire_rig()
    #generate_asset()

    #print(rig.get_storage())
    # hacker.scan_inventory('CryptoToken')
    #hacker.launch_spike()
    #hacker.scan_storage('Data Spike')

main()
