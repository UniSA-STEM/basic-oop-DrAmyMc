"""
File: Asset.py
Description: Asset class, representing digital assets used by hackers and rigs, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Creation of Asset class
class Asset:
    # The type_list defines the five possible asset names and the description_list provides the five matching descriptions for each asset type
    type_list = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']
    description_list = ['Use to acquire or repair rigs.', 'Used in battles', 'Found in rigs and used for extraction.', 'Used to encrypt or decrypt assets.', 'Used to upgrade rigs.']

    # The asset is created with a name parameter, which is matched to the type_list to initialise the correct matching description
    def __init__(self, name):
        self.__name = name
        self.__description = Asset.description_list[Asset.type_list.index(name)]
        self.__is_encrypted = False

    # Getter functions for each attribute
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_is_encrypted(self):
        return self.__is_encrypted

    # Setter functions for each attribute
    def set_name(self, name):
        self.__name = name

    def set_description(self, desc):
        self.__description = desc

    def set_is_encrypted(self, encrypted):
        # Ensures only a True/False value can be passed to encryption status
        if encrypted == True or encrypted == False:
            self.__is_encrypted = encrypted

    # Properties for each attribute
    name = property(get_name, set_name)
    description = property(get_description, set_description)
    is_encrypted = property(get_is_encrypted, set_is_encrypted)

    # Returns output for asset as per assignment specification
    def __str__(self):
        if self.__is_encrypted:
            return f"{self.get_name()}: {self.get_description()} [Encrypted]"
        else:
            return f"{self.get_name()}: {self.get_description()}"
