import unittest;
from Poker import Card, Poker;

class Hand_Tests(unittest.TestCase):
    def test_royal_flush(self):
        # First, generate some hands. Some are royal flushes, some are not.
        H1 = [Card(14, 'S'), Card(13, 'S'), Card(12, 'S'), Card(11, 'S'), Card(10, 'S')];   # Royal flush
        H2 = [Card(6, 'S'),  Card(5, 'S'),  Card(4, 'S'),  Card(3, 'S'),  Card(2, 'S') ];   # Straight flush
        H3 = [Card(14, 'S'), Card(13, 'D'), Card(12, 'H'), Card(11, 'H'), Card(10, 'C')];   # Straight
        H4 = [Card(13, 'C'), Card(12, 'C'), Card(8, 'C'),  Card(5, 'C'),  Card(2, 'C') ];   # Flush
        H5 = [Card(9, 'D'),  Card(9, 'D'),  Card(4, 'S'),  Card(4, 'S'),  Card(1, 'C') ];   # Two pair.
        H6 = [Card(14, 'C'), Card(13, 'H'), Card(12, 'C'), Card(5, 'H'),  Card(5, 'D')];    # One pair.

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_royal_flush(H1));
        self.assertFalse(P.is_royal_flush(H2));
        self.assertFalse(P.is_royal_flush(H3));
        self.assertFalse(P.is_royal_flush(H4));
        self.assertFalse(P.is_royal_flush(H5));
        self.assertFalse(P.is_royal_flush(H6));

    def test_straight_flush(self):
        # First, generate some hands. Some are straight flushes, some are not.
        H1 = [Card(6, 'S'),  Card(5, 'S'),  Card(4, 'S'),  Card(3, 'S'),  Card(2, 'S')];    # straight flush
        H2 = [Card(13, 'S'), Card(12, 'D'), Card(11, 'H'), Card(10, 'H'), Card(9, 'C')];    # straight
        H3 = [Card(13, 'C'), Card(11, 'C'), Card(10, 'C'), Card(5, 'C'),  Card(4, 'C') ];   # Flush
        H4 = [Card(14, 'D'), Card(14, 'C'), Card(5, 'H'),  Card(5, 'C'),  Card(3, 'D') ];   # two pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_straight_flush(H1));
        self.assertFalse(P.is_straight_flush(H2));
        self.assertFalse(P.is_straight_flush(H3));
        self.assertFalse(P.is_straight_flush(H4));

    def test_flush(self):
        # First, generate some hands. Some are flushes, others are not.
        H1 = [Card(6, 'S'),  Card(5, 'S'),  Card(4, 'S'), Card(3, 'S'), Card(2, 'S')];      # Flush
        H2 = [Card(13, 'C'), Card(7, 'C'),  Card(6, 'C'), Card(5, 'C'), Card(2, 'C') ];     # Flush
        H3 = [Card(10, 'C'), Card(9, 'C'),  Card(9, 'D'), Card(4, 'H'), Card(3, 'S')];      # One Pair
        H4 = [Card(14, 'C'), Card(11, 'D'), Card(5, 'C'), Card(2, 'S'), Card(2, 'C')];      # One Pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_flush(H1));
        self.assertTrue(P.is_flush(H2));
        self.assertFalse(P.is_flush(H3));
        self.assertFalse(P.is_flush(H4));

    def test_straight(self):
        # First, generate some hands. Some are straights, some are not.
        H1 = [Card(6, 'S'),  Card(5, 'S'),  Card(4, 'S'),  Card(3, 'S'),  Card(2, 'S') ];   # Straight
        H2 = [Card(13, 'S'), Card(12, 'D'), Card(11, 'H'), Card(10, 'H'), Card(9, 'C') ];   # Straight
        H3 = [Card(12, 'S'), Card(11, 'H'), Card(7, 'C'),  Card(5, 'D'),  Card(3, 'H')];    # Nothing
        H4 = [Card(14, 'D'), Card(5, 'D'),  Card(5, 'H'),  Card(5, 'C'),  Card(3, 'D')];    # Three of a kind

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_straight(H1));
        self.assertTrue(P.is_straight(H2));
        self.assertFalse(P.is_straight(H3));
        self.assertFalse(P.is_straight(H4));

    def test_four_of_a_kind(self):
        # First, generate some hands. Some have 4 of a kind, some don't.
        H1 = [Card(5, 'S'),  Card(5, 'D'),  Card(5, 'H'), Card(5, 'C'), Card(3, 'D')];      # Four of a kind
        H2 = [Card(14, 'D'), Card(5, 'D'),  Card(5, 'H'), Card(5, 'C'), Card(3, 'D')];      # Three of a kind
        H3 = [Card(9, 'C'),  Card(6, 'S'),  Card(5, 'C'), Card(4, 'S'), Card(3, 'D')];      # Nothing
        H4 = [Card(12, 'C'), Card(11, 'S'), Card(9, 'D'), Card(9, 'C'), Card(5, 'S')];      # One pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_four_of_a_kind(H1));
        self.assertFalse(P.is_four_of_a_kind(H2));
        self.assertFalse(P.is_four_of_a_kind(H3));
        self.assertFalse(P.is_four_of_a_kind(H4));

    def test_full_house(self):
        # First, generate some hands. Some have a full house, some don't.
        H1 = [Card(13, 'S'), Card(13, 'D'), Card(13, 'H'), Card(7, 'C'), Card(7, 'D')];     # Full House
        H2 = [Card(14, 'D'), Card(5, 'D'),  Card(5, 'H'),  Card(5, 'C'), Card(3, 'D')];     # Three of a kind
        H3 = [Card(9, 'C'),  Card(6, 'S'),  Card(5, 'C'),  Card(4, 'S'), Card(3, 'D')];     # Nothing
        H4 = [Card(12, 'C'), Card(11, 'S'), Card(9, 'D'),  Card(9, 'C'), Card(5, 'S')];     # One pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_full_house(H1));
        self.assertFalse(P.is_full_house(H2));
        self.assertFalse(P.is_full_house(H3));
        self.assertFalse(P.is_full_house(H4));

    def test_three_of_a_kind(self):
        # First, generate some hands. Some have 3 of a kind, some don't.
        H1 = [Card(14, 'D'), Card(5, 'D'),  Card(5, 'H'), Card(5, 'C'), Card(3, 'D')];      # Three of a kind
        H2 = [Card(5, 'S'),  Card(5, 'D'),  Card(5, 'H'), Card(5, 'C'), Card(3, 'D')];      # Four of a kind
        H3 = [Card(13, 'C'), Card(10, 'H'), Card(5, 'C'), Card(4, 'C'), Card(4, 'H')];      # One pair
        H4 = [Card(12, 'D'), Card(11, 'H'), Card(6, 'D'), Card(6, 'S'), Card(5, 'H')];      # One pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_three_of_a_kind(H1));
        self.assertTrue(P.is_three_of_a_kind(H2));
        self.assertFalse(P.is_three_of_a_kind(H3));
        self.assertFalse(P.is_three_of_a_kind(H4));

    def test_two_pair(self):
        # First, generate some hands. Some have two pairs, some don't.
        H1 = [Card(14, 'C'), Card(14, 'D'), Card(10, 'S'), Card(10, 'C'), Card(4, 'D')];    # Two pair
        H2 = [Card(12, 'D'), Card(7, 'S'),  Card(7, 'S'),  Card(3, 'C'),  Card(3, 'H')];    # Two pair
        H3 = [Card(5, 'S'),  Card(5, 'D'),  Card(5, 'H'),  Card(5, 'C'),  Card(3, 'D')];    # Four of a kind
        H4 = [Card(11, 'D'), Card(8, 'D'),  Card(4, 'H'),  Card(2, 'S'),  Card(2, 'C')];    # One pair
        H5 = [Card(13, 'C'), Card(12, 'H'), Card(11, 'S'), Card(9, 'D'),  Card(7, 'S')];    # Nothing
        H6 = [Card(13, 'H'), Card(13, 'S'), Card(12, 'D'), Card(11, 'C'), Card(4, 'S')];    # Nothing

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_two_pair(H1))
        self.assertTrue(P.is_two_pair(H2));
        self.assertTrue(P.is_two_pair(H3));
        self.assertFalse(P.is_two_pair(H4));
        self.assertFalse(P.is_two_pair(H5));
        self.assertFalse(P.is_two_pair(H6));

    def test_one_pair(self):
        # First, generate some hands. Some have pairs, some don't.
        H1 = [Card(11, 'D'), Card(9, 'H'),  Card(5, 'S'),  Card(5, 'C'),  Card(5, 'D')];    # One pair
        H2 = [Card(10, 'S'), Card(8, 'D'),  Card(8, 'S'),  Card(8, 'H'),  Card(5, 'S')];    # Three of a kind
        H3 = [Card(14, 'H'), Card(13, 'S'), Card(12, 'D'), Card(12, 'C'), Card(6, 'C')];    # One pair
        H4 = [Card(14, 'D'), Card(13, 'H'), Card(11, 'C'), Card(10, 'D'), Card(2, 'D')];    # Nothing
        H5 = [Card(14, 'C'), Card(12, 'H'), Card(11, 'S'), Card(7, 'S'),  Card(3, 'D')];    # Nothing

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_one_pair(H1))
        self.assertTrue(P.is_one_pair(H2));
        self.assertTrue(P.is_one_pair(H3));
        self.assertFalse(P.is_one_pair(H4));
        self.assertFalse(P.is_one_pair(H5));



if(__name__ == "__main__"):
    unittest.main();
