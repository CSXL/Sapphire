import os
import unittest

import httpretty

from sapphire import Sapphire


class TestSapphire(unittest.TestCase):
    def test_calculate_rank_score(self):
        # Mock JSON response
        # Adapted from request made to https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=T9xsTO6ujqM&key=[YOUR_API_KEY]
        # on 6/22/2023.
        mock_video_duration_response = """
        {
            "kind": "youtube#videoListResponse",
            "etag": "jRM3UkS0H97J0JE_RooCw1CNA0c",
            "items": [
                {
                    "kind": "youtube#video",
                    "etag": "2_4jVYm_8tYAVsj-Vg_P8HJ6qkc",
                    "id": "T9xsTO6ujqM",
                    "contentDetails": {
                        "duration": "PT24M20S",
                        "dimension": "2d",
                        "definition": "hd",
                        "caption": "false",
                        "licensedContent": true,
                        "contentRating": {},
                        "projection": "rectangular"
                    }
                }
            ],
            "pageInfo": {
                "totalResults": 1,
                "resultsPerPage": 1
            }
        }
        """
        videoID = "example_videoID"
        api_key = "example_api_key"
        os.environ["api_key"] = api_key
        expected_score = 2.9120317139990197
        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id={videoID}&key={api_key}&alt=json",
            body=mock_video_duration_response,
        )
        with open("tests/sample_data/example_youtube_video.html", "r") as f:
            mock_youtube_html_response = f.read()
        with open("tests/sample_data/example_xml_youtube_transcript.xml", "r") as f:
            mock_youtube_xml_response = f.read()
        httpretty.register_uri(
            httpretty.GET,
            f"https://www.youtube.com/watch?v={videoID}",
            body=mock_youtube_html_response,
        )
        # This is the request that is made to get the final transcript
        httpretty.register_uri(
            httpretty.GET,
            "https://www.youtube.com/api/timedtext?v=T9xsTO6ujqM&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1687325993&sparams=ip,ipbits,expire,v,caps,opi,xoaf&signature=82EC42B531F868F24D3EF4C6765BFA55A735C121.851DCD4FDCD046D8793E98EFEDC7F451B8156CFE&key=yt8&kind=asr&lang=en",
            body=mock_youtube_xml_response,
        )

        actual_duration = Sapphire().calculate_rank_score(videoID)
        self.assertEqual(expected_score, actual_duration)
