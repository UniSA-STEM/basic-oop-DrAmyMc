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

    def acquire_rig(self, name):
        for item in self.__inventory:
            if item.name == 'CryptoToken':
                self.__rig = Rig(name)
                self.__inventory.remove(item)
                print(f"Congratulations, {self.__name}! You have activated your rig.\n")

    # TODO: Actual launching of spike needs to be written in, and consumption of spike from inventory
    def launch_spike(self):
        if self.__is_exposed == False:
            for item in self.__rig.get_storage():
                # TODO: need to rewrite this so ONE data spike is found and used, this is matching each item and hence NOT WORKING
                if item.name == 'Data Spike':
                    print('match!')
                    self.__rig.remove_item(item)
                    self.__trace_level += 1
                    if self.__trace_level == 5:
                        set.is_exposed(True)
                else:
                    print("You do not have a data spike in your rig's storage to launch.")
        else:
            print("You cannot launch a data spike while exposed. Reduce your exposure level.")

    def scan_inventory(self, asset):
        item_index = None
        for item in self.get_inventory():
            if item.get_name() == asset:
                item_index = self.__inventory.index(item)
        return item_index

    def scan_storage(self, asset):
        return self.get_rig().scan_storage(asset)

    def encrypt_asset(self, asset):
        pass

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



