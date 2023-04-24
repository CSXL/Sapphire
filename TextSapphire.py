import unittest
from unittest.mock import patch

from sapphire import Sapphire


class TestSapphire(unittest.TestCase):
    @patch("sapphire.requests.get")
    def test_sapphire(self, mock_get):
        videoID = "ix5jPkxsr7M"
        expected_score = 152.23789533365175

        # mock the response from the requests.get call in Sapphire function
        mock_response = type(
            "MockResponse",
            (object,),
            {"status_code": 200, "json": lambda self: {"score": expected_score}},
        )
        mock_get.return_value = mock_response

        # call the Sapphire function and assert the result
        actual_score = Sapphire(videoID)
        self.assertAlmostEqual(actual_score, expected_score, places=2)
