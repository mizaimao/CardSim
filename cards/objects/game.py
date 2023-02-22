"""Game instance."""
from typing import List

from cards.objects.dealer import Dealer
from cards.objects.player import Player


class GameSession:
    
    def __init__(
        self,
        dealer: Dealer,
        players: List[Player],
        active_player: int = 0,
        game_name: str = "Chicken",
    ):
        self.dealer: Dealer = dealer
        self.players: List[Player] = players
        self.active_player: int = active_player
        self.game_name: str = game_name

    