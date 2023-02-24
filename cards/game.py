"""Main game entry-point."""
from typing import List

import numpy as np
import cv2

from cards.visual.visual_manger import VisualManager
from cards.objects.player import Player
from cards.objects.dealer import Dealer
from cards.objects.game import GameSession


FRAME_WIDTH: int = 1280
FRAME_HEIGHT: int = 800
WINDOW_NAME: str = "Chicken"
N_PLAYERS: int = 1
SEED: int = 720



def game():
    """Entry-point."""
    # rng
    rng: np.random.RandomState() = np.random.RandomState(SEED)

    # add players
    players: List[Player] = [
        Player(disabled=False) for _ in range(N_PLAYERS)
    ]

    # create a card dealer
    dealer: Dealer = Dealer(
        sets=1,
        include_jokers=False,
        players=players,
        rng=rng,
    )

    # create a game
    game_session: GameSession = GameSession(
        dealer=dealer,
        players=players,
        active_player_index=0,
        game_name="Chicken Game",
    )

    vman: VisualManager = VisualManager(
        frame_width=FRAME_WIDTH,
        frame_height=FRAME_HEIGHT,
        game_session=game_session,  # add a session pointer to vis
        color_format="BGR",
    )


    key: int = ord('n')
    
    while key == ord('n'):

        game_session.deal_cards_discard_hand(3)
        image: np.ndarray = vman.get_frame()


        cv2.imshow(WINDOW_NAME, image)

        key = cv2.waitKey(0)
                
    cv2.destroyAllWindows()


if __name__ == "__main__":
    """Main function."""
    game()