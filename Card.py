# Class for cards
class Card:
    RANKS = ["2", "3", "4", "5" , "6",  "7" , "8" , "9",  "10",  "J",  "Q" , "K", "A"]
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

    def __init__(self, suit: str, rank: str):
        if suit not in Card.SUITS:
            raise ValueError(f"{suit} not valid in {Card.SUITS}")
        if rank not in Card.RANKS:
            raise ValueError(f"{rank} not valid in {Card.RANKS}")


        # Storing them as Attributes
        self._suit = suit # Use underscore to indicate internal use (immutable)
        self._rank = rank

    # Read_Only Access
    @property
    def suit(self):
        return self._suit
    
    @property
    def card(self):
        return self._rank
        
    # String representation for debugging
    def __str__(self):
        return f"{self._rank}{self._suit}"
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self._rank == other._rank and self._suit == other._suit
    
    # Class for Deck of Cards
import random

class Deck:
    # Initializes a deck of 52 Cards
    def __init__(self):
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, num_cards: int):
        if num_cards > len(self._cards):
            raise ValueError(f"Cannot deal {num_cards} cards. Only {len(self._cards)} ramaining cards.")
        return [self._cards.pop() for _ in range(num_cards)]
    
    def __len__(self):
        return len(self._cards)
    
# Create a deck
deck = Deck()
deck.shuffle()

# Deal some cards
hand = deck.deal(5)
print("Your hand:", hand)

# Check deck size
print("Cards remaining in deck:", len(deck))

