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

# initialize some useful global variables
in_play = False
message = ""
score = 0
popped = []
player = []
dealer = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

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
        
# define hand class
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
                print str(value)
        print str(value)
        return value

    def busted(self):
        pass	# replace with your code
    
    def draw(self, canvas, p):
        pos = p
        for card in self.player_hand:
#            if card == dealer.draw:
#                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            card.draw(canvas, p)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [115.5,229], CARD_BACK_SIZE)
        
# define deck class
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
        self.cards = str(cards)
        self.deal_card = str(popped)
        str(self.deal_card)

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cards)
        # print str(self.cards)

    def deal_card(self):
        popped = self.cards.pop(0)
        return popped
    
#define event handlers for buttons
def deal():
    global in_play, player, dealer, deck, message
    if in_play == False:
        deck = Deck()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        print "Player's Hand: " + str(player)
        print "Dealer's Hand: " + str(dealer)
        print player.get_value()
        print dealer.get_value()
        message = "New Hand. Hit or Stand?"
    in_play = True

def hit():
    global in_play, score, message
    if in_play == True:
        player.add_card(deck.deal_card())
        print "Player's Hand: " + str(player)
        message = "Hit or Stand?"
        if player.get_value() > 21:
            in_play = False
            message = "Player has busted! Dealer wins."
            print message
            score -= 1
       
def stand():
    global in_play, score, message
    if in_play == False:
        message = "That hand is already over. Deal again."
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            # message = "Dealer has " + str(dealer.get_value())
            print message
        print "Dealer has " + str(dealer.get_value())
        if dealer.get_value() > 21:
            message = "Dealer busted. You win!"
            score += 1
            in_play = False
            print message + str(score)
        elif dealer.get_value() >= player.get_value():
            message = "Dealer wins."
            score -= 1
            in_play = False
            print message + str(score)
        elif dealer.get_value() < player.get_value():
            message = "You win!"
            score += 1
            in_play = False
            print message + str(score)

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [40,80], 48, "White")
    canvas.draw_text("Score: " + str(score), [450,80], 36, "Black")
    canvas.draw_text("Dealer", [80,160], 30, "Black")
    canvas.draw_text("Player", [80,430], 30, "Black")
    canvas.draw_text(message, [200,355], 24, "Black")
    player.draw(canvas, [80,450])
    dealer.draw(canvas, [80,180])

# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()

# remember to review the gradic rubric
#hand = Hand()
#hand.add_card(Card('S', 'A'))
#print "The hand is", hand     # Calls hand's __str__ method
#card = Card('H', '2')
#hand.add_card(card)
#print "Now the hand is", hand
#deck = Deck()
#print "the deck's first card is", deck.deal_card()
#card = deck.deal_card()  # Get a second card
#print "the second card is", card
#card = deck.deal_card()  # Get a third card
#print "the third card is", card
#print "Going to hit a hand twice."
#hand = Hand()
#hand.add_card(deck.deal_card())
#hand.add_card(deck.deal_card())
#print "The result is:", hand