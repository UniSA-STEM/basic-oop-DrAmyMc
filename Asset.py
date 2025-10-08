"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    type_list = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']

    # TODO: Need to set up types and descriptions in a way that *actuallly* works
    def __init__(self, name):
        if name in Asset.type_list:
            self.__name = name
            self.__description = ''
            self.__is_encrypted = False
        else:
            self.__name = 'incorrect asset'

    def __str__(self):
        if self.__is_encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"



