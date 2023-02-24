"""Player calss."""

from typing import List

from cards.objects.card_class import Card

class Player:

    def __init__(
            self,
            name: str = "Chicken Player",
            max_n_cards: int = 3,
            disabled: bool = False
        ):
        self.name: str = name
        self.hand: List[Card] = []
        self.max_n_cards: int = max_n_cards
        self.disabled: bool = disabled
