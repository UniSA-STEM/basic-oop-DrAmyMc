"""
File: Rig.py
Description: Rig class, representing a hacker's rig (computer), for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports random library and related Asset class
import random
from Asset import Asset

# Creation of Rig class
class Rig:
    # The rig is created with a name parameter, storage is initialised with starting assets, and all other attributes are set to initial defaults
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__storage = [Asset('Data Spike'), Asset('Data Spike'), Asset('Removable Drive')]
        self.__upgrade_level = 0

    # Getter functions for each attribute
    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def get_is_broken(self):
        return self.__is_broken

    def get_storage(self):
        return self.__storage

    def get_upgrade_level(self):
        return self.__upgrade_level

    # Setter functions for each appropriate attribute
    def set_name(self, name):
        self.__name = name

    def set_damage_counter(self, counter):
        # Ensures only valid numbers can be passed to damage counter attribute
        if counter >= 0 and counter <= 5:
            self.__damage_counter = counter

    def set_is_broken(self, broken):
        # Ensures only a True/False value can be passed to encryption status
        if broken == True or broken == False:
            self.__is_broken = broken

    def set_upgrade_level(self, level):
        # Ensures only valid numbers can be passed to upgrade level attribute
        if level >= 0 and level <=3:
            self.__upgrade_level = level

    # Properties for each attribute
    name = property(get_name, set_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    is_broken = property(get_is_broken, set_is_broken)
    storage = property(get_storage)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)

    # Scans storage to search for an asset by name
    def scan_storage(self, asset_name):
        item_index = None
        for item in self.get_storage():
            if item.get_name() == asset_name:
                item_index = self.get_storage().index(item)
        return item_index

    # Adds an asset to storage on rig
    def add_asset(self, asset):
        # Ensures only valid assets can be added to inventory
        if isinstance(asset, Asset) and asset.get_name() != 'Invalid':
            self.__storage.append(asset)

    # Removes an asset from storage on rig
    def remove_asset(self, asset_name):
        if self.scan_storage(asset_name) != None:
            del self.__storage[self.scan_storage(asset_name)]
        else:
            return None

    # Generates a random asset and adds it to storage
    def generate_asset(self):
        asset = Asset(random.choice(Asset.type_list))
        self.add_item(asset)

    # Repairs all damage to rig using a CryptoToken from storage
    def repair_rig(self):
        required = 'CryptoToken'
        if self.get_damage_counter() == 0 and self.get_is_broken() == False:
            print("No repair is needed.\n")
        elif self.scan_storage(required) == None :
            print(f"You cannot perform this repair - you need a {required} in your storage.\n")
        else:
            self.set_damage_counter(0)
            self.set_is_broken(False)
            self.remove_asset(required)
            print(f"Your rig has been repaired and restored to pristine condition.")

    # Upgrades rig using a Hardware Patch from storage
    def upgrade_rig(self):
        required = 'Hardware Patch'
        if self.get_upgrade_level() == 3:
            print("You cannot upgrade this rig - maximum upgrade level reached.\n")
        elif self.scan_storage(required) == None :
            print(f"You cannot perform this upgrade - you need a {required} in your storage.\n")
        else:
            self.set_upgrade_level((self.get_upgrade_level() + 1))
            self.remove_asset(required)
            print(f"Your rig has been upgraded to level {self.get_upgrade_level()}.\n")

    # Records hit damage from an attack from another hacker
    def take_hit(self):
        self.set_damage_counter((self.get_damage_counter() + 1))
        print(f"You have been hit! Your damage is now {self.get_damage_counter()}.\n")
        if self.get_damage_counter() >= 2:
            self.set_is_broken(True)
            print(f"Your rig is now broken :( Your assets are vulnerable!\n")

# TODO: Update all methods with different conditions based on game numbers - upgrade level, damage counter, storage size
    # Returns condition of rig based on damage and upgrade level
    def show_condition(self):
        if self.get_upgrade_level() >= 0:
            if self.get_damage_counter() == 0:
                return f"Pristine (Level {self.get_upgrade_level()})"
            elif self.get_damage_counter() == 1:
                return f"Partially damaged (Level {self.get_upgrade_level()})"
            else:
                return f"Broken (Level {self.get_upgrade_level()})"

    # Returns output for rig as per assignment specification
    def __str__(self):
        details = []
        details.append(f"Rig's Name: {self.get_name()}")
        details.append(self.show_condition())
        if self.get_storage() == []:
            details.append(f"This rig has no stored assets!")
        else:
            details.append(f"Storage Contents:")
            for item in self.get_storage():
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)