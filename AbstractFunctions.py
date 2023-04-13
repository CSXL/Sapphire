from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration

def array_extend(arr1,arr2):
  for element in arr2:
    arr1.append(arr1)
  
def fallback_detection(json):
    sum_ = 0
    for word in json:
        sum_ += json[word]
    if sum_ == 0:
        return 404

def fallback_tfidf_evaluation(corpus,sw):
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
    tfidf_values = X[i,:].toarray()[0]
    # Sort the features by their TF-IDF values and print the top 5
    top_indices = tfidf_values.argsort()[:][::-1]
    for j in top_indices:
       # Map values while managing laplace smoothing to prevent 0 division
        json[feature_names[j]] = tfidf_values[j]*10
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
    This function takes in a string and strips it off any character that is not a letter or a "-".
    """
    return ''.join(c for c in text if c.isalpha() or c == '-')
    
def average_td_idf_score(score_json):
  num = 0
  i = 0
  for word in score_json:
    num += score_json[word]
    i += 1
  return float(num/i)
