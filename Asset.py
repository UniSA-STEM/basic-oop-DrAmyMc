"""
File: Asset.py
Description: Asset class, representing digital assets used by hackers and rigs, for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    """
    Represents a digital asset that may be used by a hacker or rig (computer).

    Assets have a specific type (e.g. 'CryptoToken', 'Data Spike').
    Each type of asset is associated with a predefined description.
    Assets can be encrypted or unencrypted (the default).
    """

    # List of the five valid asset types
    type_list = ['CryptoToken', 'Data Spike', 'Removable Drive', 'Security Chip', 'Hardware Patch']

    # Corresponding descriptions for each asset type
    description_list = ['Use to acquire or repair rigs.', 'Used in battles.', 'Used for extraction.',
                        'Used to encrypt or decrypt assets.', 'Used to upgrade rigs.']

    def __new__(cls, name):
        """
        Creates a new Asset instance only if the provided name is valid.
        This method is called before the __init__ method to prevent creation of invalid asset types
        by checking against values in 'type_list'.

        Args:
            name (str): The name (type) of the asset to create.

        Returns:
            Asset | None: Asset object if name is a valid asset type, otherwise None.
        """
        if name in cls.type_list:
            return super().__new__(cls)
        else:
            print(
                f"Error - {name} is not a valid asset type (CryptoToken, Data Spike, Removable Drive, Security Chip, "
                f"or Hardware Patch).")
            return None
        # Code inspired by:
        # Zuo Lin, L., 2025. __new__ vs __init__ Methods in Python. [online] Built-In.
        # Available at: <https://builtin.com/data-science/new-python> [Accessed 18 October 2025].

    def __init__(self, name):
        """
        Initialises a new Asset instance.

        Args:
            name (str): The name (tyoe) of the asset, which must exist in 'type_list'.

        Attributes:
            __name (str): The asset's name (type).
            __description (str): The description automatically matched from 'description_list' based on
                                the asset's name.
            __is_encrypted (bool): Indicates whether the asset is encrypted, initially False.
        """
        self.__name = name
        # Correct description initialised from 'description_list' based on asset name
        self.__description = Asset.description_list[Asset.type_list.index(name)]
        self.__is_encrypted = False

    # --------------
    # Getter methods
    # --------------

    def get_name(self):
        """Returns the asset's name."""
        return self.__name

    def get_description(self):
        """Returns the asset's description."""
        return self.__description

    def get_is_encrypted(self):
        """Returns whether the asset is currently encrypted (True/False)."""
        return self.__is_encrypted

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Updates the asset's name and automatically sets the matching description.

        Args:
            name (str): The new asset name. Must be a valid type from 'type_list'.
        """
        if name in Asset.type_list:
            self.__name = name
            self.__description = Asset.description_list[Asset.type_list.index(name)]

    def set_is_encrypted(self, encrypted):
        """
        Sets the encryption status of the asset.

        Args:
            encrypted (bool): The new encryption status. Must be True or False.
        """
        if isinstance(encrypted, bool):
            self.__is_encrypted = encrypted

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    description = property(get_description)
    is_encrypted = property(get_is_encrypted, set_is_encrypted)

    # -------------------
    # Behavioural methods
    # -------------------

    def __str__(self):
        """
        Returns a formatted string representation of the asset.

        Returns:
            str: The asset's name and description.
                 Includes '[Encrypted]' if the asset is encrypted.
        """
        if self.is_encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"
