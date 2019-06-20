""" File: Poker.py

    Description:

    Student's Name: Robert Stephany

    Student's UT EID: rrs2558

    Course Name: CS 313E

    Unique Number: 85575

    Date Created: 06/20/2019

    Date Last Modified: 06/20/2019 """

import random

# Card class.
class Card (object):
    ############################################################################
    # Class Variables.
    # Note: Jack = 11, Queen = 12, King = 13, Ace = 14.

    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14);
    SUITS = ('C', 'D', 'H', 'S');

    ############################################################################
    # Constructor.
    # Note: default card is Queen of Spades
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank;
        else:
            self.rank = 12;

        if (suit in Card.SUITS):
            self.suit = suit;
        else:
            self.suit = 'S';

    ############################################################################
    # Special methods

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A';
        elif (self.rank == 13):
            rank = 'K';
        elif (self.rank == 12):
            rank = 'Q';
        elif (self.rank == 11):
            rank = 'J';
        else:
            rank = str (self.rank)
        return rank + self.suit;

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank;

    def __ne__ (self, other):
        return self.rank != other.rank;

    def __lt__ (self, other):
        return self.rank < other.rank;

    def __le__ (self, other):
        return self.rank <= other.rank;

    def __gt__ (self, other):
        return self.rank > other.rank;

    def __ge__ (self, other):
        return self.rank >= other.rank;



# Deck class.
class Deck (object):
    ############################################################################
    # Constructor
    def __init__ (self, num_decks = 1):
        self.deck = [];

        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit);
                    self.deck.append(card);

    ############################################################################
    # Methods

    # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None;
        else:
            return self.deck.pop(0);



class Poker (object):
    ############################################################################
    # constructor
    def __init__ (self, num_players = 2):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = 5;

        # deal the cards to the players
        for i in range (num_players):
            hand = [];
            for j in range (self.numCards_in_Hand):
                hand.append (self.deck.deal());
                self.all_hands.append (hand);

    ############################################################################
    # Play

    # simulate the play of poker
    def play (self):
        # sort the hands of each player and print
        for i in range (len(self.all_hands)):
            sorted_hand = sorted (self.all_hands[i], reverse = True);
            self.all_hands[i] = sorted_hand;
            hand_str = '';
            for card in sorted_hand:
                hand_str = hand_str + str (card) + ' ';
                print ('Player ' + str(i + 1) + ' : ' + hand_str);

        # determine the type of each hand and print
        hand_type = []; 	# create a list to store type of hand
        hand_points = [];	# create a list to store points for hand


        # determine winner and print

    ############################################################################
    # Hand analysis methods.
    # Each of these functions take one argument, a hand. This is a list of 5
    # cards (the player). Each one returns a boolean (True or False).
    # Note: All of these methods that hand is sorted.

    # determine if a hand is a royal flush
    def is_royal_flush(self, hand):
        # First, check that the hand is both a flush and a straight.
        if(self.is_straight_flush(hand) == False):
            return False;

        # If we've made it here, then we at least know that hand is a straight
        # flush. For a straight flush to be a royal flush, the high card
        # must be an Ace (rank 14)
        if(hand[0].rank == 14):
            return True;
        else:
            return False;

    # determine if a hand is a straight flush
    def is_straight_flush(self, hand):
        # if hand is a straight flush, then it is both a straight and a flush.
        # since we already have code to check both of these things, we can just
        # call the appropiate methods rather than rewriting code.
        return ((self.is_straight(hand)) and (self.is_flush(hand)));

    # determine if a hand has four of the same kind.
    def is_four_of_a_kind(self, hand):
        for i in range(len(hand)-3):
            if(hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank) and (hand[i+2].rank == hand[i+3].rank):
                return True;

        # If we've made it here, then hand does not have 4 of a kind
        return False;

    # determine if a hand is a full house
    def is_full_house(self, hand):
        # if hand has a full house then it must have a pair and 3 of a kind.
        # these two sets of cards must be disjoint, however.
        i = 0;
        three_of_a_kind = False;
        pair = False;
        while i < (len(hand) - 1):
            # First, check for 3 of a kind.
            if(i < (len(hand) - 2) and (hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank)):
                three_of_a_kind = True;
                # Now, skip ahead of the 3 of a kind.
                i += 3;

            # Now check for a pair.
            elif(hand[i].rank == hand[i+1].rank):
                pair = True;

                # now, skip ahead of the pair.
                i += 2;

            else:
                i +=1;

        if(three_of_a_kind and pair):
            return True;
        else:
            return False;

    # determine if a hand is flush
    def is_flush(self, hand):
        # First, check that the hand is a flush. This happens when all 5 cards
        # have the same suit. Or, equivalently, when each of the first 4 cards
        # have the same suit as the next one.
        for i in range (len(hand) - 1):
            if(hand[i].suit != hand[i+1].suit):
                return False;

        # If we've made it here then the hand is a flush.
        return True;

    # determine if a hand is a straight
    def is_straight(self, hand):
        # First, check if the hand is a flush. This happens when the 5 cards
        # are in a row. Or, equivalently, when the rank of the ith card is
        # one more than the rank of the i+1th card (for i = 0,1,2,3)
        for i in range(len(hand)-1):
            if((hand[i].rank - 1) != hand[i+1].rank):
                return False;

        # If we've made it to here then the hand is a straight.
        return True;

    # determine if a hand has (at least) 3 of a kind
    def is_three_of_a_kind(self, hand):
        # since the cards are sorted, 3 of a kind occurs if there are three
        # adjacent cards with the same rank.
        for i in range(len(hand) - 2):
            if ((hand[i].rank == hand[i+1].rank) and (hand[i+1].rank == hand[i+2].rank)):
                return True;

        # If we've gotten to here then the hand does not have 3 of a kind
        return False;

    # determine if a hand has 2 pair.
    def is_two_pair(self, hand):
        # since the cards are sorted, two pairs occurs when there are two
        # disjoint locations in the hand where adjacent cards have the same
        # rank.
        num_pairs = 0;
        i = 0;
        while i < (len(hand)-1):
            if(hand[i].rank == hand[i+1].rank):
                num_pairs += 1;

                # since we know that the ith and i+1th cards are a pair, we need
                # to skip forward two cards (to see if any other pairs exist)
                i += 2;
            else:
                i +=1;

        if(num_pairs == 2):
            return True;
        else:
            return False;

    # determine if a hand has (at least) one pair
    def is_one_pair(self, hand):
        # since the cards are sorted, a pair occurs when two adjacnet cards have
        # the same rank
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                return True;

        # If we've made it to here then there are no pairs in this hand.
        return False;

    ############################################################################
    # Calculate points (using the formula provided by the professor)
    def calculate_points(h, c1, c2, c3, c4, c5):
        return h*(15**5) + c1*(15**4) + c2*(15**4) + c3*(15**2) + c4*(15) + c5;



def get_num_players():
    # This function gets the number of players from the user using an exception
    # save setup. Invalid input is handled using exception
    num_players = 0;
    while((num_players < 2) or (num_players > 6)):
        try:
            num_players = int(input('Enter number of players: '));
        except:
            print("Invalid input. Number of players must be between 2 and 6 (inclusive). Try again.");

    return num_players;



def main():
    # prompt the user to enter the number of plaers
    num_players = get_num_players();

    # create the Poker object
    game = Poker (num_players);

    # play the game
    game.play();

if(__name__ == "__main__"):
    main();
