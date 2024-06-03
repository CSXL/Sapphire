from typing import List, Tuple

from TokenSatisfaction.AbstractFunctions import average_td_idf_score, freq_dist
from TokenSatisfaction.EvaluationFunction import get_n_val, get_top_n


class KeywordQualification:
    def __init__(self, tokens: List[str], tf_idf_scores: List[float]):
        """
        To evaluate the keywords that qualify for further score calculation, follow these steps.

        Args:
        ----
            tokens: A list of tokens.
            tf_idf_scores: A list of term-document IDF scores.

        """
        self.freq_dist = freq_dist(tokens)
        self.qualification = self.get_qualification(tf_idf_scores)
        self.qualified_terms = self.get_qualified_terms(tf_idf_scores)

    def get_qualification(self, tf_idf_scores: List[float]) -> float:
        """
        Follow the given procedure to return the qualification threshold based on the average term-document IDF score.

        Args:
        ----
            tf_idf_scores: A list of term-document IDF scores.

        Returns:
        -------
            The nth highest term-document IDF score, where n is the average term-document IDF score.

        """
        avg_td_idf_score = average_td_idf_score(tf_idf_scores)
        return get_n_val(avg_td_idf_score, tf_idf_scores)

    def get_qualified_terms(
        self, tf_idf_scores: List[float]
    ) -> List[Tuple[str, float]]:
        """
        Returns the top terms based on their term-document IDF score.

        Args:
        ----
            tf_idf_scores: A list of term-document IDF scores.

        Returns:
        -------
            A list of tuples, where each tuple contains a term and its corresponding term-document IDF score.

        """
        return get_top_n(tf_idf_scores, self.qualification)

    def show(self) -> Tuple[dict, float, List[Tuple[str, float]]]:
        """
        Here are the steps to obtain the frequency distribution, qualification threshold, and top qualified terms.
        Returns
        -------
            A tuple containing the frequency distribution (dict), qualification threshold (float), and top terms (list of tuples).

        """
        return self.freq_dist, self.qualification, self.qualified_terms
