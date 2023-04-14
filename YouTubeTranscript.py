from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration
import os
from dotenv import load_dotenv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

load_dotenv()
nltk.download('vader_lexicon')

def get_transcript(videoID):
  json_list = YouTubeTranscriptApi.get_transcript(videoID,languages=['en','en-US'])
  string_format = get_string_format(json_list)  
  transcript = modify_transcript(200,2000,videoID,string_format)
  return transcript

def get_string_format(json_list):
  string= ''
  for _ in json_list:
    string += _['text']
    string += ' '
  return string

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration


def modify_transcript(limit1,limit2,video_id,string_format):
  if get_youtube_video_duration(video_id,os.getenv("api_key")) >= float(limit1) and get_youtube_video_duration(video_id,os.getenv("api_key")) <= float(limit2):
    transcript =  join_most_sophisticated_sentences(string_format,500)
    print('method 2')
    return transcript
  else:
    print("method 1")
    return string_format

def get_youtube_video_duration(video_id, api_key):
    """
    Returns the duration of a YouTube video given its video ID using the YouTube Data API.

    Parameters:
    video_id (str): The ID of the YouTube video.
    api_key (str): Your YouTube Data API key.

    Returns:
    float: The duration of the video in seconds.
    """

    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        video_response = youtube.videos().list(
            part='contentDetails',
            id=video_id
        ).execute()

        duration = parse_duration(video_response['items'][0]['contentDetails']['duration']).total_seconds()

        return duration/60
    except HttpError as e:
        print(f'An error occurred: {e}')

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def join_most_sophisticated_sentences(text, num_sentences):
    """
    Joins the most sophisticated sentences of a text (string) together.

    Args:
        text (str): The input text.
        num_sentences (int): The number of sophisticated sentences to join.

    Returns:
        str: The joined sophisticated sentences of the input text.
    """
    if len(text) == 0:
        return ""

    # Tokenize the input text into sentences
    sentences = nltk.sent_tokenize(text)

    # Initialize the Sentiment Intensity Analyzer
    sid = SentimentIntensityAnalyzer()

    # Calculate the sentiment scores for each sentence
    sentence_scores = {}
    for sentence in sentences:
        sentiment_scores = sid.polarity_scores(sentence)
        sentence_scores[sentence] = sentiment_scores

    # Sort the sentences based on their compound sentiment score in descending order
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1]['compound'], reverse=True)

    # Extract the most sophisticated sentences
    sophisticated_sentences = [sentence for sentence, _ in sorted_sentences[:num_sentences]]

    # Join the most sophisticated sentences back into a single string
    sophisticated_text = " ".join(sophisticated_sentences)

    return sophisticated_text