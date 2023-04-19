#!/usr/bin/python
# -*- coding: utf-8 -*-
import nltk #Used for performing standard NLP tasks like lexical analysis
from nltk.tokenize import word_tokenize #Used for tokenizing individual words for weightage evaluation
from nltk.corpus import stopwords #Use stopwords to hold unnecessary words as residue
from nltk.probability import FreqDist #Used for calculating the frequency of tokens in a corpus
import math # used for performing the log operation in IDF evaluation
from nltk import tokenize #Tokenizing words specifically for dictionary mapping(to result in score prediction)
import spacy #Load a new set of stopwords
from sklearn.feature_extraction.text import TfidfVectorizer #Evaluate TF-IDF score using cython

nltk.download('stopwords')
nltk.download('punkt')

from AbstractFunctions import *  
from stopwords import *  
from YouTubeTranscript import *  
from EvaluationFunction import *  
from TFIDFEvaluation import *  
from KeywordQualification import *  


def Sapphire(videoID):
    """
    Returns the rank score of a video using the Sapphire algorithm.

    Args:
    - videoID (str): The ID of the video to be evaluated.

    Returns:
    - float: The rank score of the video.

    """

    # Initialize the evaluation object
    ir_evaluator = TFIDFEvaluation(videoID)

    # Perform text pre-processing
    ir_evaluator.lower_case_conversion()
    ir_evaluator.evaluate_term_freq()
    ir_evaluator.evaluate_inverse_doc_freq()
    ir_evaluator.initialize_json_scores()
    ir_evaluator.strip_non_ascii()
    ir_evaluator.filter_words()

    # Perform keyword qualification
    fallback_evaluation = ir_evaluator.fallback_evaluation()
    k_qualifier = KeywordQualification(ir_evaluator.tokens, ir_evaluator.tf_idf_score)
    (freq_dist, qualification, qualified_terms) = k_qualifier.show()

    # Calculate rank score
    rank_score = InformationalRetrievalRank(qualified_terms, freq_dist, qualification)

    return float(rank_score)



print(Sapphire('h0e2HAPTGF4'))
