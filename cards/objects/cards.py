"""Definition of card objects."""

from typing import Tuple

import numpy as np
import cv2


# constants
DEFAULT_WINDOW_WIDTH: int = 800
DEFAULT_CARD_WIDTH_RATIO: float = 0.2  # ratio to widow width
DEFAULT_CARD_RALETIVE_HEIGHT: float = 1.61  # ratio to card width

DEFAULT_CARD_TEXT_COLOR: Tuple[int, int, int] = (0, 0, 0)
DEFAULT_CARD_TEXT_FONT: int = cv2.FONT_HERSHEY_SIMPLEX
DEFAULT_CARD_TEXT_LINE: int = cv2.LINE_AA
DEFAULT_CARD_FONT_THICKNESS: int = 2
DEFAULT_CARD_FONT_SCALE: int = 20
DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET: float = 0.2  # from top
DEFAULT_CARD_TEXT_RELATIVE_X_OFFSET: float = 0.1  # from left

card_width: int = int(DEFAULT_WINDOW_WIDTH * DEFAULT_CARD_WIDTH_RATIO)
card_height: int = int(card_width * DEFAULT_CARD_RALETIVE_HEIGHT)
card_text_loc: Tuple[int, int] = (
    int(card_height * DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET), int(card_width * DEFAULT_CARD_TEXT_RELATIVE_X_OFFSET)
)

def create_card_blank(
        card_width: int, card_height: int, background_color: Tuple[int, int, int, int]
    ) -> np.ndarray:

    return np.full(
        (card_height, card_width, 4), background_color
    )
card_background: np.ndarray = create_card_blank()

class Card:
    
    def __init__(self, suit: int, number: int):
        """
        Args
            suit: Suit of card. Using the following codes:
                0: jokers, numebr 0 is black-white, and 1 is colored
                1. spades
                2. hearts
                3. diamons
                4. clubs
        """
        # sainty checks
        assert isinstance(number, int)
        if suit == 0:
            assert number in (0, 1), f"Joker can only have number code 0 or 1, got {number}."
        elif suit < 5:
            assert 0 < number < 14, f"Number can be range from 1 to 13, inclusively; got {number}."
        else:
            raise ValueError(f"Unknown suit code {suit}")
        
        self.suit: int = suit
        self.number: int = number

    def get_card_image(self, card_width: int, card_height: int) -> np.ndarray:

        assert card_background is not None
        card_image: np.ndarray = cv2.putText(
            card_background.copy()
            f"{self.suit}\n{self.number}"
            card_text_loc,
            DEFAULT_CARD_TEXT_FONT,
            DEFAULT_CARD_FONT_SCALE,
            DEFAULT_CARD_TEXT_COLOR,
            DEFAULT_CARD_FONT_THICKNESS,
            DEFAULT_CARD_TEXT_LINE
        )

        return card_image
