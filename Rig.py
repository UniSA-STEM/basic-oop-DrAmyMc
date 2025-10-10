"""
File: Rig.py
Description: Rig class, representing a hacker's rig (computer), for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__upgrade_level = 0
        self.__storage = [Asset('Data Spike'), Asset('Data Spike'), Asset('Removable Drive')]

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def get_is_broken(self):
        return self.__is_broken

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_storage(self):
        return self.__storage

    def set_name(self, name):
        self.__name = name

    def set_damage_counter(self, counter):
        if counter.isdigit() == True:
            self.__damage_counter = counter

    def set_is_broken(self, broken):
        if broken == True or broken == False:
            self.__is_broken = broken

    def set_upgrade_level(self, level):
        if level.isdigit() == True:
            self.__upgrade_level = level

    def add_item(self, item):
        self.__storage.append(item)

    def remove_item(self, item):
        if item in self.__storage:
            self.__storage.remove(item)

    def generate_asset(self):
        pass

# TODO: Need to scan inventory for item to start with, need to fix inventory scanning before anything else as all dependent on this
    def repair_rig(self):
        if self.__damage_counter > 0:
            self.__damage_counter = 0
            self.is_broken = False
            self.remove_item('CryptoToken')
        else:
            print("No repair is needed.")

    name = property(get_name, set_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    is_broken = property(get_is_broken, set_is_broken)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)
    storage = property(get_storage)


    def __str__(self):
        details = []
        details.append(f"Rig's Name: {self.__name}")
        #TODO: details.append(method for rig condition here)
        details.append(f"Upgrade Level: {self.__upgrade_level}\nStorage Contents:")
        for item in self.__storage:
            details.append("    " + str(item))
        return '\n'.join(details)



