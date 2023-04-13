from EvaluationFunction import *
def InformationalRetrievalRank(qualified_terms,freq_dist,qualification):
    score = text_scoring(qualified_terms,freq_dist,qualification)
    return score