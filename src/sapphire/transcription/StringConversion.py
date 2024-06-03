import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


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
        string += segment["text"]
        string += " "
    return string


def join_most_sophisticated_sentences(text, num_sentences):
    scores = []
    """
    Follow as given to join the most sophisticated sentences of a text (string) together.

    Args:
    ----
        text (str): The input text.
        num_sentences (int): The number of sophisticated sentences to join.

    Returns:
    -------
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
    sorted_sentences = sorted(
        sentence_scores.items(), key=lambda x: x[1]["compound"], reverse=True
    )
    # Extract the most sophisticated sentences
    sophisticated_sentences = [
        sentence for (sentence, _) in sorted_sentences[:num_sentences]
    ]

    # Join the most sophisticated sentences back into a single string
    sophisticated_text = " ".join(sophisticated_sentences)

    return sophisticated_text
