"""Asset loader for cards."""
from pathlib import Path
from typing import Dict, Union
import json
import os

from PIL import Image
import numpy as np


cwd: Path = Path(os.path.dirname(__file__))
config_name: str = "config.json"

class CardAsset:

    def __init__(self, asset_name: str = "card_set_0"):

        self.name: str = asset_name
        self.asset_root: Path = cwd.joinpath(asset_name)

        cfg_path: Path = self.asset_root.joinpath(config_name)
        self.cfg: Dict[str, str] = json.load(open(cfg_path))

        self.pillow_images: Dict[str, Image.Image] = {}
        self.images: Dict[str, np.ndarray] = {}  # will be populated in "resize_card_images()"
        self.__post_init__()

    def __post_init__(self):
        """Load images files into memory."""
        print(f"Loading image assests {self.name} ...")
        for image_id, image_file_name in self.cfg.items():
            image_full_path = self.asset_root.joinpath(image_file_name)
            self.pillow_images[int(image_id)] = Image.open(image_full_path)

    def resize_card_images(
            self,
            target_width: int,
            target_height: int,
            keep_ratio: bool
        ) -> int:
        """Resize all images."""
        # current sizes
        width, height = self.pillow_images[0].size  # Pillow image returns width and hight, not HW
        # calculate new height if necessary
        if keep_ratio:
            target_height = int(target_width * height / width)
        for image_id, image_array in self.pillow_images.items():
            self.images[image_id] = np.array(
                image_array.resize((target_width, target_height))
            )

        return target_height

    def get_card_image(self, card_code: Union[int, str]):
        assert self.images, "Populate card images with resize_card_images() first."
        return self.images[int(card_code)]

if __name__ == "__main__":

    a = CardAsset()
