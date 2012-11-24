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
outcome = ""
score = 0
popped = []

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
        # self.add_card = str(add_card)
        #self.player_hand = str(self.player_hand)
        s = ''
        for c in self.player_hand:
            s = s + str(c) + ' '
        return s

    def add_card(self, card):
        # draw = Deck.deal_card
        self.player_hand.append(card)
        return self.player_hand

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        for card in Hand:
            value += VALUES[i] 

    def busted(self):
        pass	# replace with your code
    
    def draw(self, canvas, p):
        pass	# replace with your code
        
# define deck class
class Deck:
    def __init__(self):
        # self.cards = [[suit,rank] for suit in SUITS for rank in RANKS]
        #cards = []
        popped = []
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        #self.cards = cards
        self.shuffle()
        #self.deal_card = deal_card
        
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
        self.cards.pop(0)
        popped = self.cards.pop(0)
        return popped
    
#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
#frame = simplegui.create_frame("Blackjack", 600, 600)
#frame.set_canvas_background("Green")

#create buttons and canvas callback
#frame.add_button("Deal", deal, 200)
#frame.add_button("Hit",  hit, 200)
#frame.add_button("Stand", stand, 200)
#frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
#frame.start()


# remember to review the gradic rubric
#hand = Hand()
#hand.add_card(Card('S', 'A'))
#print "The hand is", hand     # Calls hand's __str__ method
#card = Card('H', '2')
#hand.add_card(card)
#print "Now the hand is", hand
deck = Deck()
print "the deck's first card is", deck.deal_card()
card = deck.deal_card()  # Get a second card
print "the second card is", card
card = deck.deal_card()  # Get a third card
print "the third card is", card
print "Going to hit a hand twice."
hand = Hand()
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())
print "The result is:", hand
print deck