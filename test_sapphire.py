"""
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
"""

import unittest
from unittest.mock import patch
from RigorEvaluation.TextScoring import InformationalRetrievalRank
from RigorEvaluation.TFIDFEvaluation import TFIDFEvaluation
from TokenSatisfaction.KeywordQualification import KeywordQualification
import nltk
from sapphire import Sapphire
import httpretty
nltk.download("punkt")


import unittest
import httpretty

class test_sapphire(unittest.TestCase):
    def test_sapphire(self):
        videoID = "--qKOhdgJAs"

        # Mock the Sapphire function to return a desired value

        mock_json_response = """{"kind":"youtube#videoListResponse","items":[{"kind":"youtube#video","etag":"exampleETag","id":"example_videoID","contentDetails":{"duration":"PT2H13M17S"}}]}"""
        api_key = "example_api_key"
        expected_result = 94.10661404911535

        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            "https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=example_videoID&key=example_api_key",
            body=mock_json_response,
        )

        actual_result = Sapphire(videoID)

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
