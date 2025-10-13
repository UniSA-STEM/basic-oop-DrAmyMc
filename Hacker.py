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

    # Setter functions for each attribute
    def set_name(self, name):
        self.__name = name

    def set_rig(self, rig):
        self.__rig = rig

    def set_trace_level(self, trace):
        # Ensures only valid numbers can be passed to trace level attribute
        if trace >= 0 and trace <= 10:
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
        for item in self.get_inventory():
            if item.get_name() == asset_name:
                item_index = self.get_inventory().index(item)
        return item_index

    # Scans storage on rig to search for an asset by name
    def scan_storage(self, asset_name):
        # Ensures rig must be present to be scanned
        if self.get_rig() != None:
            return self.get_rig().scan_storage(asset_name)

    # Adds an asset to hacker's inventory
    def add_asset(self, asset):
        # Ensures only valid assets can be added to inventory
        if isinstance(asset, Asset) and asset.get_name() != 'Invalid':
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
        if self.get_rig() != None:
            print("You already have a rig!\n")
        elif self.scan_inventory(required) == None:
            print(f"You cannot acquire a rig - you need a {required} in your inventory.\n")
        else:
            self.set_rig(Rig(name))
            self.remove_asset(required)
            print(f"Congratulations, {self.__name}! You have activated your rig.\n")

    def store_asset(self):
        pass

    def retrieve_asset(self):
        pass

    # TODO: Need to link with attacked rig and their exposure status?
    def launch_attack(self, target_rig):
        if self.get_is_exposed() == False:
            required = 'Data Spike'
            if self.get_rig() == None:
                print("You cannot launch an attacked - you do not have a rig!\n")
            elif self.scan_storage(required) == None:
                print(f"You cannot launch an attack - you need a {required} in your rig's storage.\n")
            else:
                self.get_rig().remove_asset(required)
                self.set_trace_level(self.get_trace_level() + 1)
                print(f"Congratulations, {self.get_name()}! You have hit the target rig, {target_rig.get_name()}.")
                print(f"Your trace level is now {self.get_trace_level()}.\n")
                if self.get_trace_level() == 5:
                    self.set_is_exposed(True)
                    print(f"You are now exposed!!! Be careful, and reduce your trace.\n")
        else:
            print("You cannot launch a data spike while exposed. Reduce your exposure level.\n")

    # Extract assets when target rig is broken from attack
    def extract_assets(self, target_rig):
        if self.get_is_exposed() == False:
            required = 'Removable Drive'
            if self.get_rig() == None:
                print("You cannot extract assets - you do not have a rig!\n")
            elif self.scan_storage(required) == None:
                print(f"You cannot extract assets - you need a {required} in your rig's storage.\n")
            else:
                # TODO Need to actually get the assets here!!!!!
                self.get_rig().remove_asset(required)
                print(f"Congratulations, {self.get_name()}! You have extracted the unsecured assets from the target rig.\n")
                self.set_trace_level(self.get_trace_level() + 1)
                if self.get_trace_level() == 5:
                    self.set_is_exposed(True)
                    print(f"You are now exposed!!! Be careful, and reduce your trace.\n")
        else:
            print("You cannot extract assets while exposed. Reduce your exposure level.\n")

# TODO: THIS IS VERY MUCH IN PROCESS - does security chip need to be in inventory, or in rig storage? Need separate method for
    #inventoy versus storage, encryption versus decryption???
    def encrypt_inventory(self, asset):
        required = 'Security Chip'
        if self.get_damage_counter() == 0 and self.get_is_broken() == False:
            print("No repair is needed.\n")
        elif self.scan_storage(required) == None:
            print(f"You cannot perform this repair - you need a {required} in your storage.\n")
        else:
            self.set_damage_counter(0)
            self.set_is_broken(False)
            self.remove_asset(required)
            print(f"Your rig has been repaired and restored to pristine condition.")

    def decrypt_asset(self, asset):
        pass

    # Returns output for hacker as per assignment specification
    def __str__(self):
        details = []
        details.append(f"Hacker's Name: {self.get_name()}")
        if self.__rig is None:
            details.append(f"This hacker has no rig!")
        else:
            details.append(f"Rig Name: {self.get_rig().get_name()}")
        details.append(f"Trace Level: {self.get_trace_level()}")
        if self.get_inventory() == []:
            details.append(f"This hacker has no inventory!")
        else:
            details.append(f"Inventory Contents:")
            for item in self.get_inventory():
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)



