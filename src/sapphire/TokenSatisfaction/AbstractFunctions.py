from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def array_extend(arr1, arr2):
    """
    Follow the steps to extend the first array with the elements of the second array.

    Args:
    ----
    arr1 (list): The first array to be extended.
    arr2 (list): The second array containing elements to add to arr1.

    Returns:
    -------
    None
    """
    # Hint: In the loop, you need to append `element` to `arr1`, not `arr1` to `arr1`.
    for element in arr2:
        arr1.append(element)


def fallback_detection(json):
    sum_ = 0
    for word in json:
        sum_ += json[word]
    if sum_ == 0:
        return 404


def fallback_tfidf_evaluation(corpus, sw):
    corpus = sent_tokenize(corpus)

    # Initialize the TfidfVectorizer with optional parameters

    vectorizer = TfidfVectorizer(stop_words="english")

    # Fit the vectorizer to the corpus and transform the corpus

    X = vectorizer.fit_transform(corpus)

    # Get the feature names (important words) from the vectorizer

    feature_names = vectorizer.get_feature_names_out()
    json = {}

    # Loop through each document in the corpus and print the important words

    for i in range(len(corpus)):
        # Get the TF-IDF values for each feature in the current document

        tfidf_values = X[i, :].toarray()[0]

        # Sort the features by their TF-IDF values and print the top 5

        top_indices = tfidf_values.argsort()[:][::-1]
        for j in top_indices:
            # Map values while managing laplace smoothing to prevent 0 division

            json[feature_names[j]] = tfidf_values[j] * 10
    return json


def alphabets():
    import string

    alphabet_array = list(string.ascii_lowercase)

    return list(alphabet_array)


# Create frequency distribution of keywords


def freq_dist(tokens):
    freq_dist = FreqDist(tokens)

    # Print the frequency distribution

    freq_dist = dict(freq_dist)
    return freq_dist


def check_sent(word, sentences):
    final = [all([w in x for w in word]) for x in sentences]
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))


def strip_non_alpha_dash(text):
    """
    Use the method to strip it off any character that is not a letter or a "-".
    """

    return "".join(c for c in text if c.isalpha() or c == "-")


def average_td_idf_score(score_json: dict) -> float:
    num = 0
    i = 0
    for word in score_json:
        num += score_json[word]
        i += 1
    return float(num / i)
