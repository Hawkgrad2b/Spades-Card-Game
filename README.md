# Spades-Card-Game
Creating a functional Spades game, influenced from class project (making helper functions in Haskell)

# Spades Game - Functional & Class Outline

## 1. Card & Deck Management

### Class `Card`
- `__init__(self, suit: str, rank: str)`: Initializes a card with a suit and rank.
- `__str__(self)`: Returns a string representation of the card.
- `__eq__(self, other)`: Compares two cards (useful for validation).

### Class `Deck`
- `__init__(self)`: Initializes a full deck of 52 cards.
- `shuffle(self)`: Shuffles the deck.
- `deal(self, num_cards: int) -> List[Card]`: Deals a specified number of cards.

---

## 2. Players and Hands

### Class `Player` (Abstract)
- `__init__(self, name: str)`: Initializes a player with a name and empty hand.
- `receive

