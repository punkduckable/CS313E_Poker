import unittest;
from Poker import Card, Poker;

class Hand_Tests(unittest.TestCase):
    def test_royal_flush(self):
        # First, generate some hands. Some are royal flushes, some are not.
        H1 = [Card(14, 'S'), Card(13, 'S'), Card(12,'S'), Card(11, 'S'), Card(10, 'S')];    # Royal flush
        H2 = [Card(6, 'S'),  Card(5, 'S'),  Card(4,'S'),  Card(3, 'S'),  Card(2, 'S') ];    # Straight flush
        H3 = [Card(14, 'S'), Card(13, 'D'), Card(12,'H'), Card(11, 'H'), Card(10, 'C')];    # Straight
        H4 = [Card(5, 'C'),  Card(13, 'C'), Card(12,'C'), Card(2, 'C'),  Card(8, 'C') ];    # Flush
        H5 = [Card(4, 'S'),  Card(1, 'C'),  Card(9, 'D'), Card(9, 'D'),  Card(4, 'S') ];    # Two pair.
        H6 = [Card(14, 'C'), Card(5, 'H'),  Card(5, 'D'), Card(13, 'H'), Card(12, 'C')];    # One pair.

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
        H1 = [Card(6, 'S'),  Card(5, 'S'),  Card(4,'S'),  Card(3, 'S'),  Card(2, 'S') ];    # straight flush
        H2 = [Card(13, 'S'), Card(12, 'D'), Card(11,'H'), Card(10, 'H'), Card(9, 'C') ];    # straight
        H3 = [Card(5, 'C'),  Card(13, 'C'), Card(12,'C'), Card(2, 'C'),  Card(8, 'C') ];    # flush
        H4 = [Card(5, 'H'),  Card(5, 'C'),  Card(3,'D'),  Card(14, 'D'), Card(14, 'C')];    # two pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_straight_flush(H1));
        self.assertFalse(P.is_straight_flush(H2));
        self.assertFalse(P.is_straight_flush(H3));
        self.assertFalse(P.is_straight_flush(H4));

    def test_flush(self):
        # First, generate some hands. Some are flushes, others are not.
        H1 = [Card(6, 'S'), Card(5, 'S'),  Card(4,'S'),   Card(3, 'S'),  Card(2, 'S')];     # Flush
        H2 = [Card(5, 'C'), Card(13, 'C'), Card(12,'C'),  Card(2, 'C'),  Card(8, 'C')];     # Flush
        H3 = [Card(5, 'C'), Card(4, 'H'),  Card(3, 'S'),  Card(10, 'C'), Card(7,'S') ];     # Nothing
        H4 = [Card(2, 'S'), Card(5, 'C'),  Card(11, 'D'), Card(2, 'C'),  Card(14,'C')];     # One Pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_flush(H1));
        self.assertTrue(P.is_flush(H2));
        self.assertFalse(P.is_flush(H3));
        self.assertFalse(P.is_flush(H4));

    def test_straight(self):
        # First, generate some hands. Some are straights, some are not.
        H1 = [Card(6, 'S'),  Card(5, 'S'),  Card(4,'S'),  Card(3, 'S'),  Card(2, 'S') ];    # Straight
        H2 = [Card(13, 'S'), Card(12, 'D'), Card(11,'H'), Card(10, 'H'), Card(9, 'C') ];    # Straight
        H3 = [Card(5, 'D'),  Card(11, 'H'), Card(3,'H'),  Card(7, 'C'),  Card(12, 'S')];    # Nothing
        H4 = [Card(5, 'H'),  Card(5, 'C'),  Card(3,'D'),  Card(14, 'D'), Card(14, 'C')];    # Two pair

        # Now, create a poker game object (so that we can use its methods) and
        # test that it gives the correct results.
        P = Poker(2);

        self.assertTrue(P.is_straight(H1));
        self.assertTrue(P.is_straight(H2));
        self.assertFalse(P.is_straight(H3));
        self.assertFalse(P.is_straight(H4));

if(__name__ == "__main__"):
    unittest.main();
