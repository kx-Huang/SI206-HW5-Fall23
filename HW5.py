# Name:
# Student ID:
# Email:
# List who you have worked with on this homework:
# List any AI tool (e.g. ChatGPT, GitHub Copilot):

import re
import os
import unittest


def get_player_info(file_name: str) -> list:
    """
    This function reads the file and returns a list of strings. Each string should contain all the information of one player.

    Args:
        file_name (str): file name of data

    Returns:
        player_info (list): a list of strings with each player’s information
    """
    # TODO: implement this function
    pass


def create_bio_dict(player_info: list) -> dict:
    """
    This function gets a list of strings with each player’s information and returns a dictionary with player’s full names (including any suffixes such as Jr) as keys and their birth year, month and date as values in tuples.

    Args:
        player_info (list): a list of strings with each player’s information

    Returns:
        bio_dict (dict): a dictionary with player’s full names with suffixes as keys and their birth year, month and date as values in tuples
    """
    # TODO: implement this function
    pass


def create_short_bio(player_info: list) -> list:
    """
    This function gets a list of strings with each player’s information and returns a list of short bios (the first sentence of each player’s information).

    Args:
        player_info (list): a list of strings with each player’s information

    Returns:
        short_bio (str): a list of short bios (the first sentence of each player’s information, which starts with a capital letter and ends with a period)
    """
    # TODO: implement this function
    pass


def get_valid_year(player_info: list) -> list:
    """
    This function finds all valid years (1980~2023 inclusive) and returns a list of lists containing valid years for each player. Note that "2,000" and "2020s" are not valid years.

    Args:
        player_info (list): a list of strings with each player’s information

    Returns:
        valid_year (list): a list of lists containing valid years for each player.
    """
    # TODO: implement this function
    pass


################## EXTRA CREDIT ##################
def get_abbr_dict(player_info: list) -> dict:
    """
    This function finds all abbreviations and returns a dictionary with abbreviations as keys and full names as values.
        - Abbreviations are made of consecutive uppercase letters inside a set of parentheses.
        - Full names are consecutive words starting with an uppercase letter.

    Args:
        player_info (list): a list of strings with each player’s information

    Returns:
        abbr_dict (list): a dictionary with abbreviations as keys and full names as values
    """
    # TODO: implement this function
    pass


class TestAllFunc(unittest.TestCase):
    def setUp(self):
        # TODO: fill in the blank
        self.player_info = ...
        self.bio_dict = ...
        self.short_bio = ...
        self.valid_year = ...
        self.abbr_dict = ...

    def test_get_player_info(self):
        # TODO: implement this test case
        pass

    def test_create_bio_dict(self):
        # TODO: implement this test case
        pass

    def test_create_short_bio(self):
        # TODO: implement this test case
        pass

    def test_get_valid_year(self):
        # TODO: implement this test case
        pass

    ############ EXTRA CREDIT ############
    def test_get_abbr_dict(self):
        # TODO: implement this test case
        pass


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
