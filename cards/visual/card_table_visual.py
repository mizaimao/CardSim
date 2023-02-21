"""Definition of a card table."""
from typing import Tuple

import numpy as np


table_color: Tuple[int, int, int] = (0, 81, 44, 255)

class CardTableVisual:

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

        # images
        self.image: np.ndarray = None

        # python is not calling post_init itself??
        self.__post_init__()

        # debugging variables
        self.color_index: int = 0

    def __post_init__(self):
        self.image = self.generate_frame()

    def generate_frame(self) -> np.ndarray:            
        image: np.ndarray = np.full(
            (self.frame_height, self.frame_width, 4), table_color, dtype=np.uint8
        )
        return image
        
    def get_image(self):
        assert self.image is not None
        return self.image

