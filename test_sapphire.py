import unittest
from RigorEvaluation.TextScoring import InformationalRetrievalRank
from RigorEvaluation.TFIDFEvaluation import TFIDFEvaluation
from TokenSatisfaction.KeywordQualification import KeywordQualification
import nltk
from sapphire import Sapphire
nltk.download("punkt")


class test_sapphire(unittest.TestCase):
    def test_sapphire(self):
        videoID = "--qKOhdgJAs"
        rank_score = Sapphire(videoID)
        self.assertIsInstance(rank_score, float)
        self.assertGreaterEqual(rank_score,67.0)
        self.assertLessEqual(rank_score, 100.0)


if __name__ == "__main__":
    unittest.main()
