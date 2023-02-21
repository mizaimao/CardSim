"""Top-level class handling visual elements."""
from typing import Tuple

import cv2
import numpy as np

from cards.visual.card_table_visual import CardTableVisual
from cards.visual.card_visual import CardVisual
from cards.objects.card_class import Card


DEFAULT_CARD_WIDTH_RATIO: float = 0.2  # ratio to widow width
DEFAULT_CARD_RALETIVE_HEIGHT: float = 1.61  # ratio to card width
DEFAULT_CARD_BACKGROUND_COLOR: Tuple[int, int, int, int] = (255, 255, 255, 255)

class VisualManager:
    
    def __init__(
        self,
        frame_width: int,
        frame_height: int,
        color_format: str = "BGR"
    ):
        # basic properties
        self.frame_width: int = frame_width
        self.frame_height: int = frame_height
        self.color_format: str = color_format

        # table visual
        self.tablev: CardTableVisual = CardTableVisual(
            frame_width=frame_width, frame_height=frame_height
        )

        # card visual
        card_width: int = int(frame_width * DEFAULT_CARD_WIDTH_RATIO)
        card_height: int = int(card_width * DEFAULT_CARD_RALETIVE_HEIGHT)
        self.cardv: CardVisual = CardVisual(
            card_width=card_width,
            card_height=card_height,
            background_color=DEFAULT_CARD_BACKGROUND_COLOR,
        )

    def get_card_image(self):
        return
        
    def get_table_image(self):
        table_image: np.ndarray = self.tablev.get_image()

        if self.color_format == "BGR":
            return table_image[..., 2::-1]
        elif self.color_format == "RGB":
            return table_image
        else:
            raise ValueError()
            
