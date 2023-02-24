"""Class responsible for card visuals."""
from typing import Tuple

import numpy as np
import cv2

from cards.objects.card_class import Card
from cards.assets.card_asset_loader import CardAsset

# constants
DEFAULT_CARD_TEXT_COLOR: Tuple[int, int, int, int] = (255, 255, 255, 255)
DEFAULT_CARD_TEXT_FONT: int = cv2.FONT_HERSHEY_SIMPLEX
DEFAULT_CARD_TEXT_LINE: int = cv2.LINE_AA
DEFAULT_CARD_FONT_THICKNESS: int = 1
DEFAULT_CARD_FONT_SCALE: int = 0.5
DEFAULT_CARD_TEXT_RELATIVE_Y_OFFSET: float = 0.14  # from top
DEFAULT_CARD_TEXT_RELATIVE_X_OFFSET: float = 0.06  # from left

PRIVATE_CARD_CODE: int = -2


class CardVisual:

    def __init__(
            self,
            card_width: int,
            card_height: int,
            background_color: Tuple[int, int, int, int],
            asset_name: str = None,
            use_card_ratio: bool = True,
        ):
        # card settings
        self.card_width: int = card_width
        self.card_height: int = card_height
        self.background_color: Tuple[int, int, int, int] = background_color
        
        # generated card settings
        self.card_background: np.ndarray = None
        self.card_text_loc: Tuple[int, int] = None

        # asset settings
        self.asset_name: str = asset_name
        self.card_asset: CardAsset = None
        self.use_card_ratio: bool = use_card_ratio

        self.__post_init__()
    

    def __post_init__(self):
        # update card asset if requested
        if self.asset_name is not None:
            self.card_asset = CardAsset(self.asset_name)
            # resize card asset to specified card size
            self.card_height = self.card_asset.resize_card_images(
                self.card_width, self.card_height, keep_ratio=self.use_card_ratio
            )

        # create generated card images
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
    
    def get_updated_card_height(self) -> int:
        return self.card_height
    
    def get_card_blank_image(self, card: Card) -> np.ndarray:
        assert self.card_background is not None
        return self.card_background

    def get_generated_card_image(self, card) -> np.ndarray:
        """
        Function to retrieve a generated card image.
        This is used as a placeholder when no asset is used.
        """
        assert self.card_background is not None

        if card.private:
            return self.card_background.copy()
        else:
            return cv2.putText(
                self.card_background.copy(),
                f"{card.suit_name} {card.number_name}",
                self.card_text_loc,
                DEFAULT_CARD_TEXT_FONT,
                DEFAULT_CARD_FONT_SCALE,
                DEFAULT_CARD_TEXT_COLOR,
                DEFAULT_CARD_FONT_THICKNESS,
                DEFAULT_CARD_TEXT_LINE
            )
        
    def get_asset_card_image(self, card) -> np.ndarray:
        card_code: int = card.card_code
        if card.private:
            card_code = PRIVATE_CARD_CODE
        return self.card_asset.get_card_image(card_code=card_code)

    def get_card_image(self, card: Card) -> np.ndarray:
        # use asset if available
        if self.asset_name is not None:
            return self.get_asset_card_image(card=card)
        else:
            return self.get_generated_card_image(card=card)
