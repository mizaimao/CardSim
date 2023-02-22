"""Dealer class."""
from typing import List
import numpy as np

from cards.objects.card_class import Card

class Dealer:

    def __init__(
            self,
            sets: int = 1,
            reserved: int = 0,
            include_jokers: bool = True,
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
            54 if self.include_jokers else 52
        )
        self.rng.shuffle(cards)
        self.deck.extend(
            [self._create_card(card_code=x) for x in cards]
        )

    def _create_card(self, card_code: int) -> Card:
        """
        Convert a card code into a card object.
        
        0 - 12: spades (0)
        13 - 25: hearts (1)
        26 - 38: diamons (2)
        39 - 51: clubs (3)
        52 - 53: jokers (4)
        """
        suit: int = int(card_code // 13)
        number: int = int(card_code % 13)
        card: Card = Card(suit=suit, number=number)
        return card

    def draw_one(self):
        if len(self.deck) == 0:
            raise ValueError("Empty deck.")
        return self.deck.pop()  # the last element
    
    def draw_by_index(self, index: int):
        raise NotImplementedError()

if __name__ == "__main__":
    # test module
    dealer: Dealer = Dealer()
    print(dealer.deck[0].card_full_name)
