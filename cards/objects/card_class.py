"""Definition of card objects."""

from typing import Dict

import numpy as np


# card mapping
suit_mapping: Dict[int, str] = {
    0: "Spade ",
    1: "Heart ",
    2: "Diamon",
    3: "Club  ",
    4: "Joker ",
}
number_mapping: Dict[int, int] = {
    0: "A ",  # Ace
    1: "2 ",
    2: "3 ",
    3: "4 ",
    4: "5 ",
    5: "6 ",
    6: "7 ",
    7: "8 ",
    8: "9 ",
    9: "10",
    10: "J ",  # Jack
    11: "Q ",  # Queen
    12: "K ",  # King
}


class Card:
    
    def __init__(self, card_code: int, set_number: int = 0):
        """
        Args
            suit: Suit of card. Using the following codes:
                0. spades
                1. hearts
                2. diamons
                3. clubs
                4: jokers, numebr 0 is black-white, and 1 is colored
        """
        self.suit: int
        self.number: int
        self.card_code: int = card_code
        self.set_number: int = set_number
        self.card_full_name: str = None
        self.suit_name: str = None
        self.number_name: str = None
        self.__post_init__()

    def __post_init__(self):
        """
        Convert a card code into a essential card info.
        0 - 12: spades (0)
        13 - 25: hearts (1)
        26 - 38: diamons (2)
        39 - 51: clubs (3)
        52 - 53: jokers (4)
        """
        suit: int = int(self.card_code // 13)
        number: int = int(self.card_code % 13)

        # sainty checks
        if suit == 4:
            assert number in (0, 1), f"Joker can only have number code 0 or 1, got {number}."
        elif 0 <= suit < 4:
            assert 0 <= number <= 12, f"Number can be range from 0 to 12, inclusively; got {number}."
        else:
            raise ValueError(f"Unknown suit code {suit}")
        # update card info
        self.suit = suit
        self.number = number
        # update card name
        self.suit_name = suit_mapping[self.suit]
        self.number_name = number_mapping[self.number]
        self.card_full_name = "{} {}".format(
            self.suit_name, self.number_name
        )

    def _generate_card_name(self) -> str:
        """Generate a string of card name for display."""

        return "{} {}".format(
            suit_mapping[self.suit], number_mapping[self.number]
        )

    def get_name(self, show_set_number: bool = False) -> str:
        name_str: str = self.card_name
        if show_set_number:
            name_str += f" from Set {self.set_number}"
        return name_str
