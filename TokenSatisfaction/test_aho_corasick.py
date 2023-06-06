
import unittest
from typing import Dict
from TokenSatisfaction.LevensteinDistance import levenshtein_distance
from TokenSatisfaction.AhoCorasick import get_closest_score_from_tfidf_dict
class test_get_closest_score_from_tfidf_dict(unittest.TestCase):
    def test_get_closest_score_from_tfidf_dict(self):
        tfidf_dict = {
            "apple": 5.0,
            "banana": 0.3,
            "cherry": 0.2,
        }
        closest_key = get_closest_score_from_tfidf_dict("bfh", tfidf_dict)
        print(closest_key)
        self.assertEqual(closest_key, None)

        


if __name__ == "__main__":
    unittest.main()

