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
    # Class Variables (these just enumerate the different possible outcomes)
    ROYAL_FLUSH = 10;
    STRAIGHT_FLUSH = 9;
    FOUR_OF_A_KIND = 8;
    FULL_HOUSE = 7;
    FLUSH = 6;
    STRAIGHT = 5;
    THREE_OF_A_KIND = 4;
    TWO_PAIR = 3;
    ONE_PAIR = 2;
    HIGH_CARD = 1;

    ############################################################################
    # constructor
    def __init__ (self, num_players = 2):
        self.deck = Deck();
        self.deck.shuffle();
        self.num_players = num_players;
        self.num_cards_in_hand = 5;

        # deal the cards to the players (round robin)
        hands = [ [] for i in range(num_players)];
        for k in range(self.num_cards_in_hand):
            for i in range(num_players):
                hands[i].append(self.deck.deal());

        self.all_hands = hands;

    ############################################################################
    # Play

    # simulate the play of poker
    def play (self):
        # First, sort and print each player's hand.
        for i in range (len(self.all_hands)):
            # Sort the hand
            sorted_hand = sorted (self.all_hands[i], reverse = True);
            self.all_hands[i] = sorted_hand;

            # Now print it out.
            hand_str = '';
            for card in sorted_hand:
                hand_str += str(card) + ' ';
            print ('Player %d :' % (i+1), hand_str);

        # determine the type and points of each hand. Print out the type
        hand_type = []; 	# create a list to store type of hand
        hand_points = [];	# create a list to store points for hand

        for player in range(self.num_players):
            hand = self.all_hands[player];

            # identify the hand
            type_ID, type_str = self._identify_hand(hand);
            hand_type.append(type_ID);

            # print out what they got
            print("Player %d: %s" % (player+1, type_str));

            # Now, determine the number of points.
            points = self._calculate_hand_points(type_ID, hand)
            hand_points.append(points);
        # determine winner and print

    ############################################################################
    # Hand analysis methods.
    # Each of these functions take one argument, a hand. This is a list of 5
    # cards (the player). Each one returns a boolean (True or False).
    # Note: All of these methods that hand is sorted.

    # determine what hand player i has.
    # accepts in a hand, returns an ID and a string. ID is the ID for the hand
    # type (For example, straights have an ID of 5, see class varaiables above)
    # the string is for printing purposes. It holds the name of the hand type.
    def _identify_hand(self, hand):
        if(self.is_royal_flush(hand)):
            return Poker.ROYAL_FLUSH, "Royal Flush";
        elif(self.is_straight_flush(hand)):
            return Poker.STRAIGHT_FLUSH, "Straight Flush";
        elif(self.is_four_of_a_kind(hand)):
            return Poker.FOUR_OF_A_KIND, "Four of a Kind";
        elif(self.is_full_house(hand)):
            return Poker.FULL_HOUSE, "Full House";
        elif(self.is_flush(hand)):
            return Poker.FLUSH, "Flush";
        elif(self.is_straight(hand)):
            return Poker.STRAIGHT, "Straight";
        elif(self.is_three_of_a_kind(hand)):
            return Poker.THREE_OF_A_KIND, "Three of a Kind";
        elif(self.is_two_pair(hand)):
            return Poker.TWO_PAIR, "Two Pair";
        elif(self.is_one_pair(hand)):
            return Poker.ONE_PAIR, "One Pair";
        else:
            return Poker.HIGH_CARD, "High Card";

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
                i += 1;

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
    # Calculate points

    """This method finds the points of a given hand using the formula provided in
    the problem statement.
    Note: This method assumes that each hand has exactly 5 cards and is sorted.

    The first argument, type_ID, is the hand type ID
        The Type ID's are enumerated as class variables for the Poker class.
        These can be found at the top of the Poker class. For example, if the
        hand is a straight flush then type_ID = 9)
    Note: the user must have identified the hand type before calling this method

    The second argument, hand, is simply the hand that we're finding the points
    of."""
    def _calculate_hand_points(self, type_ID, hand):
        # First, check if the hand type requires special modification to the
        # points formula.
        if(type_ID == Poker.FOUR_OF_A_KIND):
            return self._four_of_a_kind_points(hand);
        elif(type_ID == Poker.FULL_HOUSE):
            return self._full_house_points(hand);
        elif(type_ID == Poker.THREE_OF_A_KIND):
            return self._three_of_a_kind_points(hand);
        elif(type_ID == Poker.TWO_PAIR):
            return self._two_pair_points(hand);
        elif(type_ID == Poker.ONE_PAIR):
            return self._one_pair_points(hand);
        else:
            return self._calculate_points(type_ID, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank);

    # modified points formula for if hand has 4 of a kind
    def _four_of_a_kind_points(self, hand):
        # First, we need to figure out the rank that we have four of as well
        # as the rank of the side card. Importantly, since each hand only
        # has 5 cards, the middle card must be one of the 4 and the side
        # card must be either the first or last.
        rank_four = hand[2].rank;
        rank_spare = 0;
        if(hand[0].rank != rank_four):
            rank_spare = hand[0].rank;
        else:
            rank_spare = hand[4].rank;

        # Now we can assign the c's and calculate the points
        c1 = c2 = c3 = c4 = rank_four;
        c5 = rank_spare;
        return self._calculate_points(Poker.FOUR_OF_A_KIND, c1, c2, c3, c4, c5);

    # modified points formula for if hand is a full house
    def _full_house_points(self, hand):
        # First, we need to determine the rank that we have 3 of and the
        # rank that we have two of. Since the hand is sorted and since
        # each hand only has 5 cards, the middle card must be one of the
        # 3. The first or last card must be one of the two.
        rank_three = hand[2].rank;
        rank_two = 0;

        if(hand[0].rank != rank_three):
            rank_two = hand[0].rank;
        else:
            rank_two = hand[4].rank;

        # Now we can assign the c's and find the points
        c1 = c2 = c3 = rank_three;
        c4 = c5 = rank_two;
        return self._calculate_points(Poker.FULL_HOUSE, c1, c2, c3, c4, c5);

    # modified points formula for if hand has three of a kind
    def _three_of_a_kind_points(self, hand):
        # First, we need to determine the rank that we have 3 of. Since the
        # hand is sorted and since each card only has 5 cards, the middle
        # card must be one of the 3.
        rank_three = hand[2].rank;

        # Now, determine the other two ranks
        spare_card_ranks = [c.rank for c in hand if (c.rank != rank_three)];
        c4 = spare_card_ranks[0];
        c5 = spare_card_ranks[1];

        # Finally, we can assign the other c's and then find the points.
        c1 = c2 = c3 = rank_three;
        return self._calculate_points(Poker.THREE_OF_A_KIND, c1, c2, c3, c4, c5);

    # modified points formula for if hand has two pair
    def _two_pair_points(self, hand):
        # First, we need to determine the rank of the two pairs and the spare
        # card.
        rank_high_pair = 0;
        rank_low_pair = 0;
        rank_spare = 0;
        i = 0;
        while i < (len(hand)-1):
            if(hand[i].rank == hand[i+1].rank):
                if(rank_high_pair == 0):
                    rank_high_pair = hand[i].rank;
                else:
                    rank_low_pair = hand[i].rank;

                # since we know that the ith and i+1th cards are a pair, we need
                # to skip forward two cards (to see if any other pairs exist)
                i += 2;
            else:
                rank_spare = hand[i].rank;
                i += 1;

        # now we can assign the c's and calculate the points.
        c1 = c2 = rank_high_pair
        c3 = c4 = rank_low_pair
        c5 = rank_spare;
        return self._calculate_points(Poker.TWO_PAIR, c1, c2, c3, c4, c5);

    # modified points formula for if hand has one pair
    def _one_pair_points(self, hand):
        # First, we need to determine the rank of the pairs.
        spare_card_ranks = [c.rank for c in hand];
        rank_pair = 0;
        for i in range(len(hand)-1):
            if(hand[i].rank == hand[i+1].rank):
                rank_pair = hand[i].rank;

                # remove both instances of the pair rank.
                spare_card_ranks.remove(rank_pair);
                spare_card_ranks.remove(rank_pair);
                break;

        # Now we can assign the remaining c's and calculate the points.
        c1 = c2 = rank_pair;
        c3 = spare_card_ranks[0];
        c4 = spare_card_ranks[1];
        c5 = spare_card_ranks[2];
        return self._calculate_points(Poker.ONE_PAIR, c1, c2, c3, c4, c5);

    # Calculate points using the formula provided in the problem statement.
    def _calculate_points(self, h, c1, c2, c3, c4, c5):
        return h*(15**5) + c1*(15**4) + c2*(15**3) + c3*(15**2) + c4*(15) + c5;


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
