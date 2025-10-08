"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__upgrade_level = 0
        self.__storage = []

    def __str__(self):
        details = []
        details.append(f"Rig's Name: {self.__name}")
        #TODO: details.append(method for rig condition here)
        details.append(f"Upgrade Level: {self.__upgrade_level}\nStorage Contents:")
        for item in self.__storage:
            details.append(str(item))
        return '\n'.join(details)

# TODO: Needs 2x Data Spikes and 1x Removable Drive


