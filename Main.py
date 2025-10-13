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

# Tests creation of an incorrect asset type
def create_incorrect_asset():
    asset6 = Asset('USB')
    print(asset6)

# Tests direction creation of a rig and display of string method
def create_rig():
    rig = Rig('Mah Computer')
    print(rig)

# Tests creation of a hacker and display of string method
def create_hacker():
    hacker = Hacker('Neo')
    print(hacker)

# Tests acquisition of rig by hacker in exchange for one CryptoToken, and if rig is already present and if missing Cryptoken
def acquire_rig():
    hacker = Hacker('Neo')
    hacker.remove_asset('CryptoToken')
    hacker.acquire_rig('Mah Rig')
    asset = Asset('CryptoToken')
    hacker.add_asset(asset)
    hacker.acquire_rig('Mah Rig Take 2')
    print(hacker)
    print(hacker.get_rig())
    hacker.acquire_rig('New Rig')

# Tests scanning storage on rig to locate item that is found and item that is not found
def scan_storage():
    rig = Rig('Mah Computer')
    print(rig)
    rig.scan_storage('Data Spike')
    rig.scan_storage('CryptoToken')

# Tests adding a valid asset, invalid asset, and non-asset to storage on rig
def add_item_to_storage():
    rig = Rig('Mah Computer')
    valid_asset = Asset('CryptoToken')
    invalid_asset = Asset('USB')
    non_asset = 'harddrive'
    rig.add_asset(valid_asset)
    rig.add_asset(invalid_asset)
    rig.add_asset(non_asset)
    print(rig)

# Tests removing an asset from storage, and attempting to remove an asset that is not in storage
def remove_item_from_storage():
    rig = Rig('Mah Computer')
    print(rig)
    rig.remove_asset('Data Spike')
    print(rig)
    rig.remove_asset('CryptoToken')

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

# Tests repair rig function for rig, including when rig doesn't need repair and when CryptoToken is missing
def repair_rig():
    rig = Rig('Mah Computer')
    rig.repair_rig()
    rig.set_damage_counter(5)
    rig.set_is_broken(True)
    print(rig)
    rig.repair_rig()
    asset = Asset('CryptoToken')
    rig.add_asset(asset)
    print(rig)
    rig.repair_rig()
    print(rig)

# Tests upgrade rig function for rig, including when rig is at maximum upgrade level and when Hardware Patch is missing
def upgrade_rig():
    rig = Rig('Mah Computer')
    rig.upgrade_rig()
    asset = Asset('Hardware Patch')
    rig.add_asset(asset)
    rig.set_upgrade_level(3)
    print(rig)
    rig.upgrade_rig()
    rig.set_upgrade_level(0)
    rig.upgrade_rig()
    print(rig)

# Tests rig taking a hit and broken state changing to broken when enough damage sustained
def take_hit():
    rig = Rig('Mah Computer')
    rig.take_hit()
    print(rig)
    rig.take_hit()
    print(rig)

# Tests scanning hacker's inventory and storage to locate item that is found and item that is not found#
def scan_inventory():
    hacker = Hacker('Neo')
    print(hacker)
    hacker.scan_inventory('Data Spike')
    hacker.scan_inventory('CryptoToken')
    #hacker.acquire_rig('Mah Computer')
    hacker.scan_storage('Data Spike')
    hacker.scan_storage('CryptoToken')

# Tests adding a valid asset, invalid asset, and non-asset to hacker's inventory
def add_item_to_inventory():
    hacker = Hacker('Neo')
    valid_asset = Asset('CryptoToken')
    invalid_asset = Asset('USB')
    non_asset = 'harddrive'
    hacker.add_asset(valid_asset)
    hacker.add_asset(invalid_asset)
    hacker.add_asset(non_asset)
    print(hacker)

# Tests removing an asset from inventory, and attempting to remove an asset that is not in inventory
def remove_item_from_inventory():
    hacker = Hacker('Neo')
    hacker.remove_asset('Data Spike')
    hacker.remove_asset('CryptoToken')
    print(hacker)

# TODO: Need to write tests for rig for upgrade levels with different amounts of damage and storage

# Runs testing functions for program
def main():
    #create_asset()
    #create_incorrect_asset()
    #create_rig()
    #create_hacker()
    #acquire_rig()
    #scan_storage()
    #add_item_to_storage()
    #remove_item_from_storage()
    #generate_asset()
    #repair_rig()
    #upgrade_rig()
    #take_hit()
    #scan_inventory()
    #add_item_to_inventory()
    #remove_item_from_inventory()

main()
