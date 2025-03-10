# Abstract Player class
from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.bid = None

    def recieve_cards(self, cards: list):
        # Add cards to players hand
        self.hand.extend(cards)

    @abstractmethod
    def play_card(self, bid: int):
        # subclasses must define how a card is played
        pass

    def set_bid(self, bid: int):
        # set the players bid 
        if bid < 0:
            raise ValueError("Bid must be a positive integer.")
        self.bid = bid

    def get_bid(self) -> int:
        # get the players bid
        return self.bid
    
    def __str__(self):
        return f"Player {self.name} - Hand: {self.hand}"
    
    def pick_it_up(self, upcard):
        # check if player wants to order up the upcard
        pass

    def choose_trump(self, excluded_suits):
        # choose the trump suit
        pass
    
    def recieve_card(self, card):
        # add a card to the players hand
        self.hand.append(card)
    
    def discard_card(self):
        # discard a card from the players hand
        pass
        
    
class HumanPlayer(Player):
    def play_card(self, valid_cards: list):
        # prompting the player to choose a card
        print(f"\n{self.name}, your hand: {', '.join(map(str, self.hand))}")
        print(f"Valid plays: {', '.join(map(str, valid_cards))}")

        while True:
            chosen_card = input("Choose a card to play: ")

            for card in self.hand:
                if str(card) == chosen_card and card in valid_cards:
                    self.hand.remove(card)
                    return card

            print("Invalid card. Try again.")


class NPCPlayer(Player):
    def play_card(self, valid_cards: list):
        # NPC chooses a card to play
        card = random.choice(valid_cards)
        self.hand.remove(card)
        print(f"{self.name} played: {card}")
        return card
    
