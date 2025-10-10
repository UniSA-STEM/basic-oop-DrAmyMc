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
    def __init__(self, name):
        self.__name = name
        self.__rig = None
        self.__inventory = [Asset('CryptoToken')]
        self.__trace_level = 0
        self.__is_exposed = False

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

    def set_name(self, name):
        self.__name = name

    def set_rig(self, rig):
        self.__rig = []
        self.__rig.append(rig)

    def set_trace_level(self, trace):
        if trace.isdigit() == True:
            self.__trace_level = trace

    def set_is_exposed(self, exposed):
        if exposed == True or exposed == False:
            self.__is_exposed = exposed

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
                print(f"Congratulations, {self.__name}! You have activated your rig.")

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

# TODO: Scanning methods aren't working because of retrieving name ARRRRRGHHHH
    def scan_inventory(self, asset):
        item_index = self.__inventory.index(asset)
        print(item_index)

    def scan_storage(self, asset):
        assets = self.__rig.get_storage()
        print(assets)
        item_index = assets.index(asset)
        print(item_index)

    def encrypt_asset(self, asset):
        pass

    def decrypt_asset(self, asset):
        pass

    def __str__(self):
        details = []
        details.append(f"Hacker's Name: {self.__name}")
        if self.__rig is None:
            details.append(f"This hacker has no rig!")
        else:
            details.append(f"Rig Name: {self.__rig}")
        if self.__inventory == []:
            details.append(f"This hacker has no inventory!")
        else:
            details.append(f"Trace Level: {self.__trace_level}\nInventory Contents:")
            for item in self.__inventory:
                details.append("    " + str(item))
        return '\n'.join(details)



