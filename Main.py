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
    # Display the string for the incorrect assets, showing as None
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
    hacker.remove_asset('USB')
    hacker.remove_asset('CryptoToken')
    print(hacker)

# Tests rig acquisition function for Hacker (exceptions and successful)
def acquire_rig():
    # Tests acquisition without CryptoToken available
    hacker = Hacker('Neo')
    hacker.remove_asset('CryptoToken')
    hacker.acquire_rig('Mah Rig')
    # Tests successful acquisition of rig
    hacker.add_asset(Asset('CryptoToken'))
    hacker.acquire_rig('Mah Rig Take 2')
    print(hacker)
    print(hacker.rig)
    # Tests acquisition when a rig is already present
    hacker.acquire_rig('New Rig')

# Tests repair rig function for Hacker (exceptions and successful)
def repair_rig():
    # Tests repair without a rig
    hacker = Hacker('Neo')
    hacker.repair_rig()
    # Tests repair when rig is not damaged
    hacker.acquire_rig('Mah Rig')
    hacker.repair_rig()
    # Tests repair without CryptoToken available
    hacker.rig.damage_counter = 1
    hacker.repair_rig()
    # Tests successful repair of rig
    hacker.add_asset(Asset('CryptoToken'))
    hacker.repair_rig()
    print(hacker.rig)

# Tests upgrade rig function for Hacker (exceptions and successful)
def upgrade_rig():
    # Tests upgrade without a rig
    hacker = Hacker('Neo')
    hacker.upgrade_rig()
    # Tests upgrade without Hardware Patch
    hacker.acquire_rig('Mah Computer')
    hacker.upgrade_rig()
    # Tests upgrade when rig is already at maximum upgrade level
    hacker.add_asset(Asset('Hardware Patch'))
    hacker.rig.upgrade_level = 3
    hacker.upgrade_rig()
    # Tests successful upgrade of rig
    hacker.rig.upgrade_level = 0
    hacker.upgrade_rig()
    print(hacker.rig)

# Tests encrypt asset function for Hacker (exceptions and successful)
def encrypt_asset():
    # Tests encryption without Security Chip in inventory
    hacker = Hacker('Neo')
    hacker.encrypt_asset('CryptoToken')
    # Tests encryption without Security Chip in storage or inventory
    hacker.acquire_rig('My Computer')
    hacker.encrypt_asset('CryptoToken')
    # Tests encryption of asset type not present in inventory or storage
    hacker.add_asset(Asset('Security Chip'))
    hacker.encrypt_asset('CryptoToken')
    # Tests successful encryption of asset in inventory with Security Chip in inventory
    hacker.add_asset(Asset('CryptoToken'))
    hacker.encrypt_asset('CryptoToken')
    print(hacker)
    # Tests successful encryption of asset in inventory with Security Chip in storage
    hacker.add_asset(Asset('CryptoToken'))
    hacker.rig.add_asset(Asset('Security Chip'))
    hacker.encrypt_asset('CryptoToken')
    print(hacker)
    # Tests successful encryption of asset in storage with Security Chip in inventory
    hacker.add_asset(Asset('Security Chip'))
    hacker.encrypt_asset('Data Spike')
    print(hacker.rig)
    # Tests successful encryption of asset in storage with Security Chip in storage
    hacker.rig.add_asset(Asset('Security Chip'))
    hacker.encrypt_asset('Data Spike')
    print(hacker.rig)
    # Tests encryption of asset when already encrypted
    hacker.add_asset(Asset('Security Chip'))
    hacker.encrypt_asset('CryptoToken')
    hacker.encrypt_asset('Data Spike')

# Tests decrypt asset function for Hacker (exceptions and successful)
def decrypt_asset():
    # Tests decryption without Security Chip in inventory
    hacker = Hacker('Neo')
    hacker.decrypt_asset('CryptoToken')
    # Tests decryption without Security Chip in storage or inventory
    hacker.acquire_rig('My Computer')
    hacker.rig.upgrade_level = 3
    hacker.decrypt_asset('CryptoToken')
    # Tests decryption of asset type not present in inventory or storage
    hacker.add_asset(Asset('Security Chip'))
    hacker.decrypt_asset('CryptoToken')
    # Tests successful decryption of asset in inventory with Security Chip in inventory
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)
    hacker.decrypt_asset('CryptoToken')
    print(hacker)
    # Tests successful decryption of asset in inventory with Security Chip in storage
    hacker.rig.add_asset(Asset('Security Chip'))
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)
    hacker.decrypt_asset('CryptoToken')
    print(hacker)
    # Tests successful decryption of asset in storage with Security Chip in inventory
    hacker.add_asset(Asset('Security Chip'))
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.rig.add_asset(asset)
    print(hacker.rig)
    hacker.decrypt_asset('CryptoToken')
    print(hacker.rig)
    # Tests successful decryption of asset in storage with Security Chip in storage
    hacker.rig.add_asset(Asset('Security Chip'))
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.rig.add_asset(asset)
    print(hacker.rig)
    hacker.decrypt_asset('CryptoToken')
    print(hacker.rig)
    # Tests decryption of asset when already decrypted
    hacker.add_asset(Asset('Security Chip'))
    hacker.decrypt_asset('CryptoToken')
    hacker.decrypt_asset('Data Spike')

def store_asset():
    hacker = Hacker('Neo')
    hacker.acquire_rig('My Computer')
    hacker.add_asset(Asset('CryptoToken'))
    hacker.add_asset(Asset('CryptoToken'))
    hacker.add_asset(Asset('CryptoToken'))
    asset = Asset('Data Spike')
    asset.is_encrypted = True
    asset2 = Asset('Data Spike')
    asset2.is_encrypted = True
    hacker.add_asset(asset)
    hacker.add_asset(asset2)
    print(hacker)
    print(hacker.rig)
    hacker.store_asset('all')
    print(hacker)
    print(hacker.rig)
    hacker.rig.upgrade_level = 3
    hacker.store_asset('all')
    print(hacker)
    print(hacker.rig)

def retrieve_asset():
    hacker = Hacker('Neo')
    hacker.acquire_rig('My Computer')
    hacker.rig.upgrade_level = 3
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    asset2 = Asset('CryptoToken')
    asset2.is_encrypted = True
    hacker.rig.add_asset(asset)
    hacker.rig.add_asset(asset2)
    print(hacker)
    print(hacker.rig)
    hacker.retrieve_asset('all')
    print(hacker)
    print(hacker.rig)

def launch_attack():
    hacker1 = Hacker('Neo')
    hacker2 = Hacker('Bad Guy')
    hacker1.acquire_rig('Neo Rig')
    hacker2.acquire_rig('BadGuy Rig')
    hacker1.launch_attack(hacker2.rig)
    hacker1.launch_attack(hacker2.rig)
    # Test an attack without a data spike
    hacker1.launch_attack(hacker2.rig)
    # Extract assets from broken rig
    hacker1.extract_assets(hacker2.rig)
    print(hacker1)
    print(hacker1.rig)
    print(hacker2)
    print(hacker2.rig)

def extract_assets():
    pass

# Tests reduce trace function
def reduce_trace():
    # Tests successful reduction of trace level
    hacker = Hacker('Neo')
    hacker.trace_level = 3
    hacker.reduce_trace()
    hacker.reduce_trace()
    hacker.reduce_trace()
    # Tests attempt to reduce trace level below 0
    hacker.reduce_trace()

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
    #add_item_to_inventory()
    #remove_item_from_inventory()

    acquire_rig()
    #repair_rig()
    #upgrade_rig()

    #encrypt_asset()
    #decrypt_asset()
    #store_asset()
    #retrieve_asset()

    #launch_attack()
    #extract_assets()
    #reduce_trace()

main()
