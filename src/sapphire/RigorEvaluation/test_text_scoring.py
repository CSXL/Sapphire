import unittest

from RigorEvaluation.TextScoring import InformationalRetrievalRank


class test_text_scoring(unittest.TestCase):
    def test_informational_retrieval_rank(self):
        # Test case 1
        ranked_keywords = {"keyword1": 0.5, "keyword2": 0.3, "keyword3": 0.7}
        freq_dist = {"keyword1": 0.2, "keyword2": 0.1, "keyword3": 0.5}
        threshold_n = 2
        expected_result = 0.24  # Calculate the expected result based on the formula
        self.assertEqual(
            InformationalRetrievalRank(ranked_keywords, freq_dist, threshold_n),
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
