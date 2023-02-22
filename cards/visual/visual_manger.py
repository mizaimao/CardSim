"""Top-level class handling visual elements."""
from typing import Tuple, List

import cv2
import numpy as np

from cards.visual.card_table_visual import CardTableVisual
from cards.visual.card_visual import CardVisual
from cards.objects.card_class import Card
from cards.objects.game import GameSession


DEFAULT_CARD_WIDTH_RATIO: float = 0.1  # ratio to window width
DEFAULT_CARD_RALETIVE_HEIGHT: float = 1.61  # ratio to card width
DEFAULT_CARD_BACKGROUND_COLOR: Tuple[int, int, int, int] = (224, 167, 93, 255)

BOTTOM_CARD_OFFSET_FROM_EDGE_RATIO: float = 0.05  # raito to window height, from bottom
BOTTOM_CARD_DISPLAY_RANGE_WIDTH_RATIO: float = 0.6  # ratio to window width

class VisualManager:
    
    def __init__(
        self,
        frame_width: int,
        frame_height: int,
        game_session: GameSession,
        color_format: str = "BGR"
    ):
        # basic properties
        self.frame_width: int = frame_width
        self.frame_height: int = frame_height
        self.color_format: str = color_format
        
        # game session pointer
        self.game_session: GameSession = game_session

        # table visual
        self.tablev: CardTableVisual = CardTableVisual(
            frame_width=frame_width, frame_height=frame_height
        )

        # card visual
        self.card_width: int = int(frame_width * DEFAULT_CARD_WIDTH_RATIO)
        self.card_height: int = int(self.card_width * DEFAULT_CARD_RALETIVE_HEIGHT)
        self.cardv: CardVisual = CardVisual(
            card_width=self.card_width,
            card_height=self.card_height,
            background_color=DEFAULT_CARD_BACKGROUND_COLOR,
        )

    def get_card_image(self):
        card_image: np.ndarray = self.cardv.get_card_blank_image()
        return card_image
        
    def get_table_image(self):
        table_image: np.ndarray = self.tablev.get_image()
        return table_image


    def _output_frame(self, frame) -> np.ndarray:
        """Wrapper that handls RGB or BGR."""
        if self.color_format == "BGR":
            return frame[..., 2::-1]
        elif self.color_format == "RGB":
            return frame
        else:
            raise ValueError()

    def get_frame(self):
        
        # we use frame as background, and add cards and other elements to it
        frame: np.ndarray = self.get_table_image()
        # from top to down (y), from left to right (x)
        #frame[100: 150, 200: 250] = (0, 0, 0, 255)

        # get cards
        card_image: np.ndarray = self.get_card_image()
        n_cards: int = 3
        card_displayable_window_width: int = int(self.frame_width * BOTTOM_CARD_DISPLAY_RANGE_WIDTH_RATIO)
        # left blank before card displaying region
        x_offset: int = int((self.frame_width - card_displayable_window_width) // 2)

        # get card arrangements for bottom cards
        x_coors, y_coors = self.arrange_cards(
            total_width=card_displayable_window_width,
            total_height=self.frame_height,
            card_width=self.card_width,
            card_height=self.card_height,
            n_cards=n_cards,
        )
        x_coors = [] + x_coors

        for _x_start, y_start in zip(x_coors, y_coors):
            x_start = _x_start + x_offset
            x_end = x_start + self.card_width
            y_end = y_start + self.card_height

            frame[y_start: y_end, x_start: x_end] = card_image

        return self._output_frame(frame)
        
    @staticmethod
    def arrange_cards(
        total_width: int,
        total_height: int,
        card_width: int,
        card_height: int,
        n_cards: int,
    ) -> Tuple[List[int], List[int]]:
        """
        Returns
            List[int]: Staring x coor (from left to right) for each card.
            List[int]: Staring y coor (from top to down) for each card.
        """
        # sanity check
        assert n_cards > 0
        y_coor: int = int(
            total_height * (1 - BOTTOM_CARD_OFFSET_FROM_EDGE_RATIO) - card_height
        )

        x_coors: List[int] = []
        y_coors: List[int] = [y_coor for _ in range(n_cards)]


        sum_card_width: int = card_width * n_cards
        
        # put all cards on the table and they can be arranged with spaces between them
        if sum_card_width >= total_width:
            spacer: int = int(
                (total_width - sum_card_width) // (n_cards + 1)
            )
            for i in range(n_cards):
                x_coors.append(
                    spacer + (spacer + card_width) * i  # i starts from 0
                )

        # cards have to be squeezed into the defined total_width
        else:
            space_for_each_card: int = int(total_width / n_cards)
            for i in range(n_cards):
                x_coors.append(
                    0 + space_for_each_card * i
                )

        assert len(x_coors) == len(y_coors) == n_cards

        return x_coors, y_coors
