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
            f"https://youtube.googleapis.com/youtube/v3/captions?key={videoID}&videoId={api_key}",
            body=mock_json_response,
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

        
