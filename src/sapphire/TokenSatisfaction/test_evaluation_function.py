import unittest

from TokenSatisfaction.EvaluationFunction import get_n_val, get_top_n, text_scoring


class test_text_scoring(unittest.TestCase):
    def test_text_scoring(self):
        # Test case 1
        ranked_keywords = {"keyword1": 0.5, "keyword2": 0.3, "keyword3": 0.7}
        freq_dist = {"keyword1": 0.2, "keyword2": 0.1, "keyword3": 0.5}
        threshold_n = 2
        expected_result = 0.24  # Calculate the expected result based on the formula
        self.assertEqual(
            text_scoring(ranked_keywords, freq_dist, threshold_n), expected_result
        )

        # Test case 2
        ranked_keywords = {"keyword1": 0.4, "keyword2": 0.2}
        freq_dist = {"keyword1": 0.3, "keyword2": 0.2, "keyword3": 0.1}
        threshold_n = 3
        expected_result = 0.05333333333333334
        self.assertEqual(
            text_scoring(ranked_keywords, freq_dist, threshold_n), expected_result
        )


class test_get_n_val(unittest.TestCase):
    def test_get_n_val(self):
        # Test case 1
        average_td_idf_score = 0.5
        score_json = {"term1": 0.3, "term2": 0.6, "term3": 0.8}
        expected_result = 2  # Two terms have scores greater than or equal to 0.5
        self.assertEqual(get_n_val(average_td_idf_score, score_json), expected_result)

        # Test case 2
        average_td_idf_score = 0.4
        score_json = {"term1": 0.3, "term2": 0.6, "term3": 0.8}
        expected_result = 2  # All three terms have scores greater than or equal to 0.4
        self.assertEqual(get_n_val(average_td_idf_score, score_json), expected_result)


class test_get_top_n(unittest.TestCase):
    def test_get_top_n(self):
        # Test case 1
        dict_elem = {"key1": 0.5, "key2": 0.3, "key3": 0.7}
        n = 2
        expected_result = {"key3": 0.7, "key1": 0.5}  # Top 2 elements based on values
        self.assertEqual(get_top_n(dict_elem, n), expected_result)

        # Test case 2
        dict_elem = {"key1": 0.5, "key2": 0.3, "key3": 0.7}
        n = 1
        expected_result = {"key3": 0.7}  # Top 1 element based on value
        self.assertEqual(get_top_n(dict_elem, n), expected_result)


if __name__ == "__main__":
    unittest.main()
