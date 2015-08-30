# miniproject "Blackjack", by: Luqi

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "New Game"
score = 0

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
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for i in range(len(self.cards)):
            ans += str(self.cards[i])
        return "Hand Contains: " + ans + ""

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        value = 0
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        aces = False
        for i in range(len(self.cards)):
            value += VALUES[self.cards[i].rank]           
            if self.cards[i].rank == 'A':
                aces = True
        if aces == True:
            if value <= 11:
                value += 10
                aces = False
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.cards[i].rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.cards[i].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + 100 * i + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.list = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.list.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.list)

    def deal_card(self):
        # deal a card object from the deck
        c = self.list[-1]
        self.list.remove(c)
        return c
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        for i in range(len(self.list)):
            ans += str(self.list[i])
        return "Deck Contains: " + ans + ""



#define event handlers for buttons
def deal():
    global outcome, score, player_hand, dealer_hand, card_deck, in_play
    outcome = 'New Game'
    card_deck = Deck()
    card_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(card_deck.deal_card())
    player_hand.add_card(card_deck.deal_card())
    dealer_hand.add_card(card_deck.deal_card())
    dealer_hand.add_card(card_deck.deal_card())
    in_play = True

def hit():
    global outcome, score, player_hand, card_deck, in_play
    # if the hand is in play, hit the player
    if in_play == True:
        player_hand.add_card(card_deck.deal_card())
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "Busted, You lose!"
            score -= 1
        else:
            in_play = True
       
def stand():
    global outcome, score, player_hand, dealer_hand, card_deck, in_play
    if in_play == True:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(card_deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer Busted! You Win!"
            score += 1
        else:
            if dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer Win!"
                score -= 1
            else:
                outcome = "You Win!"
                score += 1      
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

# draw handler    
def draw(canvas):
    global player_hand, dealer_hand, card_deck, outcome, score, in_play
    canvas.draw_text('Blackjack', (20, 70), 50, 'Black')
    canvas.draw_text('Score = ' + str(score), (380, 70), 30, 'Black')
    canvas.draw_text(str(outcome), (250, 120), 30, 'Orange')
    if in_play == False:
        canvas.draw_text("New Deal?", (200, 400), 30, 'Black')
        canvas.draw_text("Your value = " + str(player_hand.get_value()), (250, 170), 30, 'Orange')
        canvas.draw_text("Dealer's value = " + str(dealer_hand.get_value()), (250, 200), 30, 'Orange')
    else:
        canvas.draw_text("Hit or Stand?", (200, 400), 30, 'Black')    
    canvas.draw_text('Dealer', (50, 200), 40, 'Black')
    dealer_hand.draw(canvas, [50, 220])
    canvas.draw_text('Player', (50, 400), 40, 'Black')
    player_hand.draw(canvas, [50, 420])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 220 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        




# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)



# get things rolling
deal()
frame.start()
