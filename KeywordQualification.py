from AbstractFunctions import *
from EvaluationFunction import *
  
class KeywordQualification:
    def __init__(self,tokens,tf_idf_score):
        self.freq_dist = freq_dist(tokens)
        self.qualification = get_n_val(average_td_idf_score(tf_idf_score),tf_idf_score)
        self.qualified_terms = get_top_n(tf_idf_score,self.qualification)
    def show(self):
        return (self.freq_dist,
        self.qualification,
        self.qualified_terms)