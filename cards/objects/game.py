"""Game instance."""
from typing import List

from cards.objects.dealer import Dealer
from cards.objects.player import Player


class GameSession:
    
    def __init__(
        self,
        dealer: Dealer,
        players: List[Player],
        active_player_index: int = 0,
        game_name: str = "Chicken",
    ):
        assert active_player_index < len(players)

        self.dealer: Dealer = dealer
        self.players: List[Player] = players
        self.active_player_index: int = active_player_index
        self.game_name: str = game_name

        self.n_players: int = len(players)

    def deal_cards(self, n_deals: int = 1):
        """Ask dealer to deal requested number of cards."""
        assert n_deals > 0

        for _ in range(n_deals):
            self.dealer.deal_one_card(active_player_index=self.active_player_index)

            # bump active player index
            self.active_player_index += 1
            if self.active_player_index == self.n_players:
                self.active_player_index = 0

    def deal_cards_discard_hand(self, n_deals: int = 1):
        assert n_deals > 0
        [x.hand.clear() for x in self.players]
        for _ in range(n_deals):
            self.dealer.deal_one_card(active_player_index=self.active_player_index)

            # bump active player index
            self.active_player_index += 1
            if self.active_player_index == self.n_players:
                self.active_player_index = 0

    