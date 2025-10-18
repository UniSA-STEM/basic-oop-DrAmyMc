"""
File: Rig.py
Description: Rig class, representing a hacker's rig (computer), for 'Into the Grid' game.
Author: Amellia (Amy) McCormack
ID: 110392134
Username: MCCAY044
This is my own work as defined by the University's Academic Misconduct Policy.

Game parameters:
Upgrade levels: 0 (start)   1       2       3 (max)
Damage taken:   1 (start)   0.75    0.5     0.25
Storage size:   4 (start)   6       8       10
"""

import random
from Asset import Asset


class Rig:
    """
    Represents a hacker's rig (computer) within the game.

    Each rig has a name, upgrade level, and storage that can hold various Asset objects.
    Rigs can take damage, be upgraded, and may eventually become broken if their damage counter exceeds a threshold,
    which leaves their stored assets vulnerable to theft.
    """

    def __init__(self, name):
        """
        Initialises a new Rig instance.

        The rig starts with a default set of assets in storage, zero damage,
        an upgrade level of 0, and an unbroken state.

        Args:
             name (str): The name of the rig.
        """
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__storage = [Asset('Data Spike'), Asset('Data Spike'), Asset('Removable Drive')]
        self.__upgrade_level = 0

    # --------------
    # Getter methods
    # --------------

    def get_name(self):
        """Returns the name of the rig."""
        return self.__name

    def get_damage_counter(self):
        """Returns the current damage counter value."""
        return self.__damage_counter

    def get_is_broken(self):
        """Returns whether the rig is broken."""
        return self.__is_broken

    def get_storage(self):
        """Returns a list of Asset objects currently in storage."""
        return self.__storage

    def get_upgrade_level(self):
        """Returns the current upgrade level."""
        return self.__upgrade_level

    # --------------
    # Setter methods
    # --------------

    def set_name(self, name):
        """
        Updates the rig's name.

        Args:
            name (str): The new name for the rig.
        """
        self.__name = str(name)

    def set_damage_counter(self, counter):
        """
        Updates the damage counter, ensuring it remains within a valid range.

        Args:
            counter (float | int): The new damage value (0-2).
        """
        if isinstance(counter, (int, float)) and 0 <= counter <= 2:
            self.__damage_counter = counter

    def set_is_broken(self, broken):
        """
        Sets whether the rig is broken.

        Args:
            broken (bool): True if the rig is broken, False otherwise.
        """
        if isinstance(broken, bool):
            self.__is_broken = broken

    def set_upgrade_level(self, level):
        """
        Sets the rig's upgrade level.

        Args:
            level (int): The upgrade level (0-3).
        """
        if isinstance(level, int) and 0 <= level <= 3:
            self.__upgrade_level = level

    # --------------------
    # Property definitions
    # --------------------

    name = property(get_name, set_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    is_broken = property(get_is_broken, set_is_broken)
    storage = property(get_storage)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)

    # -------------------
    # Behavioural methods
    # -------------------

    def scan_storage(self, asset_name):
        """
        Searches the rig's storage for an asset by name.

        Args:
            asset_name (str): The name of the asset to search for.

        Returns:
            int | None: The index of the asset if found, otherwise None.
        """
        item_index = None
        for item in self.storage:
            if item.name == asset_name:
                item_index = self.storage.index(item)
        return item_index

    def add_asset(self, asset):
        """
        Adds an asset to the rig's storage if space is available.
        The maximum storage capacity depends on the rig's upgrade level.

        Args:
            asset (Asset): The asset to be added.
        """
        max_storage = [4, 6, 8, 10][self.upgrade_level]
        if isinstance(asset, Asset):
            if len(self.storage) < max_storage:
                self.__storage.append(asset)
            else:
                print(f"You cannot add another asset as you do not have enough storage available.")

    def remove_asset(self, asset_name):
        """
        Removes an asset from storage by name, if it exists.

        Args:
            asset_name (str): The name of the asset to remove.
        """
        index = self.scan_storage(asset_name)
        if index is not None:
            del self.__storage[index]

    def generate_asset(self):
        """Generates a random asset and adds it to storage."""
        asset = Asset(random.choice(Asset.type_list))
        self.add_asset(asset)

    def take_hit(self):
        """
        Records damage taken from an attack.

        Damage increases the rig's 'damage_counter' based on its upgrade level.
        Once the damage counter reaches or exceeds 2, the rig becomes broken.
        """
        hit_damage = [1, 0.75, 0.5, 0.25][self.upgrade_level]
        self.damage_counter += hit_damage
        print(f"{self.name}, you have been hit! Your damage is now {self.damage_counter}.")

        if self.damage_counter >= 2:
            self.is_broken = True
            print(f"{self.name} is now broken :( The stored assets are vulnerable!")

    def show_condition(self):
        """
        Returns a text description of the rig's current condition.

        Returns:
            str: The condition summary (e.g. "Pristine", "Partially Damaged").
        """
        if self.damage_counter == 0:
            condition = "Pristine"
        elif self.damage_counter < 1:
            condition = "Partially Damaged"
        elif self.damage_counter < 2:
            condition = "Heavily Damaged"
        else:
            condition = "Broken"
        return f"{condition} (Level {self.upgrade_level})"

    def __str__(self):
        """
        Returns a formatted string containing the rig's details.

        Returns:
            str: The name, condition, upgrade level, and storage contents.
        """
        details = [f"\nRig's Name: {self.name}", self.show_condition(),
                   f"Damage Counter: {self.damage_counter} out of 2"]
        if self.storage == []:
            details.append(f"This rig has no stored assets!")
        else:
            details.append(f"Storage Contents:")
            for item in self.storage:
                details.append("    " + str(item))
        details.append("")
        return '\n'.join(details)
