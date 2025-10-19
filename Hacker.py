"""
File: Hacker.py
Description: Hacker class, representing a cyberpunk hacker, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig


class Hacker:
    """
    Represents a hacker character who may own a rig (computer) and manages a set of digital assets.

    The Hacker class models an individual in a cyber environment, tracking their identity, rig (computer)
    ownership, inventory of assets, trace level (indicating detection risk), and exposure status.
    """

    def __init__(self, name):
        """
        Initialises a new Hacker instance.

        Args:
            name (str): The name of the hacker.

        Attributes:
            __name (str): The hacker's name.
            __rig (Rig | None): The hacker's current rig, initially None.
            __inventory (list[Asset]): A list of Asset objects held by the hacker, initially a single
                                    'CryptoToken' asset.
            __trace_level (int): How close the hacker is to being traced (0-5), initially 0.
            __is_exposed (bool): Indicates whether the hacker has been exposed, initially False.
        """
        self.__name = name
        self.__rig = None
        self.__inventory = [Asset('CryptoToken')]
        self.__trace_level = 0
        self.__is_exposed = False

    # --------------
    # Getter methods
    # --------------

    def get_name(self):
        """Returns the hacker's name."""
        return self.__name

    def get_rig(self):
        """Returns the hacker's rig object, or None if none is acquired."""
        return self.__rig

    def get_inventory(self):
        "Returns a list of Asset objects representing the hacker's inventory."
        return self.__inventory

    def get_trace_level(self):
        """Returns the hacker's current trace level (0-5)."""
        return self.__trace_level

    def get_is_exposed(self):
        """Returns whether the Hacker is exposed (True/False)."""
        return self.__is_exposed

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Sets the hacker's name.

        Args:
            name (str): The new name for the hacker, automatically converted to a string.
        """
        self.__name = str(name)

    def set_rig(self, rig):
        """
        Assigns a rig to the hacker.

        Args:
            rig (Rig): A Rig instance to assign as the hacker's rig. Must be Rig class.
        """
        if isinstance(rig, Rig):
            self.__rig = rig

    def set_trace_level(self, trace):
        """
        Sets the hacker's trace level.

        Args:
        trace (int): A value between 0 and 5 inclusive.
        """
        if isinstance(trace, int) and 0 <= trace <= 5:
            self.__trace_level = trace

    def set_is_exposed(self, exposed):
        """
        Sets the hacker's exposure status.

        Args:
            exposed (bool): True if the hacker is exposed, False otherwise.
        """
        if isinstance(exposed, bool):
            self.__is_exposed = exposed

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    rig = property(get_rig, set_rig)
    inventory = property(get_inventory)
    trace_level = property(get_trace_level, set_trace_level)
    is_exposed = property(get_is_exposed, set_is_exposed)

    # -------------------
    # Behavioural methods
    # -------------------

    def scan_inventory(self, asset_name, unsecured):
        """
        Searches the hacker's inventory for an asset by name.

        Args:
            asset_name (str): The name of the asset to search for.
            unsecured (bool): Only search for unencrypted (available) assets if True,
                                search all assets including encrypted assets is False

        Returns:
            int | None: The index of the asset if found, otherwise None.
        """
        item_index = None
        for item in self.inventory:
            if item.name == asset_name:
                if unsecured:
                    if not item.is_encrypted:
                        item_index = self.inventory.index(item)
                else:
                    if item.is_encrypted:
                        item_index = self.inventory.index(item)
        return item_index

    def add_asset(self, asset):
        """
        Adds an asset to the hacker's inventory.

        Args:
             asset (Asset): The asset to be added.
        """
        if isinstance(asset, Asset):
            self.__inventory.append(asset)

    def remove_asset(self, asset_name):
        """
        Removes an asset from inventory by name, if it exists and is unencrypted.

        Args:
            asset_name (str): The name of the asset to remove.
        """
        index = self.scan_inventory(asset_name, True)
        if index is not None:
            del self.__inventory[index]

    def acquire_rig(self, name):
        """
        Acquires a new rig in exchange for a CryptoToken from inventory.

        The method checks that:
            - The hacker does not already have a rig
            - The hacker has a CryptoToken (unencrypted) available in inventory.

        If all conditions are satisfied, the hacker acquires a rig.

        Args:
              name (str): The name to assign to the newly acquired rig.
        """
        required = 'CryptoToken'
        if self.rig is not None:
            print("You already have a rig!")
        elif self.scan_inventory(required, True) is None:
            print(f"You cannot acquire a rig - you need an unencrypted {required} in your inventory.")
        else:
            # Assigns Rig asset to rig attribute
            self.rig = Rig(name)
            print(f"Congratulations, {self.name}! You have activated your rig.")
            # Removes 'used' asset from inventory
            self.remove_asset(required)

    def repair_rig(self):
        """
        Repairs all damage to the hacker's rig using a CryptoToken from inventory.

        The method checks that:
            - The hacker owns a rig.
            - The rig is damage or broken (i.e. needs repair).
            - The hacker has a CryptoToken (unencrypted) available in inventory.

        If all conditions are satisfied, the rig's damage counter is set to 0
        and its broken status to False.
        """
        required = 'CryptoToken'
        if self.rig is None:
            print(f"You do not have a rig!")
        else:
            if self.rig.damage_counter == 0 and not self.rig.is_broken:
                print("No repair is needed. Your rig is not damaged.")
            elif self.scan_inventory(required, True) is None:
                print(f"You cannot perform this repair - you need an unencrypted {required} in your inventory.")
            else:
                # Repairs damage to rig
                self.rig.damage_counter = 0
                self.rig.is_broken = False
                print(f"Your rig has been repaired and restored to pristine condition.\n")
                # Removes 'used' asset from inventory
                self.remove_asset(required)

    def upgrade_rig(self):
        """
        Upgrades the hacker's rig using a Hardware Patch from inventory.

        The method checks that:
            - The hacker owns a rig.
            - The rig has not already reached the maximum upgrade level (3).
            - The hacker has a Hardware Patch (unencrypted) available in inventory.

        If all conditions are satisfied, the rig's upgrade level increases by 1.
        """
        required = 'Hardware Patch'
        if self.rig is None:
            print(f"You do not have a rig!")
        else:
            if self.rig.upgrade_level == 3:
                print("You cannot upgrade this rig - maximum upgrade level reached.")
            elif self.scan_inventory(required, True) is None:
                print(f"You cannot perform this upgrade - you need an unencrypted {required} in your inventory.")
            else:
                # Upgrades the rig
                self.rig.upgrade_level += 1
                print(f"Your rig has been upgraded to level {self.rig.upgrade_level}.")
                # Removes 'used' asset from inventory
                self.remove_asset(required)

    def scan_both(self, asset_name, unsecured):
        if self.rig is not None:
            index_storage = self.rig.scan_storage(asset_name, unsecured)
            in_storage = False if index_storage is None else True
        else:
            in_storage = False
        index_inventory = self.scan_inventory(asset_name, unsecured)
        in_inventory = False if index_inventory is None else True
        if not in_storage and not in_inventory:
            return None
        elif in_storage:
            return self.rig.storage[index_storage]
        else:
            return self.inventory[index_inventory]

    def encrypt_asset(self, asset_name):
        """
        Encrypts an asset in the hacker's inventory or in their rig's storage using a Security Chip.

        The method checks that:
            - The hacker has a Security Chip (unencrypted) available in either inventory or storage.
            - The asset exists and is currently unencrypted in either inventory or storage.

        If all conditions are satisfied, the first matching unencrypted asset found (storage preferred)
        will be encrypted and a Security Chip will be consumed (storage preferred).

        Args:
            asset_name (str): The name (type) of asset to encrypt (e.g. 'Removable Drive').
        """
        required = 'Security Chip'
        # Ensures unencrypted Security Chip is available to use in storage or inventory before proceeding
        if self.scan_both(required, True) is None:
            print(f"You cannot perform this encryption - you need an unencrypted {required} in your"
                  f" storage or inventory.")
        else:
            # Ensures an unencrypted target asset exists in storage or inventory before proceeding
            if self.scan_both(asset_name, True) is None:
                print(f"You do not have an unencrypted {asset_name} in your storage or inventory to encrypt.")
            else:
                # Encrypts the requested asset
                self.scan_both(asset_name, True).is_encrypted = True
                print(f"Your {asset_name} has now been encrypted.")
                # Removes 'used' Security Chip from storage or inventory
                if self.rig.scan_storage(required, True) is not None:
                    self.rig.remove_asset(required)
                else:
                    self.remove_asset(required)

    def decrypt_asset(self, asset_name):
        """
        Decrypts an asset in the hacker's inventory or in their rig's storage using a Security Chip.

        The method checks that:
            - The hacker has a Security Chip (unencrypted) available in either inventory or storage.
            - The asset exists and is currently encrypted in either inventory or storage.

        If all conditions are satisfied, the first matching encrypted asset found (storage preferred)
        will be decrypted and a Security Chip will be consumed (storage preferred).

        Args:
            asset_name (str): The name (type) of asset to decrypt (e.g. 'Removable Drive').
        """
        required = 'Security Chip'
        # Ensures unencrypted Security Chip is available to use in storage or inventory before proceeding
        if self.scan_both(required, True) is None:
            print(f"You cannot perform this decryption - you need an unencrypted {required} in your"
                  f" storage or inventory.")
        else:
            # Ensures an encrypted target asset exists in storage or inventory before proceeding
            if self.scan_both(asset_name, False) is None:
                print(f"You do not have an encrypted {asset_name} in your storage or inventory to decrypt.")
            else:
                # Decrypts the requested asset
                self.scan_both(asset_name, False).is_encrypted = False
                print(f"Your {asset_name} has now been decrypted.")
                # Removes 'used' Security Chip from storage or inventory
                if self.rig.scan_storage(required, True) is not None:
                    self.rig.remove_asset(required)
                else:
                    self.remove_asset(required)

    def increase_trace(self, amount):
        """
        Increases the hacker's trace level as a result of performing a risky action.

        If trace level then meets or exceeds 5, the hacker becomes exposed and cannot perform further risky actions
        until their trace is reduced.

        Args:
            amount (int): The amount by which to increase the hacker's trace level.
        """
        self.trace_level += amount
        print(f"Your trace level is now {self.trace_level}.")
        if self.trace_level >= 5:
            self.is_exposed = True
            print(f"You are now exposed!!! Be careful, and reduce your trace.")

    def reduce_trace(self):
        """
        Reduces the hacker's trace level by 1.

        This simulates the hacker laying low to avoid detection. If the trace level is already 0,
        no reduction occurs. If the trace level is reduced below 5, the hacker is no longer exposed.
        """
        if self.trace_level > 0:
            self.trace_level -= 1
            if self.trace_level < 5:
                self.is_exposed = False
                print(f"You have laid low and reduced your trace. Your trace level is now {self.trace_level}.")
        else:
            print("Your trace level is already 0, you cannot reduce your trace further.\n")

    # TODO: If storage is full - need to STOP moving assets, and if no assets to move, need error message
    def store_asset(self, asset_name):
        """
        Moves a specific asset (or all assets) FROM the hacker's inventory TO the rig's storage.

        Behaviour:
            - If asset_name == 'all', attempt to move all unencrypted assets from inventory to storage.
            - Otherwise, move a single matching (and unencrypted) asset from inventory to storage.
            - If the hacker is exposed, no rig is equipped, or the asset is not present, the operation is not performed.

        Args:
            asset_name (str): The name of the asset to store, or 'all' to store all available assets.
        """
        if self.is_exposed:
            print("You cannot store assets while exposed. Reduce your exposure level.")
        else:
            if self.rig is None:
                print("You cannot store assets - you do not have a rig to store them in.")
            else:
                if asset_name == 'all':
                    for item in list(self.inventory):
                        if item.is_encrypted == False:
                            self.rig.add_asset(item)
                            self.remove_asset(item.name)
                    self.trace_level += 2
                    print(f"You have moved all unencrypted assets from inventory to storage. Your trace level is"
                          f" now {self.trace_level}.")
                    if self.trace_level >= 5:
                        self.is_exposed = True
                        print(f"You are now exposed!!! Be careful, and reduce your trace.")
                else:
                    if self.scan_inventory(asset_name, True) is None:
                        print(f"You cannot store a {asset_name}, you do not have an unencrypted {asset_name}"
                              f" in your inventory.")
                    else:
                        self.rig.add_asset(Asset(asset_name))
                        self.remove_asset(asset_name)
                        self.trace_level += 1
                        print(f"You have moved a {asset_name} from inventory to storage. Your trace level is"
                              f" now {self.trace_level}.")
                        if self.trace_level >= 5:
                            self.is_exposed = True
                            print(f"You are now exposed!!! Be careful, and reduce your trace.")

    def retrieve_asset(self, asset_name):
        """
        Moves a specific asset (or all assets) FROM the rig's storage TO the hacker's inventory.

        Behaviour:
            - If asset_name == 'all', attempt to move all unencrypted assets from storage to inventory.
            - Otherwise, move a single matching (and unencrypted) asset from storage to inventory.
            - If the hacker is exposed, no rig is equipped, or the asset is not present, the operation is not performed.
        Args:
            asset_name (str): The name of the asset to retrieve, or 'all' to retrieve all available assets.
        """
        if self.is_exposed:
            print("You cannot retrieve assets while exposed. Reduce your exposure level.")
        else:
            if self.rig is None:
                print("You cannot retrieve assets - you do not have a rig to retrieve them from.")
            else:
                if asset_name == 'all':
                    for item in list(self.rig.storage):
                        if item.is_encrypted == False:
                            self.add_asset(item)
                            self.rig.remove_asset(item.name)
                else:
                    if self.rig.scan_storage(asset_name, True) is not None:
                        del self.rig.storage[self.rig.scan_storage(asset_name, True)]
                        self.add_asset(Asset(asset_name))
                    else:
                        return None

    def launch_attack(self, target_rig):
        """
        Launchs a data spike attack against a target rig.

        Requirements:
            - The hacker must not be currently exposed.
            - The hacker must have an equipped rig containing a 'Data Spike' asset.

        Behaviour:
            - Removes one 'Data Spike' from storage on the hacker's rig.
            - Increments the hacker's trace level.
            - Marks the hacker as exposed if the trace level reaches the exposure threshold (5).
            - Calls take_hit() on the target rig.

        Args:
            target_rig(Rig): The rig being attacked.
        """
        if not self.is_exposed:
            required = 'Data Spike'
            if self.rig == None:
                print("You cannot launch an attacked - you do not have a rig!\n")
            elif self.rig.scan_storage(required) == None:
                print(f"You cannot launch an attack - you need a {required} in your rig's storage.\n")
            else:
                self.rig.remove_asset(required)
                self.trace_level += 1
                print(f"Congratulations, {self.name}! You have hit the target rig, {target_rig.name}. Your trace level"
                      f" is now {self.trace_level}.\n")
                if self.trace_level >= 5:
                    self.is_exposed = True
                    print(f"You are now exposed!!! Be careful, and reduce your trace.\n")
                target_rig.take_hit()
        else:
            print("You cannot launch a data spike while exposed. Reduce your exposure level.")

    def extract_assets(self, target_rig):
        """
        Extracts unsecured assets from a target rig that is broken.

        Requirements:
        - The hacker must not be exposed.
        - The hacker must have an equipped rig containing a 'Removable Drive' asset.
        - The target rig must be broken.

       Behaviour:
        - Transfers unencrypted assets from the target rig's storage into the hacker's inventory.
        - Consumes the 'Removable Drive' used to extract from the hacker's rig.
        - Increments the hacker's trace level and handles exposure threshold.

        Args:
            target_rig (Rig): The broken rig from which assets are to be extracted.
        """
        if not self.is_exposed:
            required = 'Removable Drive'
            if self.rig == None:
                print("You cannot extract assets - you do not have a rig!\n")
            elif self.rig.scan_storage(required) == None:
                print(f"You cannot extract assets - you need a {required} in your rig's storage.\n")
            elif target_rig.is_broken == False:
                print(f"You cannot extract assets from this rig - it is not broken!\n")
            else:
                # Still need to fix these loops for duplicate items!!!!!!
                for item in target_rig.storage:
                    if item.is_encrypted == False:
                        self.add_asset(item)
                        target_rig.remove_asset(item.name)
                self.rig.remove_asset(required)
                print(f"Congratulations, {self.name}! You have extracted the unsecured assets from the target rig.\n")
                self.trace_level += 1
                if self.trace_level == 5:
                    self.is_exposed = True
                    print(f"You are now exposed!!! Be careful, and reduce your trace.")
        else:
            print("You cannot extract assets while exposed. Reduce your exposure level.")

    def __str__(self):
        """
        Returns a formatted string containing the hacker's details.

        Returns:
            str: The name, rig name, trace level, and inventory contents.
        """
        details = [f"\nHacker's Name: {self.name}"]
        if self.rig is None:
            details.append(f"This hacker has no rig!")
        else:
            details.append(f"Rig Name: {self.rig.name}")
        details.append(f"Trace Level: {self.trace_level}")
        if self.is_exposed:
            details.append("This hacker is exposed!")
        if self.inventory == []:
            details.append("This hacker has no inventory.")
        else:
            details.append(f"Inventory Contents:")
            for item in self.inventory:
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)
