"""
File: Asset.py
Description: Asset class, representing digital assets used by hackers and rigs, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    type_list = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']
    description_list = ['Use to acquire or repair rigs.', 'Used in battles', 'Found in rigs and used for extraction.', 'Used to encrypt or decrypt assets.', 'Used to upgrade rigs.']

    # TODO: WORKS for correct names!!! Need a way to handle incorrect names that doesn't generate a shitty system error
    def __init__(self, name):
            self.__name = name
            self.__description = Asset.description_list[Asset.type_list.index(name)]
            self.__is_encrypted = False

    def __str__(self):
        if self.__is_encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"

# TODO: This kinda thing works to catch error, but then messages with str recall. Come back to handling exceptions later.
#try:
#    if name not in Asset.type_list:
#        raise ValueError(
#            'Incorrect asset type - must be CryptoToken, Data Spike, Removable Drive, Security Chip, or Hardware Patch.')
#        except ValueError as error:
#            print(f"{error}")

