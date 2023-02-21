"""Definition of a card table."""
from typing import Tuple

import numpy as np


test_colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
table_color: Tuple[int, int, int] = (0, 81, 44, 255)

class CardTable:

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

        # debugging variables
        self.color_index: int = 0

    def __post_init__(self):
        self.image = self.generate_frame()

    def generate_frame(self) -> np.ndarray:

        if self.color_index == len(test_colors):
            self.color_index = 0
            
        image: np.ndarray = np.full(
            (self.frame_height, self.frame_width, 4), test_colors[self.color_index], dtype=np.uint8
        )
        self.color_index += 1

        return image
        
    def get_image(self):
        assert self.image is not None
        if self.color_format == "BGR":
            return self.image[..., 2::-1]
        elif self.color_format == "RGB":
            return self.image
        else:
            raise ValueError()
        
    def iter_image(self):
        """Debugging function."""
        self.image = self.generate_frame()
        
        if self.color_format == "BGR":
            return self.image[..., 2::-1]
        elif self.color_format == "RGB":
            return self.image
        else:
            raise ValueError()
