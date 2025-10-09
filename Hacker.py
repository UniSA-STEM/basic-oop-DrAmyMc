"""
File: Hacker.py
Description: Hacker class, representing a cyberpunk hacker, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset

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
        self.__rig = rig

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

    def __str__(self):
        details = []
        details.append(f"Hacker's Name: {self.__name}")
        if self.__rig is None:
            details.append(f"This hacker has no rig!")
        else:
            details.append(f"Rig Name: {self.__rig}")
        details.append(f"Trace Level: {self.__trace_level}\nInventory Contents:")
        for item in self.__inventory:
            details.append("    " + str(item))
        return '\n'.join(details)



