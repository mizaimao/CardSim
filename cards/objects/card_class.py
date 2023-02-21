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
    
    def __init__(self, suit: int, number: int, set_number: int = 0):
        """
        Args
            suit: Suit of card. Using the following codes:
                0. spades
                1. hearts
                2. diamons
                3. clubs
                4: jokers, numebr 0 is black-white, and 1 is colored
        """
        # sainty checks
        assert isinstance(number, int)
        if suit == 4:
            assert number in (0, 1), f"Joker can only have number code 0 or 1, got {number}."
        elif 0 <= suit < 4:
            assert 0 <= number <= 12, f"Number can be range from 0 to 12, inclusively; got {number}."
        else:
            raise ValueError(f"Unknown suit code {suit}")
        
        self.suit: int = suit
        self.number: int = number
        self.set_number: int = set_number
        self.card_name: str = None
        self.__post_init__()


    def __post_init__(self):
        self.card_name = self._generate_card_name()


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

    def get_card_image(self, card_width: int, card_height: int) -> np.ndarray:

        assert card_background is not None
        card_image: np.ndarray = cv2.putText(
            card_background.copy(),
            f"{self.suit}\n{self.number}",
            card_text_loc,
            DEFAULT_CARD_TEXT_FONT,
            DEFAULT_CARD_FONT_SCALE,
            DEFAULT_CARD_TEXT_COLOR,
            DEFAULT_CARD_FONT_THICKNESS,
            DEFAULT_CARD_TEXT_LINE
        )

        return card_image
    
