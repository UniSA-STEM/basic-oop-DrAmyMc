"""
File: Hacker.py
Description: Hacker class, representing a cyberpunk hacker, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports related Asset and Rig classes
from Asset import Asset
from Rig import Rig

# Creation of Hacker class
class Hacker:
    """ Documentation for Hacker class """
    # The hacker is created with a name parameter, inventory is initialised with starting asset, and all other attributes are set to initial defaults
    def __init__(self, name):
        self.__name = name
        self.__rig = None
        self.__inventory = [Asset('CryptoToken')]
        self.__trace_level = 0
        self.__is_exposed = False

    # Getter functions for each attribute
    def  get_name(self):
        return self.__name

    def get_rig(self):
        return self.__rig

    def get_inventory(self):
        return self.__inventory

    def get_trace_level(self):
        return self.__trace_level

    def get_is_exposed(self):
        return self.__is_exposed

    # Setter functions for each appropraite attribute
    def set_name(self, name):
        # Ensures name is stored as a string
        self.__name = str(name)

    def set_rig(self, rig):
        # Ensures only an object of Rig class can be assigned as the hacker's rig
        if isinstance(rig, Rig):
            self.__rig = rig

    def set_trace_level(self, trace):
        # Ensures only valid numbers can be passed to trace level attribute
        if trace >= 0 and trace <= 5:
            self.__trace_level = trace

    def set_is_exposed(self, exposed):
        # Ensures only a True/False value can be passed to exposed status
        if exposed == True or exposed == False:
            self.__is_exposed = exposed

    # Properties for each attribute
    name = property(get_name, set_name)
    rig = property(get_rig, set_rig)
    inventory = property(get_inventory)
    trace_level = property(get_trace_level, set_trace_level)
    is_exposed = property(get_is_exposed, set_is_exposed)

    # Scans inventory to search for an asset by name
    def scan_inventory(self, asset_name):
        item_index = None
        for item in self.inventory:
            if item.name == asset_name:
                item_index = self.inventory.index(item)
        return item_index

    # Adds an asset to hacker's inventory
    def add_asset(self, asset):
        # Ensures only valid assets can be added to inventory
        if isinstance(asset, Asset) and asset.name != 'Invalid':
            self.__inventory.append(asset)

    # Removes an asset from hacker's inventory
    def remove_asset(self, asset_name):
        if self.scan_inventory(asset_name) != None:
            del self.__inventory[self.scan_inventory(asset_name)]
        else:
            return None

    # Acquire a rig in exchange for a CryptoToken
    def acquire_rig(self, name):
        required = 'CryptoToken'
        if self.rig != None:
            print("You already have a rig!\n")
        elif self.scan_inventory(required) == None:
            print(f"You cannot acquire a rig - you need a {required} in your inventory.\n")
        else:
            self.rig = Rig(name)
            self.remove_asset(required)
            print(f"Congratulations, {self.name}! You have activated your rig.\n")

    # Repairs all damage to rig using a CryptoToken from inventory
    def repair_rig(self):
        required = 'CryptoToken'
        if self.rig == None:
            print(f"You do not have a rig!\n")
        else:
            if self.rig.damage_counter == 0 and self.rig.is_broken == False:
                print("No repair is needed. Your rig is not damaged.\n")
            elif self.scan_inventory(required) == None :
                print(f"You cannot perform this repair - you need a {required} in your inventory.\n")
            else:
                self.rig.damage_counter = 0
                self.rig.is_broken = False
                self.remove_asset(required)
                print(f"Your rig has been repaired and restored to pristine condition.\n")

    # Upgrades rig using a Hardware Patch from inventory
    def upgrade_rig(self):
        required = 'Hardware Patch'
        if self.rig == None:
            print(f"You do not have a rig!\n")
        else:
            if self.rig.upgrade_level == 3:
                print("You cannot upgrade this rig - maximum upgrade level reached.\n")
            elif self.scan_inventory(required) == None :
                print(f"You cannot perform this upgrade - you need a {required} in your inventory.\n")
            else:
                self.rig.upgrade_level += 1
                self.remove_asset(required)
                print(f"Your rig has been upgraded to level {self.rig.upgrade_level}.\n")

    # Moves 'all' or specific asset FROM hacker's inventory TO rig's storage
    def store_asset(self, asset_name):
        if asset_name == 'all':
            for item in self.inventory:
                if item.is_encrypted == False:
                    self.rig.add_asset(item)
                    self.remove_asset(item.name)
        else:
            # TODO This bit needs encryption filter as well
            if self.scan_inventory(asset_name) != None:
                del self.inventory[self.scan_inventory(asset_name)]
                self.rig.add_asset(Asset('asset_name'))
            else:
                return None

    # Moves 'all' or specific asset FROM rig's storage TO hacker's inventory
    def retrieve_asset(self, asset_name):
        if asset_name == 'all':
            for item in self.rig.storage:
                if item.is_encrypted == False:
                    self.add_asset(item)
                    self.rig.remove_asset(item.name)
        else:
            # TODO This bit needs encryption filter as well
            if self.rig.scan_storage(asset_name) != None:
                del self.rig.storage[self.rig.scan_storage(asset_name)]
                self.add_asset(Asset('asset_name'))
            else:
                return None

    # Encrypt an asset from inventory or storage
    def encrypt_asset(self, asset_name):
        required = 'Security Chip'
        if self.rig == None and self.scan_inventory(required) == None:
            print(f"You cannot perform this encryption - you need a {required} in your inventory.\n")
        elif self.rig != None and self.scan_inventory(required) == None and self.rig.scan_storage(required) == None:
            print(f"You cannot perform this encryption - you need a {required} in your inventory or storage.\n")
        else:
            if self.rig == None and self.scan_inventory(asset_name) == None:
                 print(f"You cannot encrypt a {asset_name}, as you do not have one in your inventory.\n")
            elif self.rig != None and self.scan_inventory(asset_name) == None and self.rig.scan_storage(asset_name) == None:
                 print (f"You cannot encrypt a {asset_name}, as you do not have one in your inventory or storage.\n")
            else:
                in_inventory = False
                index_inventory = None
                in_storage = False
                index_storage = None
                for item in self.inventory:
                    if item.name == asset_name and item.is_encrypted == False:
                        index_inventory = self.inventory.index(item)
                        in_inventory = True
                for item in self.rig.storage:
                    if item.name == asset_name and item.is_encrypted == False:
                        index_storage = self.rig.storage.index(item)
                        in_storage = True
                if in_inventory == False and in_storage == False:
                    print(f"All of your {asset_name}s are already encrypted.\n")
                elif in_inventory == True:
                    self.inventory[index_inventory].is_encrypted = True
                    if self.scan_inventory(required) != None:
                        self.remove_asset(required)
                    else:
                        self.rig.remove_asset(required)
                    print(f"Your {asset_name} in inventory has now been encrypted.\n")
                elif in_inventory == False and in_storage == True:
                    self.rig.storage[index_storage].is_encrypted = True
                    if self.scan_inventory(required) != None:
                        self.remove_asset(required)
                    else:
                        self.rig.remove_asset(required)
                    print(f"Your {asset_name} in storage has now been encrypted.\n")

    def decrypt_asset(self, asset_name):
        required = 'Security Chip'
        if self.rig == None and self.scan_inventory(required) == None:
            print(f"You cannot perform this decryption - you need a {required} in your inventory.\n")
        elif self.rig != None and self.scan_inventory(required) == None and self.rig.scan_storage(required) == None:
            print(f"You cannot perform this decryption - you need a {required} in your inventory or storage.\n")
        else:
            if self.rig == None and self.scan_inventory(asset_name) == None:
                print(f"You cannot decrypt a {asset_name}, as you do not have one in your inventory.\n")
            elif self.rig != None and self.scan_inventory(asset_name) == None and self.rig.scan_storage(
                    asset_name) == None:
                print(f"You cannot decrypt a {asset_name}, as you do not have one in your inventory or storage.\n")
            else:
                in_inventory = False
                index_inventory = None
                in_storage = False
                index_storage = None
                for item in self.inventory:
                    if item.name == asset_name and item.is_encrypted == True:
                        index_inventory = self.inventory.index(item)
                        in_inventory = True
                for item in self.rig.storage:
                    if item.name == asset_name and item.is_encrypted == True:
                        index_storage = self.rig.storage.index(item)
                        in_storage = True
                if in_inventory == False and in_storage == False:
                    print(f"All of your {asset_name}s are already decrypted.\n")
                elif in_inventory == True:
                    self.inventory[index_inventory].is_encrypted = False
                    if self.scan_inventory(required) != None:
                        self.remove_asset(required)
                    else:
                        self.rig.remove_asset(required)
                    print(f"Your {asset_name} in inventory has now been decrypted.\n")
                elif in_inventory == False and in_storage == True:
                    self.rig.storage[index_storage].is_encrypted = False
                    if self.scan_inventory(required) != None:
                        self.remove_asset(required)
                    else:
                        self.rig.remove_asset(required)
                    print(f"Your {asset_name} in storage has now been decrypted.\n")

    # Launch attack at opponent's rig
    def launch_attack(self, target_rig):
        if self.is_exposed == False:
            required = 'Data Spike'
            if self.rig == None:
                print("You cannot launch an attacked - you do not have a rig!\n")
            elif self.rig.scan_storage(required) == None:
                print(f"You cannot launch an attack - you need a {required} in your rig's storage.\n")
            else:
                self.rig.remove_asset(required)
                self.trace_level += 1
                print(f"Congratulations, {self.name}! You have hit the target rig, {target_rig.name}.")
                print(f"Your trace level is now {self.trace_level}.\n")
                if self.trace_level == 5:
                    self.is_exposed = True
                    print(f"You are now exposed!!! Be careful, and reduce your trace.\n")
                target_rig.take_hit()
        else:
            print("You cannot launch a data spike while exposed. Reduce your exposure level.\n")

    # Extract assets when target rig is broken from attack
    def extract_assets(self, target_rig):
        if self.is_exposed == False:
            required = 'Removable Drive'
            if self.rig == None:
                print("You cannot extract assets - you do not have a rig!\n")
            elif self.rig.scan_storage(required) == None:
                print(f"You cannot extract assets - you need a {required} in your rig's storage.\n")
            elif target_rig.is_broken == False:
                print(f"You cannot extract assets from this rig - it is not broken!\n")
            else:
                for item in target_rig.storage:
                    if item.is_encrypted == False:
                        self.add_asset(item)
                        target_rig.remove_asset(item.name)
                self.rig.remove_asset(required)
                print(f"Congratulations, {self.name}! You have extracted the unsecured assets from the target rig.\n")
                self.trace_level += 1
                if self.trace_level == 5:
                    self.is_exposed = True
                    print(f"You are now exposed!!! Be careful, and reduce your trace.\n")
        else:
            print("You cannot extract assets while exposed. Reduce your exposure level.\n")

    def reduce_trace(self):
        if self.trace_level > 0:
            self.trace_level -= 1
            print (f"You have laid low and reduced your trace. Your trace level is now {self.trace_level}.\n")
        else:
            print("Your trace level is already 0, you cannot reduce your trace further.\n")
    # Returns output for hacker as per assignment specification
    def __str__(self):
        details = []
        details.append(f"Hacker's Name: {self.name}")
        if self.rig is None:
            details.append(f"This hacker has no rig!")
        else:
            details.append(f"Rig Name: {self.rig.name}")
        details.append(f"Trace Level: {self.trace_level}")
        if self.inventory == []:
            details.append(f"This hacker has no inventory!")
        else:
            details.append(f"Inventory Contents:")
            for item in self.inventory:
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)