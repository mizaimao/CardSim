"""Player calss."""

from typing import List

from cards.objects.card_class import Card

class Player:

    def __init__(
            self,
            disabled: bool = False
        ):
        self.hand: List[Card] = []
        self.disabled: bool = disabled
