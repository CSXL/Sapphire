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
from TFIDFEvaluation import *
from KeywordQualification import *

def Sapphire(videoID):
    ir_evaluator = TFIDFEvaluation(videoID)
    ir_evaluator.lower_case_conversion()
    ir_evaluator.evaluate_term_freq()
    ir_evaluator.evaluate_inverse_doc_freq()
    ir_evaluator.initialize_json_scores()
    ir_evaluator.strip_non_ascii()
    ir_evaluator.filter_words()
    fallback_evaluation = ir_evaluator.fallback_evaluation()
    k_qualifier = KeywordQualification(ir_evaluator.tokens,ir_evaluator.tf_idf_score)
    freq_dist,qualification,qualified_terms=k_qualifier.show()

    rank_score = InformationalRetrievalRank(qualified_terms,freq_dist,qualification)
    return float(rank_score)