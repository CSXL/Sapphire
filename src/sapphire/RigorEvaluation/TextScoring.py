from TokenSatisfaction.EvaluationFunction import text_scoring


def InformationalRetrievalRank(qualified_terms, freq_dist, qualification):
    """
    Follow the steps to compute a score for a document based on its frequency distribution and the frequency of qualified terms.

    Args:
    ----
        qualified_terms (list): A list of terms that the document should be qualified for.
        freq_dist (FreqDist): A frequency distribution of terms in the document.
        qualification (int): A value indicating the required frequency of qualified terms in the document.

    Returns:
    -------
        float: A score between 0 and 1 indicating the degree to which the document meets the qualification criteria.
    """
    score = text_scoring(qualified_terms, freq_dist, qualification)
    return score
