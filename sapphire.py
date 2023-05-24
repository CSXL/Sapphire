#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk  # Used for performing standard NLP tasks like lexical analysis

from RigorEvaluation.TextScoring import InformationalRetrievalRank
from RigorEvaluation.TFIDFEvaluation import TFIDFEvaluation
from TokenSatisfaction.KeywordQualification import KeywordQualification

nltk.download("punkt")


def Sapphire(videoID: str) -> float:
    """
    To get the rank score of the YouTube video(videoID) using the Sapphire algorithm, follow these steps.

    Args:
    ----
    - videoID (str): The unique identification of a YouTube video.

    Returns:
    -------
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
    ir_evaluator.fallback_evaluation()
    k_qualifier = KeywordQualification(ir_evaluator.tokens, ir_evaluator.tf_idf_score)
    (freq_dist, qualification, qualified_terms) = k_qualifier.show()

    # Calculate rank score
    rank_score = InformationalRetrievalRank(qualified_terms, freq_dist, qualification)

    return float(rank_score)
print(Sapphire("bqu6BquVi2M"))