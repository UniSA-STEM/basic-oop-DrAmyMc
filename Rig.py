"""
File: Rig.py
Description: Rig class, representing a hacker's rig (computer), for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.

Game parameters:
Upgrade levels: 0 (start)   1       2       3 (max)
Damage taken:   1 (start)   0.75    0.5     0.25
Storage size:   4 (start)   6       8       10
"""

# Imports random library and related Asset class
import random
from Asset import Asset

# Creation of Rig class
class Rig:
    """ Documentation for Rig class"""
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
        # Ensures name is stored as a string
        self.__name = str(name)

    def set_damage_counter(self, counter):
        # Ensures only valid numbers can be passed to damage counter attribute
        if counter >= 0 and counter <= 2:
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
        for item in self.storage:
            if item.name == asset_name:
                item_index = self.storage.index(item)
        return item_index

    # Adds an asset to storage on rig
    def add_asset(self, asset):
        # Sets maximum storage size variables based on upgrade level
        if self.upgrade_level == 0:
            max_storage = 4
        elif self.upgrade_level == 1:
            max_storage = 6
        elif self.upgrade_level == 2:
            max_storage = 8
        else:
            max_storage = 10
        # Ensures only valid assets can be added to storage and that storage space is available:
        if isinstance(asset, Asset) and asset.name != 'Invalid' and len(self.storage) < max_storage:
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
        self.add_asset(asset)

    # TODO THIS NEEDS BE HACKER INITIATED FROM INVENORY Repairs all damage to rig using a CryptoToken from storage
    def repair_rig(self):
        required = 'CryptoToken'
        if self.damage_counter == 0 and self.is_broken == False:
            print("No repair is needed.\n")
        elif self.scan_storage(required) == None :
            print(f"You cannot perform this repair - you need a {required} in your storage.\n")
        else:
            self.damage_counter = 0
            self.is_broken = False
            self.remove_asset(required)
            print(f"Your rig has been repaired and restored to pristine condition.")

    # TODO SAME THING THIS NEEDS TO BE HACKER LED Upgrades rig using a Hardware Patch from storage
    def upgrade_rig(self):
        required = 'Hardware Patch'
        if self.upgrade_level == 3:
            print("You cannot upgrade this rig - maximum upgrade level reached.\n")
        elif self.scan_storage(required) == None :
            print(f"You cannot perform this upgrade - you need a {required} in your storage.\n")
        else:
            self.upgrade_level += 1
            self.remove_asset(required)
            print(f"Your rig has been upgraded to level {self.upgrade_level}.\n")

    # Records hit damage from an attack from another hacker
    def take_hit(self):
        # Sets damage amount from hit based on upgrade level
        if self.upgrade_level == 0:
            hit_damage = 1
        elif self.upgrade_level == 1:
            hit_damage = 0.75
        elif self.upgrade_level == 2:
            hit_damage = 0.5
        else:
            hit_damage = 0.25
        self.damage_counter += hit_damage
        print(f"You have been hit! Your damage is now {self.damage_counter}.\n")
        # Sets broken status if damage counter reaches 2
        if self.damage_counter >= 2:
            self.is_broken = True
            print(f"Your rig is now broken :( Your assets are vulnerable!\n")

    # Returns condition of rig based on damage count
    def show_condition(self):
        if self.damage_counter == 0:
            return f"Pristine condition - damage count {self.damage_counter} out of 2"
        elif self.damage_counter < 1:
            return f"Partially damaged - damage count {self.damage_counter} out of 2"
        elif self.damage_counter < 2:
            return f"Heavily damaged - damage count {self.damage_counter} out of 2"
        else:
            return f"Broken - maximum damage! This rig's assets are exposed."

    # Returns output for rig as per assignment specification
    def __str__(self):
        details = []
        details.append(f"Rig's Name: {self.name}")
        details.append(self.show_condition())
        details.append(f"Upgrade Level: {self.upgrade_level}")
        if self.storage == []:
            details.append(f"This rig has no stored assets!")
        else:
            details.append(f"Storage Contents:")
            for item in self.storage:
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)