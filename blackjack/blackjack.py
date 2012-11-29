# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize global variables
in_play = False
message = ""
outcome = ""
score = 0
popped = []
player = []
dealer = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# Card class. Hand class calls this draw method for rendering card images onto canvas
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# Hand class used for adding card objects from Deck() and for getting the value of hands
class Hand:
    def __init__(self):
        self.player_hand = []

    def __str__(self):
        s = ''
        for c in self.player_hand:
            s = s + str(c) + ' '
        return s

    def add_card(self, card):
        self.player_hand.append(card)
        return self.player_hand

    def get_value(self):
        value = 0
        for card in self.player_hand:
            rank = card.get_rank()
            value = value + VALUES[rank]
        for card in self.player_hand:
            rank = card.get_rank()    
            if rank == 'A' and value <= 11:
                value += 10
        return value
    
    def draw(self, canvas, p):
        pos = p
        for card in self.player_hand:
            card.draw(canvas, p)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [115.5,229], CARD_BACK_SIZE)
        
# Deck class used for re-shuffling between hands and giving card objects to Hand as called
class Deck:
    def __init__(self):
        popped = []
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()
        
    def __str__(self):
        s = ''
        for c in self.cards:
            s = s + str(c) + ' '
        return s

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        popped = self.cards.pop(0)
        return popped
    
def deal():
    # deal function deals initial hands and adjusts message.
    global in_play, player, dealer, deck, message, score, outcome
    if in_play == True:
        # if player clicks Deal button during a hand, player loses hand in progress
        message = "Okay, here is a new hand"
        score -= 1
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    if in_play == False:
        # starts a new hand
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        message = "New Hand. Hit or Stand?"
    in_play = True
    outcome = ""

def hit():
    # deals player a new hand and ends hand if it causes a bust.
    global in_play, score, message
    if in_play == True:
        player.add_card(deck.deal_card())
        message = "Hit or Stand?"
        if player.get_value() > 21:
            in_play = False
            message = "Player has busted! Play again?"
            score -= 1
            outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())

def stand():
    # hits dealer until >=17 or busts. Determines winner of hand and adjusts score, game state, and messages
    global in_play, score, message, outcome
    if in_play == False:
        message = "That hand is already over. Deal again."
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            message = "Dealer busted. You win! Play again?"
            score += 1
            in_play = False
        elif dealer.get_value() >= player.get_value():
            message = "Dealer wins. Play again?"
            score -= 1
            in_play = False
        elif dealer.get_value() < player.get_value():
            message = "You win! Play again?"
            score += 1
            in_play = False
        outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())

# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", [40,80], 48, "White")
    canvas.draw_text("Score: " + str(score), [450,80], 36, "Black")
    canvas.draw_text("Dealer", [80,160], 30, "Black")
    canvas.draw_text("Player", [80,430], 30, "Black")
    canvas.draw_text(message, [200,355], 24, "Black")
    canvas.draw_text(outcome, [350,160], 24, "Black")
    player.draw(canvas, [80,450])
    dealer.draw(canvas, [80,180])

# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 600)
frame.set_canvas_background("Green")

# buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deals initial hand
deal()

# get things rolling
frame.start()