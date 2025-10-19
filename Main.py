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
         - Removing assets (valid, invalid, and encrypted) from a rig's storage.

         Expected behaviour:
         - Valid assets should be successfully added and removed from storage.
         - Invalid assets should not be added or removed from storage.
         - Encrypted assets should not be removed from storage.

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
    valid_asset.is_encrypted = True
    invalid_asset = Asset('USB')        # Not a valid asset name (type)
    non_asset = 'harddrive'             # Not an Asset object

    # --- Add assets to rig's storage and display ---
    rig.add_asset(valid_asset)
    rig.add_asset(invalid_asset)
    rig.add_asset(non_asset)
    print("\n--- This rig should have one encrypted CryptoToken added to default storage ---")
    print(rig)

    # --- Remove assets from rig's storage and display ---
    rig.remove_asset('Data Spike')      # Valid asset to be removed
    rig.remove_asset('Security Chip')   # Attempt to remove asset not found in storage
    rig.remove_asset('CryptoToken')     # Attempt to remove encrypted asset from storage
    print("--- This rig should now have only one Data Spike in storage instead of two ---")
    print(rig)

def generate_asset():
    """
        Direct tests for the Rig class for random asset generation and storage size limits.

        Tests:
         - Generating random assets and adding them to the rig's storage.
         - Maximum storage limit for asset varying based on upgrade level of rig.
         - Attempting to generate an asset while rig is broken.

         Expected behaviour:
         - Randomly generated assets should be successfully added to the rig's storage if the maximum storage
            limit is not exceeded.
         - Maximum storage limit will change from 4 to 6 to 8 to 10 items in line with upgrade levels of 0, 1, 2 and 3.
         - Error message will display if rig is broken and no asset will be generated.
        """
    print("\n=== TEST: Generate Random Asset and Check Maximum Storage Limits ===\n")

    # --- Create rig ---
    rig = Rig('Mah Computer')

    # --- Test asset generation while rig is broken ---
    rig.is_broken = True
    rig.generate_asset()
    print("\n--- This rig should only have the default 3 starting assets ---")
    print(rig)

    # --- Test asset generation for Level 0 rig - max items 4 ---
    rig.is_broken = False
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

def take_hit():
    """
    Direct tests for the Rig class for taking damage and determining broken state.

    Tests:
        - Rig taking hits at different upgrade levels.
        - Damage scaling according to rig upgrade level.
        - Rig becoming broken when damage reaches or exceeds threshold.

    Expected behaviour:
        - Each hit increases the rig's damage counter based on its current upgrade level.
            Level 0     +1.0 damage
            Level 1     +0.75 damage
            Level 2     +0.5 damage
            Level 3     +0.25 damage
        - When total damage reaches or exceeds 2.0, the rig becomes broken.
    """

    print("\n=== TEST: Rig Taking a Hit, Damage Taken Varying with Upgrade Level, and Broken State ===\n")

    # --- Create rig ---
    rig = Rig('Mah Computer')

    # --- Take hit of damage 1 for Level 0 rig ---
    rig.take_hit()
    print("\n--- This rig should have damage of 1 ---")
    print(rig)

    # --- Take further hit of damage 1, rig is now broken ---
    rig.take_hit()
    print("\n--- This rig has damage of 2 and is now broken ---")
    print(rig)

    # --- Create a new rig ---
    rig2 = Rig('Mah Better Computer')

    # --- Upgrade rig to level 1 and take hit of damage 0.75 ---
    rig2.upgrade_level = 1
    rig2.take_hit()

    # --- Upgrade rig to level 2 and take hit of damage 0.5 ---
    rig2.upgrade_level = 2
    rig2.take_hit()

    # --- Upgrade rig to level 3 and take hit of damage 0.25 ---
    rig2.upgrade_level = 3
    rig2.take_hit()
    print("\n--- This rig should have total damage of 0.75 + 0.5 + 0.25 = 1.5 ---")
    print(rig2)

def show_condition():
    """
    Direct tests for Rig class to display condition based on damage level and broken state.

    Tests:
        - Displaying rig condition are various damage levels.
        - Displaying change of upgrade level.
        - Displaying broken state when applicable.

    Expected behaviour:
        - Damage = 0 is pristine condition.
        - Damage > 0 and <1 is slightly damaged.
        - Damage >= 1 and < 2 is heavily damaged.
        - Damage >=2 is broken
        - Broken state = True overrides at any damage level to display as broken state.
        - Upgrade level is reflected in output messages.
    """
    print("\n=== TEST: Show Condition of Rig ===\n")

    # --- Create rig ---
    rig = Rig('Mah Computer')

    # --- Show pristine condition for undamaged rig ---
    print(rig.show_condition())

    # --- Show partially damaged condition for rig with damage < 1 ---
    rig.damage_counter = 0.75
    print(rig.show_condition())

    # --- Show heavily damaged condition for rig with damage >= 1 and < 2 ---
    rig.damage_counter = 1.0
    print(rig.show_condition())
    rig.damage_counter = 1.75
    print(rig.show_condition())

    # --- Show broken condition for rig with damage >= 2 ---
    rig.damage_counter = 2
    print(rig.show_condition())

    # --- Show rig with different upgrade level ---
    rig.damage_counter = 0
    rig.upgrade_level = 2
    print(rig.show_condition())

    # --- Show broken rig will display as broken regardless of damage counter ---
    rig.is_broken = True
    print(rig.show_condition())

def create_set_display_hacker():
    """
    Direct tests for the Hacker class for hacker creation, setting attributes and string display.

    Tests:
     - Creation of a hacker instance.
     - Changing name, rig, trace_level, and is_exposed manually.
     - Displaying string representations.

     Expected behaviour:
     - Hacker should be created successfully.
     - Valid changes should be applied and displayed in string representation.
     - Invalid changes should not be applied and string representation should be displayed unchanged.
    """
    print("\n=== TEST: Create, Modify and Display Hacker ===\n")

    # --- Create and display hacker ---
    hacker = Hacker('Neo')
    print("--- Newly created hacker ---")
    print(hacker)

    # --- Modify attributes to valid values and display new values ---
    hacker.name = 123456        # Value will be converted to a string
    hacker.trace_level = 3      # Valid integer in range 0-5
    hacker.is_exposed = True    # Valid boolean value
    hacker.rig = Rig('Old Rig') # Valid Rig object
    print("--- Hacker with modified attributes ---")
    print(hacker)

    # --- Attempt to modify attributes to invalid values ---
    hacker.trace_level = 6      # Out of range 0-5
    hacker.trace_level = -1     # Out of range 0-5
    hacker.trace_level = 'abc'  # Not an integer
    hacker.is_exposed = 'yes'   # Not boolean value
    hacker.rig = 'New Rig'      # Not a Rig object
    print("--- Hacker with no invalid changes - same as previous display ---")
    print(hacker)

def scan_add_remove_inventory():
    """
        Direct tests for the Hacker class for adding and removing assets from inventory.

        Tests:
         - Adding assets (valid and invalid) to a hacker's inventory.
         - Removing assets (valid, invalid, and encrypted) from a hacker's inventory.

         Expected behaviour:
         - Valid assets should be successfully added and removed from inventory.
         - Invalid assets should not be added or removed from inventory.
         - Encrypted assets should not be removed from inventory.

         Notes:
             - scan_inventory function indirectly tested via its utilisation in remove_asset function.
             - There are no limits on inventory capacity.
        """
    print("\n=== TEST: Search, Add and Remove Assets from Hacker's Inventory ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')
    print("--- This new hacker should have default inventory of 1x CryptoToken ---")
    print(hacker)

    # --- Create valid and invalid assets ---
    valid_asset = Asset('CryptoToken')
    valid_asset.is_encrypted = True
    invalid_asset = Asset('USB')        # Not a valid asset name (type)
    non_asset = 'harddrive'             # Not an Asset object

    # --- Add assets to hacker's inventory and display ---
    hacker.add_asset(valid_asset)
    hacker.add_asset(invalid_asset)
    hacker.add_asset(non_asset)
    print("\n--- This hacker should now have 2x CryptoTokens (one encrypted) ---")
    print(hacker)

    # --- Remove assets from hacker's inventory and display ---
    hacker.remove_asset('CryptoToken')     # Valid asset to be removed
    hacker.remove_asset('Security Chip')   # Attempt to remove asset not found in inventory
    hacker.remove_asset('CryptoToken')     # Attempt to remove encrypted asset from inventory
    print("--- This hacker should now have only one encrypted CryptoToken left in inventory ---")
    print(hacker)

def acquire_rig():
    """
    Tests rig acquisition for the Hacker class.

    Tests:
        - Attempting rig acquisition without a CryptoToken in inventory.
        - Attempting rig acquisition with an encrypted CryptoToken in inventory.
        - Successful rig acquisition using an unencrypted CryptoToken.
        - Attmeping to acquire an additional rig when one is already owned.

    Expected behaviour:
        - Hacker cannot acquire a rig without an unencrypted CryptoToken.
        - Upon rig acquisition, one CryptoToken is consumed and the hacker gains a rig.
        - Hacker cannot acquire another rig if one is already owned.
    """
    print("\n=== TEST: Acquisition of Rig by Hacker ===")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Attempt rig acquisition with no CryptoToken ---
    hacker.remove_asset('CryptoToken')
    print(hacker)
    hacker.acquire_rig('Mah Rig')

    # --- Attempt rig acquisition with encrypted CryptoToken ---
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)
    hacker.acquire_rig('Mah Rig Take 2')

    # Successful acquisition of rig with unencrypted CryptoToken
    hacker.add_asset(Asset('CryptoToken'))
    print(hacker)
    hacker.acquire_rig('Mah Rig Take 3')
    print(hacker)

    # Attempt acquisition when a rig is already present
    hacker.acquire_rig('New Rig')

# Tests repair rig function for Hacker (exceptions and successful)
def repair_rig():
    """
    Tests rig repair for the Hacker class.

    Tests:
        - Attempting to repair rig without a rig present.
        - Attempting to repair rig when rig is undamaged.
        - Attempting to repair rig without an encrypted CryptoToken available.
        - Successfully repairing a damaged rig using an unencrypted CryptoToken.

    Expected behaviour:
        - Hacker cannot perform rig repair without a rig.
        - Repair action is blocked if the rig has no damage.
        - Encrypted CryptoTokens cannot be used for rig repair.
        - Upon successful repair, one CryptoToken is consumed, the rig's damage counter
            resets to 0 and is no longer broken.
    """
    print("\n=== TEST: Repair of Rig by Hacker ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Attempt repair without a rig ---
    hacker.repair_rig()

    # --- Attempt repair when rig is not damaged ---
    hacker.acquire_rig('Mah Rig')
    hacker.repair_rig()

    # --- Attempt repair of damaged rig without unencrypted CryptoToken available ---
    hacker.rig.damage_counter = 2
    hacker.rig.is_broken = True
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)
    print(hacker.rig)
    hacker.repair_rig()

    # --- Successful rig repair with unencrypted CryptoToken ---
    hacker.add_asset(Asset('CryptoToken'))
    print(hacker)
    hacker.repair_rig()
    print(hacker)
    print(hacker.rig)

def upgrade_rig():
    """
    Tests rig upgrade for the Hacker class.

    Tests:
        - Attempting to upgrade rig without a rig present.
        - Attempting to upgrade rig when maximum upgrade level (3) is already reached.
        - Attempting to upgrade rig without an encrypted Hardware Patch available.
        - Successfully upgrading a rig using an unencrypted Hardware Patch.

    Expected behaviour:
        - Hacker cannot perform rig upgrade without a rig.
        - Upgrade action is blocked if the rig is already at maximum upgrade level (3).
        - Encrypted Hardware Patches cannot be used for rig upgrades.
        - Upon successful upgrade, one Hardware Patch is consumed and the rig's upgrade level increments by 1.
    """
    print("\n=== TEST: Upgrade of Rig by Hacker ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Attempt upgrade without a rig ---
    hacker.upgrade_rig()

    # --- Attempt upgrade when rig is already at maximum level ---
    hacker.acquire_rig('Mah Rig')
    hacker.rig.upgrade_level = 3
    hacker.upgrade_rig()

    # --- Attempt upgrade without unencrypted Hardware Patch in inventory ---
    hacker.rig.upgrade_level = 0
    asset = Asset('Hardware Patch')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)
    hacker.upgrade_rig()

    # --- Successful rig upgrade with unencrypted Hardware Patch ---
    hacker.add_asset(Asset('Hardware Patch'))
    print(hacker)
    hacker.upgrade_rig()
    print(hacker)
    print(hacker.rig)

def encrypt_asset():
    """
    Tests for encrypt asset function by Hacker, covering all major conditions and edge cases.

    Tests:
        - Attempting encryption when the hacker has no rig and no Security Chip in inventory.
        - Attempting encryption when no Security Chip is available in inventory or storage.
        - Attempting encryption when only encrypted Security Chips are available.
        - Successful encryption of an asset from storage using Security Chip from storage.
        - Successful encryption of an asset from inventory using Security Chip from inventory.
        - Attempting encryption when only encrypted target assets remain.

    Expected behaviour:
        - Encryption should only occur if at least one unencrypted target asset and one
            unencrypted Security Chip are available in either inventory or storage.
        - The Security Chip used for encryption should be removed after successful encryption.
        - Storage should be the preferred source over inventory for both target assets and
            Security Chips if they are available in both places.
    """
    print("\n=== TEST: Encryption of Assets by Hacker ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Attempt encryption without rig or Security Chip in inventory ---
    hacker.encrypt_asset('CryptoToken')

    # --- Acquire and upgrade rig ---
    hacker.acquire_rig('My Computer')
    hacker.rig.upgrade_level = 3

    # --- Attempt encryption with no Security Chip in storage or inventory ---
    hacker.encrypt_asset('Data Spike')

    # --- Attempt encryption with encrypted Security chips in storage and inventory ---
    asset1 = Asset('Security Chip')
    asset2 = Asset('Security Chip')
    asset1.is_encrypted = True
    asset2.is_encrypted = True
    hacker.add_asset(asset1)
    hacker.rig.add_asset(asset2)
    hacker.encrypt_asset('Data Spike')

    # --- Add assets to inventory and storage for testing and display contents ---
    hacker.add_asset(Asset('Security Chip'))
    hacker.add_asset(Asset('Security Chip'))
    hacker.rig.add_asset(Asset('Security Chip'))
    hacker.add_asset(Asset('Removable Drive'))
    asset3 = Asset('Removable Drive')
    asset3.is_encrypted = True
    hacker.rig.add_asset(asset3)
    print(hacker)
    print(hacker.rig)

    # --- Successful encryption with target asset from storage and Security Chip from storage ---
    hacker.encrypt_asset('Removable Drive')
    print(hacker)
    print(hacker.rig)

    # --- Successful encryption with target asset from inventory and Security Chip from inventory ---
    hacker.encrypt_asset('Removable Drive')
    print(hacker)
    print(hacker.rig)

    # --- Attempt encryption with no unencrypted target assets available ---
    hacker.encrypt_asset('Removable Drive')
    print(hacker)
    print(hacker.rig)

def decrypt_asset():
    """
    Tests for decrypt asset function by Hacker, covering all major conditions and edge cases.

    Tests:
        - Attempting decryption when the hacker has no rig and no Security Chip in inventory.
        - Attempting decryption when no Security Chip is available in inventory or storage.
        - Attempting decryption when only encrypted Security Chips are available.
        - Successful decryption of an asset from storage using Security Chip from storage.
        - Successful decryption of an asset from inventory using Security Chip from inventory.
        - Attempting decryption when only decrypted target assets remain.

    Expected behaviour:
        - Decryption should only occur if at least one encrypted target asset and one
            unencrypted Security Chip are available in either inventory or storage.
        - The Security Chip used for decryption should be removed after successful decryption.
        - Storage should be the preferred source over inventory for both target assets and
            Security Chips if they are available in both places.
    """
    print("\n=== TEST: Decryption of Assets by Hacker ===")

    # --- Create hacker and add encrypted asset to inventory ---
    hacker = Hacker('Neo')
    asset = Asset('CryptoToken')
    asset.is_encrypted = True
    hacker.add_asset(asset)
    print(hacker)

    # --- Attempt decryption without rig or Security Chip in inventory ---
    hacker.decrypt_asset('CryptoToken')

    # --- Acquire and upgrade rig ---
    hacker.acquire_rig('My Computer')
    hacker.rig.upgrade_level = 3

    # --- Attempt decryption with no Security Chip in storage or inventory ---
    hacker.decrypt_asset('CryptoToken')

    # --- Attempt decryption with encrypted Security chips in storage and inventory ---
    asset1 = Asset('Security Chip')
    asset2 = Asset('Security Chip')
    asset1.is_encrypted = True
    asset2.is_encrypted = True
    hacker.add_asset(asset1)
    hacker.rig.add_asset(asset2)
    hacker.decrypt_asset('CryptoToken')

    # --- Add assets to inventory and storage for testing and display contents ---
    hacker.add_asset(Asset('Security Chip'))
    hacker.add_asset(Asset('Security Chip'))
    hacker.rig.add_asset(Asset('Security Chip'))
    hacker.add_asset(Asset('CryptoToken'))
    asset3 = Asset('CryptoToken')
    asset3.is_encrypted = True
    hacker.rig.add_asset(asset3)
    print(hacker)
    print(hacker.rig)

    # --- Successful decryption with target asset from storage and Security Chip from storage ---
    hacker.decrypt_asset('CryptoToken')
    print(hacker)
    print(hacker.rig)

    # --- Successful decryption with target asset from inventory and Security Chip from inventory ---
    hacker.decrypt_asset('CryptoToken')
    print(hacker)
    print(hacker.rig)

    # --- Attempt decryption with no encrypted target assets available ---
    hacker.decrypt_asset('CryptoToken')
    print(hacker)
    print(hacker.rig)

def change_trace():
    """
    Direct tests for increasing and reducing trace and associated exposure for Hacker.

    Tests:
        - Increasing trace level by a specified amount.
        - Reducing trace level.

    Expected behaviour:
        - Trace level will increase by amount specified. If trace level >= 5, the hacker becomes exposed.
        - Reduce trace function will reduce trace level by 1 each time it is called.
        - When trace level falls below 5, the hacker is no longer exposed.
        - Trace cannot be reduced below 0.
    """
    print("\n=== TEST: Increase and Reduce Hacker's Trace Level and Corresponding Exposure ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Directly increase hacker's trace level until exposed ---
    hacker.increase_trace(1)
    hacker.increase_trace(2)
    hacker.increase_trace(2)
    print(hacker)

    # --- Reduce hacker's trace level and change exposure ---
    hacker.reduce_trace()
    print(hacker)

    # --- Continue to reduce hacker's trace level ---
    hacker.reduce_trace()
    hacker.reduce_trace()
    hacker.reduce_trace()
    hacker.reduce_trace()

    # --- Attempt to reduce trace level below 0 ---
    hacker.reduce_trace()

def store_asset():
    """
    Docstring here
    """
    print("\n=== TEST: Storage of Assets by Hacker ===\n")

    # --- Create hacker ---
    hacker = Hacker('Neo')

    # --- Attempt to store assets while exposed ---
    hacker.is_exposed = True
    hacker.store_asset('all')

    # --- Attempt to store assets with no rig ---
    hacker.is_exposed = False
    hacker.store_asset('all')

    # --- Acquire rig and add assets to inventory ---
    hacker.acquire_rig('My Computer')
    hacker.rig.upgrade_level = 3
    hacker.add_asset(Asset('CryptoToken'))
    hacker.add_asset(Asset('CryptoToken'))
    hacker.add_asset(Asset('CryptoToken'))
    hacker.add_asset(Asset('Security Chip'))
    hacker.add_asset(Asset('Security Chip'))
    asset = Asset('Data Spike')
    asset.is_encrypted = True
    asset2 = Asset('Data Spike')
    asset2.is_encrypted = True
    hacker.add_asset(asset)
    hacker.add_asset(asset2)
    print(hacker)
    print(hacker.rig)

    # --- Transfer of single assets ---
    hacker.store_asset('CryptoToken')       # Available for transfer
    hacker.store_asset('CryptoToken')       # Available for transfer
    hacker.store_asset('Security Chip')     # Available for transfer
    hacker.store_asset('Removable Drive')   # Not available in inventory
    hacker.store_asset('Data Spike')        # Encrypted
    print(hacker)
    print(hacker.rig)

    # --- Transfer of all remaining assets and exposure threshold reached ---
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


# Runs testing functions for program
def main():
    #create_set_display_assets()

    #create_set_display_rig()
    #scan_add_remove_storage()
    #generate_asset()
    #take_hit()
    #show_condition()

    #create_set_display_hacker()
    #scan_add_remove_inventory()
    #acquire_rig()
    #repair_rig()
    #upgrade_rig()

    #encrypt_asset()
    #decrypt_asset()

    change_trace()

    #store_asset()
    #retrieve_asset()

    #launch_attack()
    #extract_assets()


main()
