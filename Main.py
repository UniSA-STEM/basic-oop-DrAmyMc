"""
File: main.py
Description: Test code for running 'Into the Grid' game, using classes for Hackers, Rigs and Assets.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

def create_set_display_assets():
    """
    Direct tests for the Asset class for asset creation, setting attributes, and string display.

    Tests:
     - Creation of valid asset types.
     - Handling of invalid asset types.
     - Changing the name (type) of asset manually.
     - Setting encryption status manually.
     - Displaying string representations.

     Expected behaviour:
     - Valid asset types should be created successfully.
     - Invalid asset types should not be created (prints warning, returns None).
     - Valid name change should set new name and description successfully.
     - Invalid name change should be unsuccessful.
     - Encrypted assets should display 'Encrypted' status in their string output.
    """
    print("\n=== TEST: Create, Modify and Display Assets ===\n")

    # --- Create valid assets ---
    asset1 = Asset('CryptoToken')
    asset2 = Asset('Data Spike')
    asset3 = Asset('Removable Drive')
    asset4 = Asset('Security Chip')
    asset5 = Asset('Hardware Patch')

    # --- Attempt to create invalid assets ---
    asset6 = Asset('USB')   # Invalid name (not in type_list)
    asset7 = Asset(1)       # Invalid type (not a string)

    # --- Modify asset name ---
    asset4.name = 'CryptoToken' # Valid name
    asset4.name = 'USB'         # Invalid name (not in type_list)

    # --- Modify encryption status ---
    asset2.is_encrypted = True
    asset5.is_encrypted = True

    # --- Display asset details ---
    print(asset1)
    print(asset2)
    print(asset3)
    print(asset4)
    print(asset5)

def create_set_display_rig():
    """
        Direct tests for the Rig class for rig creation, setting attributes and string display.

        Tests:
         - Creation of a rig instance.
         - Changing name, damager_counter, is_broken, and upgrade_level manually.
         - Displaying string representations.

         Expected behaviour:
         - Rig should be created successfully.
         - Valid changes should be applied and displayed in string representation.
         - Invalid changes should not be applied and string representation should be displayed unchanged.
        """
    print("\n=== TEST: Create, Modify and Display Rig ===\n")

    # --- Create and display rig ---
    rig = Rig('Mah Computer')
    print("--- Newly created rig ---")
    print(rig)

    # --- Modify attributes to valid values and display new values ---
    rig.name = 123456           # Value will be converted to a string
    rig.damage_counter = 1.5    # Valid float in range 0-2
    rig.is_broken = True        # Valid boolean value
    rig.upgrade_level = 2       # Valid integer in range 0-3
    print("--- Rig with modified attributes ---")
    print(rig)

    # --- Attempt to modify attributes to invalid values ---
    rig.damage_counter = 5      # Out of range 0-2
    rig.damage_counter = -1     # Out of range 0-2
    rig.damage_counter = 'abc'  # Not an integer
    rig.is_broken = 'yes'       # Not boolean value
    rig.upgrade_level = 5       # Out of range 0-3
    rig.upgrade_level = -1      # Out of range 0-3
    rig.upgrade_level = 'abc'   # Not an integer
    print("--- Rig with no invalid changes - same as previous display ---")
    print(rig)

def scan_add_remove_storage():
    """
        Direct tests for the Rig class for adding and removing assets from storage.

        Tests:
         - Adding assets (valid and invalid) to a rig's storage.
         - Removing assets (valid and invalid) from a rig's storage.

         Expected behaviour:
         - Valid assets should be successfully added and removed from storage.
         - Invalid assets should not be added or removed from storage.

         Notes:
             - scan_storage function indirectly tested via its utilisation in remove_asset function.
             - Limits to storage size based on upgrade level will be tested as part of generate_asset function.
        """
    print("\n=== TEST: Search, Add and Remove Assets from Rig's Storage ===\n")

    # --- Create rig ---
    rig = Rig('Mah Computer')
    print("--- This new rig should have default storage of 2x Data Spikes and 1x Removable Drive ---")
    print(rig)

    # --- Create valid and invalid assets ---
    valid_asset = Asset('CryptoToken')
    invalid_asset = Asset('USB')        # Not a valid asset name (type)
    non_asset = 'harddrive'             # Not an Asset object

    # --- Add assets to rig's storage and display ---
    rig.add_asset(valid_asset)
    rig.add_asset(invalid_asset)
    rig.add_asset(non_asset)
    print("\n--- This rig should have one CryptoToken added to default storage ---")
    print(rig)

    # --- Remove assets from rig's storage and display ---
    rig.remove_asset('Data Spike')      # Valid asset to be removed
    rig.remove_asset('Security Chip')   # Attempt to remove asset not found in storage
    rig.remove_asset('USB')             # Attempt to remove invalid asset not found in storage
    print("--- This rig should now have only one Data Spike left in storage ---")
    print(rig)


# Tests random asset generate function for rig along with add_asset function
def generate_asset():
    """
        Direct tests for the Rig class for random asset generation and storage size limits.

        Tests:
         - Generating random assets and adding them to the rig's storage.
         - Maximum storage limit for asset varying based on upgrade level of rig.

         Expected behaviour:
         - Randomly generated assets should be successfully added to the rig's storage if the maximum storage
            limit is not exceeded.
         - Maximum storage limit will change from 4 to 6 to 8 to 10 items in line with upgrade levels of 0, 1, 2 and 3.
        """
    print("\n=== TEST: Generate Random Asset and Check Maximum Storage Limits ===\n")

    # --- Create rig ---
    rig = Rig('Mah Computer')

    # --- Test asset generation for Level 0 rig - max items 4 ---
    rig.generate_asset()    # 4th item in storage
    rig.generate_asset()    # Limit exceeded - will not add
    print("\n--- This level 0 rig should have 4 items in storage ---")
    print(rig)

    # --- Test asset generation for Level 1 rig - max items 6 ---
    rig.upgrade_level = 1
    rig.generate_asset()    # 5th item in storage
    rig.generate_asset()    # 6th item in storage
    rig.generate_asset()    # Limit exceeded - will not add
    print("\n--- This level 1 rig should have 6 items in storage ---")
    print(rig)

    # --- Test asset generation for Level 2 rig - max items 8 ---
    rig.upgrade_level = 2
    rig.generate_asset()    # 7th item in storage
    rig.generate_asset()    # 8th item in storage
    rig.generate_asset()    # Limit exceeded - will not add
    print("\n--- This level 2 rig should have 8 items in storage ---")
    print(rig)

    # --- Test asset generation for Level 3 rig - max items 10 ---
    rig.upgrade_level = 3
    rig.generate_asset()    # 9th item in storage
    rig.generate_asset()    # 10th item in storage
    rig.generate_asset()    # Limit exceeded - will not add
    print("\n--- This level 3 rig should have 10 items in storage ---")
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
    #create_set_display_assets()
    #create_set_display_rig()
    #scan_add_remove_storage()
    generate_asset()

    #take_hit()
    #show_condition()

    #create_hacker()
    #add_item_to_inventory()
    #remove_item_from_inventory()

    #acquire_rig()
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
