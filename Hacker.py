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



