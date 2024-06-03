import unittest

from TokenSatisfaction.LevensteinDistance import levenshtein_distance


class test_levenshtein_distance(unittest.TestCase):
    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("Saturday", "Sunday"), 3)
        self.assertEqual(levenshtein_distance("book", "back"), 2)
        self.assertEqual(levenshtein_distance("open", "closed"), 4)
        self.assertEqual(levenshtein_distance("", ""), 0)
        self.assertEqual(levenshtein_distance("abc", ""), 3)
        self.assertEqual(levenshtein_distance("", "xyz"), 3)
        self.assertEqual(levenshtein_distance("same", "same"), 0)


if __name__ == "__main__":
    unittest.main()
