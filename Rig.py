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

    def __str__(self):
        details = []
        details.append(f"Rig's Name: {self.__name}")
        #TODO: details.append(method for rig condition here)
        details.append(f"Upgrade Level: {self.__upgrade_level}\nStorage Contents:")
        for item in self.__storage:
            details.append("    " + str(item))
        return '\n'.join(details)



