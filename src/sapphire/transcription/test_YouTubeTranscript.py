# Test YouTubeTranscript
import unittest

import httpretty

from transcription import YouTubeTranscript


class TestGetYouTubeVideoDuration(unittest.TestCase):
    def test_get_youtube_video_duration(self):
        """
        Tests the get_youtube_video_duration function.
        """
        # Mock JSON response
        # Adapted from request made to 'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=ix5jPkxsr7M&key=[YOUR_API_KEY]
        # on 4/26/2023.
        mock_json_response = """{"kind":"youtube#videoListResponse","items":[{"kind":"youtube#video","etag":"exampleETag","id":"example_videoID","contentDetails":{"duration":"PT2H13M17S"}}]}"""
        videoID = "example_videoID"
        api_key = "example_api_key"
        expected_duration = 133.28333333333333
        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            "https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=example_videoID&key=example_api_key",
            body=mock_json_response,
        )
        actual_duration = YouTubeTranscript.get_youtube_video_duration(videoID, api_key)
        self.assertEqual(expected_duration, actual_duration)
