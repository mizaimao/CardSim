"""Top-level class handling visual elements."""

import cv2
import numpy as np

from cards.visual.card_table import CardTable
from cards.objects.card_class import Card

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

        # table
        self.table: CardTable = CardTable(
            frame_width=frame_width, frame_height=frame_height
        )

    def get_card_image(self):
        return
        
    def get_table_image(self):
        table_image: np.ndarray = self.table.get_image()

        if self.color_format == "BGR":
            return table_image[..., 2::-1]
        elif self.color_format == "RGB":
            return table_image
        else:
            raise ValueError()
            
