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

# Tests direct creation of each asset type and invalid asset types
def create_asset():
    # Create the five different types of assets
    asset1 = Asset('CryptoToken')
    asset2 = Asset('Data Spike')
    asset3 = Asset('Removable Drive')
    asset4 = Asset('Security Chip')
    asset5 = Asset('Hardware Patch')
    # Set two of the assets as encrypted
    asset2.is_encrypted = True
    asset5.is_encrypted = True
    # Display the string for each asset showing its name, description and encryption status
    print(asset1)
    print(asset2)
    print(asset3)
    print(asset4)
    print(asset5)
    # Pass an incorrect asset name (not found on the type list) to the asset class
    asset6 = Asset('USB')
    asset7 = Asset(1)
    # Display the string for the incorrect assets, showing as 'Invalid: Please remove'
    print(asset6)
    print(asset7)

# Tests direct creation of a rig, and setting correct and incorrect attributes
def create_rig():
    # Creation of rig and display of string method
    rig = Rig('Mah Computer')
    print(rig)
    # Setting attributes to allowable values
    rig.name = 'My Computer'
    rig.damage_counter = 1.5
    rig.is_broken = True
    rig.upgrade_level = 2
    print(rig)
    # Any values passed to rig name will be converted to a string
    rig.name = 123456
    # The following values are out of range or incorrect types and will not be updated
    rig.damage_counter = 5
    rig.damage_counter = -1
    rig.damage_counter = 'abc'
    rig.is_broken = 'yes'
    rig.upgrade_level = 5
    rig.upgrade_level = -1
    rig.upgrade_level = 'abc'
    print(rig)

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
    # Remove asset found in storage
    rig.remove_asset('Data Spike')
    # Attempt to remove asset not found in storage
    rig.remove_asset('CryptoToken')
    # Attempt to remove item that is not a valid asset
    rig.remove_asset('USB')
    print(rig)

# Tests random asset generate function for rig along with add_asset function
def generate_asset():
    rig = Rig('Mah Computer')
    # Only one asset will be generated, then maximum storage (4 items) will be reached
    rig.generate_asset()
    rig.generate_asset()
    print(rig)
    # Only two more assets will be generated, then maximum storage (6 items) will be reached
    rig.upgrade_level = 1
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    print(rig)
    # Only two more assets will be generated, then maximum storage (8 items) will be reached
    rig.upgrade_level = 2
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    print(rig)
    # Only two more assets will be generated, then maximum storage (10 items) will be reached
    rig.upgrade_level = 3
    rig.generate_asset()
    rig.generate_asset()
    rig.generate_asset()
    print(rig)

# Tests rig taking a hit, reaching broken state, and different damage levels base on upgrade level
def take_hit():
    rig = Rig('Mah Computer')
    rig.take_hit()
    print(rig)
    rig.take_hit()
    print(rig)
    rig2 = Rig('Mah Better Computer')
    rig2.upgrade_level = 1
    rig2.take_hit()
    rig2.upgrade_level = 2
    rig2.take_hit()
    rig2.upgrade_level = 3
    rig2.take_hit()
    print(rig2)

# Tests different condition displays for rig
def show_condition():
    rig = Rig('Mah Computer')
    print(rig.show_condition())
    rig.damage_counter = 0.75
    print(rig.show_condition())
    rig.damage_counter = 1.0
    print(rig.show_condition())
    rig.damage_counter = 1.75
    print(rig.show_condition())
    rig.damage_counter = 2
    print(rig.show_condition())

# Tests creation of a hacker and display of string method
def create_hacker():
    hacker = Hacker('Neo')
    print(hacker)

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

# Runs testing functions for program
def main():
    #create_asset()
    #create_rig()
    #add_item_to_storage()
    #remove_item_from_storage()
    #generate_asset()
    #take_hit()
    #show_condition()

    create_hacker()
    add_item_to_inventory()
    remove_item_from_inventory()

    #acquire_rig()
    #repair_rig()
    #upgrade_rig()

    #encrypt_asset()
    #decrypt_asset()
    #store_asset()
    #retrieve_asset()

    #launch_attack()
    #extract_assets()


main()
