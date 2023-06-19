import unittest

import httpretty

from sapphire import Sapphire


class TestSapphire(unittest.TestCase):
    def test_calculate_rank_score(self):

        # Mock JSON response
        # Adapted from request made to 'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=ix5jPkxsr7M&key=[YOUR_API_KEY]
        # on 4/26/2023.
        mock_json_response = """[{"text":"example_text","start":"example_start","duration":"example_duration"}]"""
        videoID = "example_videoID"
        api_key = "example_api_key"
        expected_score = 69.6828989690041
        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            "https://youtube.googleapis.com/youtube/v3/captions?key=[example_api_key]&videoId=[example_videoID]",
            body=mock_json_response,
        )
        actual_duration = Sapphire().calculate_rank_score(videoID)
        self.assertEqual(expected_duration, actual_duration)

        
