from Card import Deck
from Player import HumanPlayer, NPCPlayer

class Euchre:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [
            HumanPlayer("You"), 
            NPCPlayer("NPC1"), 
            NPCPlayer("NPC2"), 
            NPCPlayer("NPC3")
        ]

        self.trump_suit = None
        self.dealer_index = 0


    def deal_cards(self):
        self.deck.shuffle()
        for player in self.players:
            player.recieve_cards(self.deck.deal(5))
        self.kitty = self.deck.deal(4)
        self.upcard = self.kitty.pop()

        print(f"Upcard: {self.upcard}")

    def bidding_phase(self):
        # Frist round of bidding
        for i in range(1, 5):
            player = self.players[(self.dealer_index + i) % 4]
            if player.pick_it_up(self.upcard):
                self.trump_suit = player.upcard.suit
                self.dealer().recieve_cards(self.upcard)
                self.dealer().discard_card()
                return

        # Second round of bidding: choose trump suit
        for i in range(1,5):
            player = self.players[(self.dealer_index + i) % 4]
            chosen_suit = player.choose_trump(self.upcard.suit)
            if chosen_suit:
                self.trump_suit = chosen_suit
                return

        # If all pass, redeal
        print("Redealing...")

        self.deal_cards()
        self.bidding_phase()


    def dealer(self):
        return self.players[self.dealer_index]

    def next_dealer(self):
        self.dealer_index = (self.dealer_index + 1) % 4

    def play_game(self):
        while not self.is_game_over():
            self.deal_cards()
            self.bidding_phase()

            # add trick implementing phase

            self.next_dealer()

    def is_game_over(self):
        # if any player has 10 points, the game is over
        pass