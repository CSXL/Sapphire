#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import nltk
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration
from youtube_transcript_api import YouTubeTranscriptApi

from transcription.StringConversion import (
    get_string_format,
    join_most_sophisticated_sentences,
)

load_dotenv()
nltk.download("vader_lexicon")


def get_transcript(video_id: str) -> str:
    """
    Here are the steps to retrieve the transcript of a YouTube video.

    Args:
    ----
        video_id (str): The ID of the YouTube video to retrieve the transcript for.

    Returns:
    -------
        transcript (str): The transcript of the video.
    """
    json_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en", "en-US"])
    string_format = get_string_format(json_list)
    transcript = modify_transcript(200, 2000, video_id, string_format)
    return transcript


def modify_transcript(
    limit1: str, limit2: str, video_id: str, string_format: str
) -> str:
    """
    Follow these steps to modify the transcript string based on the duration of the video.

    Args:
    ----
        limit1 (str): The lower limit of the video duration range to modify the transcript for.
        limit2 (str): The upper limit of the video duration range to modify the transcript for.
        video_id (str): The ID of the YouTube video to retrieve the transcript for.
        string_format (str): The original transcript string to modify.

    Returns:
    -------
        transcript (str): The modified transcript string.
    """
    if get_youtube_video_duration(video_id, os.getenv("api_key")) >= float(
        limit1
    ) and get_youtube_video_duration(video_id, os.getenv("api_key")) <= float(limit2):
        transcript = join_most_sophisticated_sentences(string_format, 1000)
        print("Using method 2")
        return transcript
    else:
        print("Using method 1")
        return string_format


def get_youtube_video_duration(video_id: str, api_key: str) -> float:
    """
    Follow as given to return the duration of a YouTube video given its video ID using the YouTube Data API.
    Request format: https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&id=[VIDEO_ID]M&key=[YOUR_API_KEY]
    Args:
    ----
        video_id (str): The ID of the YouTube video.
        api_key (str): Your YouTube Data API key.

    Returns:
    -------
        float: The duration of the video in seconds.
    """

    youtube = build("youtube", "v3", developerKey=api_key)
    try:
        req = youtube.videos().list(part="contentDetails", id=video_id)
        video_response = req.execute()

        duration = parse_duration(
            video_response["items"][0]["contentDetails"]["duration"]
        ).total_seconds()
        return duration / 60
    except HttpError as e:
        print(f"An error occurred: {e}")
