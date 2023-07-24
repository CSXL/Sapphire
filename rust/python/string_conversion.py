import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration
import heapq

nltk.download("punkt")
nltk.download('vader_lexicon')
load_dotenv()

sid = SentimentIntensityAnalyzer()
def join_most_sophisticated_sentences(text, num_sentences, sid):
    # Tokenize the input text into sentences
    sentences = nltk.sent_tokenize(text)

    # Initialize the priority queue with the first `num_sentences` sentences
    priority_queue = []
    for sentence in sentences[:num_sentences]:
        sentiment_scores = sid.polarity_scores(sentence)
        heapq.heappush(priority_queue, (-sentiment_scores["compound"], sentence))

    # Iterate over the remaining sentences, keeping track of the top `num_sentences` sophisticated sentences
    for sentence in sentences[num_sentences:]:
        sentiment_scores = sid.polarity_scores(sentence)
        compound_score = -sentiment_scores["compound"]
        if compound_score > priority_queue[0][0]:
            heapq.heappop(priority_queue)
            heapq.heappush(priority_queue, (compound_score, sentence))

    # Extract the most sophisticated sentences from the priority queue in descending order
    sophisticated_sentences = [sentence for _, sentence in sorted(priority_queue, reverse=True)]
    
    # Join the most sophisticated sentences back into a single string
    sophisticated_text = " ".join(sophisticated_sentences)

    return sophisticated_text
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
        transcript = join_most_sophisticated_sentences(string_format, 1000,sid)
        print("Using method 2")
        return transcript
    else:
        print("Using method 1")
        return string_format    



def get_string_format(json_list: list) -> str:
    """
    To formats the transcript JSON into a string format, follow as given.

    Args:
    ----
        json_list (list): A list of transcript segments in JSON format.

    Returns:
    -------
        string (str): A formatted string containing the transcript text.
    """
    string = ""
    for segment in json_list:
        string += segment["text"]+"."
        string += " "
    return string

def get_youtube_video_duration(video_id: str, api_key: str) -> float:
    """
    Follow as given to return the duration of a YouTube video given its video ID using the YouTube Data API.

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
        video_response = (
            youtube.videos().list(part="contentDetails", id=video_id).execute()
        )

        duration = parse_duration(
            video_response["items"][0]["contentDetails"]["duration"]
        ).total_seconds()
        return duration / 60
    except HttpError as e:
        print(f"An error occurred: {e}")


def sent_tokenize(string):
    sent_tokens = nltk.sent_tokenize(string)
    return sent_tokens