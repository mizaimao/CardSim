"""Class responsible for card visuals."""
from typing import Tuple

import numpy as np
import cv2

from cards.objects.card_class import Card

# constants
DEFAULT_CARD_TEXT_COLOR: Tuple[int, int, int, int] = (255, 255, 255, 255)
DEFAULT_CARD_TEXT_FONT: int = cv2.FONT_HERSHEY_SIMPLEX
DEFAULT_CARD_TEXT_LINE: int = cv2.LINE_AA
DEFAULT_CARD_FONT_THICKNESS: int = 1
DEFAULT_CARD_FONT_SCALE: int = 0.5
DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET: float = 0.14  # from top
DEFAULT_CARD_TEXT_RELATIVE_X_OFFSET: float = 0.06  # from left


class CardVisual:

    def __init__(
            self,
            card_width: int,
            card_height: int,
            background_color: Tuple[int, int, int, int]
        ):
        self.card_width: int = card_width
        self.card_height: int = card_height
        self.background_color: Tuple[int, int, int, int] = background_color

        self.card_background: np.ndarray = None
        self.card_text_loc: Tuple[int, int] = None
        
        self.__post_init__()
    

    def __post_init__(self):
        self.card_background = self.create_card_blank()

        self.card_text_loc = (
            #int(self.card_height * DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET),
            int(self.card_width * DEFAULT_CARD_TEXT_RELATIVE_X_OFFSET),
            int(self.card_height * DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET),
        )
    
    def create_card_blank(self) -> np.ndarray:
        return np.full(
            (self.card_height, self.card_width, 4), self.background_color, dtype=np.uint8
        )
    
    def get_card_blank_image(self, card: Card) -> np.ndarray:
        assert self.card_background is not None

        

        return self.card_background

    def get_card_image(self, card: Card) -> np.ndarray:
        assert self.card_background is not None

        card_image: np.ndarray = cv2.putText(
            self.card_background.copy(),
            f"{card.suit_name} {card.number_name}",
            self.card_text_loc,
            DEFAULT_CARD_TEXT_FONT,
            DEFAULT_CARD_FONT_SCALE,
            DEFAULT_CARD_TEXT_COLOR,
            DEFAULT_CARD_FONT_THICKNESS,
            DEFAULT_CARD_TEXT_LINE
        )

        return card_image