"""Dealer class."""
from typing import List
import numpy as np

from cards.objects.card_class import Card
from cards.objects.player import Player

class Dealer:

    def __init__(
            self,
            sets: int = 1,
            reserved: int = 0,
            include_jokers: bool = True,
            players: List[Player] = None,
            rng: np.random.RandomState = None,
        ):
        # sainity checks
        assert sets > 0
        self.max_cards: int = (52 + include_jokers * 2) * sets
        assert self.max_cards >= 52
        assert reserved < self.max_cards
        
        self.sets: int = sets
        self.reserved: int = reserved
        self.include_jokers: bool = include_jokers
        self.players: List[Player] = players
        self.n_players: int = len(self.players)
        
        if isinstance(rng, int):  # seed
            self.rng: np.random.RandomState = np.random.RandomState(rng)
        elif isinstance(rng, np.random.RandomState):
            self.rng = rng
        elif rng is None:
            self.rng = np.random.RandomState()
        else:
            raise ValueError(
                f"Argument \"rng\" should be either int or np.random.RandomState, got {type(rng)}."
            )
        self.deck: List[Card] = []
        self.__post_init__()

    def __post_init__(self):
        """Post init."""
        self.fill_deck()

    def fill_deck(self):
        """Fill the current deck with number of set of cards."""
        assert len(self.deck) == 0
        for _ in range(self.sets):
            self._fill_deck_one_set()

    def _fill_deck_one_set(self):
        """Fill the current deck with one set of cards."""
        cards: np.ndarray = np.arange(
            54 if self.include_jokers else 52, dtype=np.uint8
        )
        self.rng.shuffle(cards)
        self.deck.extend(
            [Card(card_code=x, private=False) for x in cards]
        )

    def draw_one(self):
        if len(self.deck) == 0:
            raise ValueError("Empty deck.")
        return self.deck.pop()  # the last element
    
    def draw_by_index(self, index: int):
        raise NotImplementedError()
    
    def deal_one_card(self, active_player_index: int):
        """Pop one card to current active player and update active player index."""
        active_player: Player = self.players[active_player_index]

        # check if the player can receive more cards
        if active_player.max_n_cards == len(active_player.hand):
            raise ValueError(
                f"Player has got too many cards in hand, current limit is {active_player.max_n_cards}."
            )

        # give the player a card
        active_player.hand.append(self.deck.pop())




if __name__ == "__main__":
    # test module
    dealer: Dealer = Dealer()
    print(dealer.deck[0].card_full_name)
