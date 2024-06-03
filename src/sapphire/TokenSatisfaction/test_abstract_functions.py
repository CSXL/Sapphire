import unittest

from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

from TokenSatisfaction.AbstractFunctions import (
    alphabets,
    array_extend,
    average_td_idf_score,
    check_sent,
    fallback_detection,
    fallback_tfidf_evaluation,
    freq_dist,
    strip_non_alpha_dash,
)


class test_abstract_function(unittest.TestCase):
    def test_array_extend(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        array_extend(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6])

    def test_fallback_detection(self):
        json = {"a": 0, "b": 0, "c": 0}
        result = fallback_detection(json)
        self.assertEqual(result, 404)

    def test_fallback_tfidf_evaluation(self):
        corpus = "This is a sample sentence. Another sentence."
        sw = ["is", "a"]
        result = fallback_tfidf_evaluation(corpus, sw)
        expected = {
            "sample": 0.0,
            "sentence": 10.0,
        }
        self.assertEqual(result, expected)

    def test_alphabets(self):
        result = alphabets()
        expected = list("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, expected)

    def test_freq_dist(self):
        tokens = ["apple", "banana", "apple", "cherry", "banana"]
        result = freq_dist(tokens)
        expected = {
            "apple": 2,
            "banana": 2,
            "cherry": 1,
        }
        self.assertEqual(result, expected)

    def test_check_sent(self):
        word = ["apple", "banana"]
        sentences = ["I like apples and bananas.", "She ate an apple and a banana."]
        result = check_sent(word, sentences)
        self.assertEqual(result, 2)

    def test_strip_non_alpha_dash(self):
        text = "This is a sample text! It contains @#$ special characters."
        result = strip_non_alpha_dash(text)
        expected = "ThisisasampletextItcontainsspecialcharacters"
        self.assertEqual(result, expected)

    def test_average_td_idf_score(self):
        score_json = {"apple": 10, "banana": 20, "cherry": 30}
        result = average_td_idf_score(score_json)
        expected = 20.0
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
