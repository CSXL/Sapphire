import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import math
from nltk import tokenize
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import ahocorasick
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')

from AbstractFunctions import *
from stopwords import *
from YouTubeTranscript import *
from AhoCorasick import *
from EvaluationFunction import *
from LevensteinDistance import *


from KeywordQualification import *
from TextScoring import *


class TFIDFEvaluation:
    def __init__(self, videoID):
        self.text = get_transcript(videoID)
        self.text = self.text.lower()
        self.total_words = self.text.split()
        array_extend(sw,sw_spacy)
        array_extend(sw,custom_stopwords)
        array_extend(sw,pronouns)
        array_extend(sw,nouns)
        # Tokenize the text
        self.tokens = word_tokenize(self.text)  
        self.total_sentences = tokenize.sent_tokenize(self.text)
        self.total_sentences_1 = []
        self.total_sent_len = int(0)
        self.tf_score = {}
        self.idf_score = {}
        self.tf_idf_score_new = {}
        self.tf_idf_score = {}
        self.tf_idf_score_n = {}

    def lower_case_conversion(self):
        for sent in self.total_sentences:
            self.total_sentences_1.append(sent.lower())
        self.total_sentences = self.total_sentences_1
        self.total_sent_len = len(self.total_sentences)

    def evaluate_term_freq(self):
        for each_word in self.total_words:
            each_word = each_word.replace('.','')
            if (each_word not in stop_words) and (each_word not in sw_spacy) and (each_word not in custom_stopwords) and (each_word not in pronouns) and (each_word not in nouns) and (each_word not in numbers_str):
                if each_word in self.tf_score:
                    self.tf_score[each_word] += 1
                else:
                    self.tf_score[each_word] = 1
    def evaluate_inverse_doc_freq(self):
        for each_word in self.total_words:
            each_word = each_word.replace('.','')
            if (each_word not in stop_words) and (each_word not in sw_spacy) and (each_word not in custom_stopwords) and (each_word not in pronouns) and (each_word not in nouns) and (each_word not in numbers_str):
                if each_word in self.idf_score:
                    self.idf_score[each_word] = check_sent(each_word, self.total_sentences)
                else:
                    self.idf_score[each_word] = 1
    def initialize_json_scores(self):
        self.idf_score.update((x, math.log(int(self.total_sent_len)/y)) for x, y in self.idf_score.items())

        self.tf_idf_score = {key: self.tf_score[key] * self.idf_score.get(key, 0) for key in self.tf_score.keys()}
    def strip_non_ascii(self):
        for key in self.tf_idf_score:
            new_key = strip_non_alpha_dash(key)
            self.tf_idf_score_new[new_key] = self.tf_idf_score[key]

        self.tf_idf_score = self.tf_idf_score_new

        self.tf_idf_score = get_top_n(self.tf_idf_score_new, len(self.tf_idf_score_new))
    def filter_words(self):
        for word in self.tf_idf_score:
            if word not in custom_stopwords:
                self.tf_idf_score_n[word] = self.tf_idf_score[word]
    def fallback_evaluation(self):  
        if fallback_detection(self.tf_idf_score_n) == 404:
            self.tf_idf_score_n = fallback_tfidf_evaluation(self.text,sw)
        self.tf_idf_score = self.tf_idf_score_n
        return (self.tf_idf_score)