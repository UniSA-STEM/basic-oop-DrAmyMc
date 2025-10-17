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
    """This is the documentation for the asset class"""
    # The type_list defines the five possible asset names
    type_list = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']
    # The description_list provides the five matching descriptions for each asset type
    description_list = ['Use to acquire or repair rigs.', 'Used in battles.', 'Found in rigs and used for extraction.', 'Used to encrypt or decrypt assets.', 'Used to upgrade rigs.']

    # The asset is initialised with a name parameter
    def __init__(self, name):
        # If the name is found in the type_list, the asset initialises with the correct matching description
        if name in Asset.type_list:
            self.__name = name
            self.__description = Asset.description_list[Asset.type_list.index(name)]
            self.__is_encrypted = False
        # If the name is not in the type_list, the asset is initialised as 'Invalid'
        else:
            self.__name = 'Invalid'
            self.__description = 'Please remove'
            self.__is_encrypted = False

    # Getter functions for each attribute
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_is_encrypted(self):
        return self.__is_encrypted

    # Setter function for name attribute, which also automatically sets matching description via lookup
    def set_name(self, name):
        # Ensures asset is of a correct type by checking name argument against list of asset types
        if name in Asset.type_list:
            self.__name = name
            self.__description = Asset.description_list[Asset.type_list.index(name)]

    # Setter function for is_encrypted attribute
    def set_is_encrypted(self, encrypted):
        # Ensures only a True/False value can be passed to encryption status
        if encrypted == True or encrypted == False:
            self.__is_encrypted = encrypted

    # Properties for each attribute
    name = property(get_name, set_name)
    description = property(get_description)
    is_encrypted = property(get_is_encrypted, set_is_encrypted)

    # Returns output for asset as per assignment specification
    def __str__(self):
        # Adds the string '[Encrypted]' if asset is encrypted
        if self.is_encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        # Omits the string '[Encrypted]' if asset is not encrypted
        else:
            return f"{self.name}: {self.description}"
