from operator import itemgetter
from typing import Dict

from TokenSatisfaction.AhoCorasick import get_closest_score_from_tfidf_dict


def text_scoring(
    ranked_keywords: Dict[str, float], freq_dist: Dict[str, float], threshold_n: int
) -> float:
    """
    To calculate the text score using a given set of ranked keywords, frequency distribution, and threshold value, follow these instructions.

        Args:
        ----
            ranked_keywords: A dictionary mapping string keywords to float scores.
            freq_dist: A dictionary mapping string keywords to float frequency distributions.
            threshold_n: An integer threshold value for normalization.

        Returns:
        -------
            The calculated text score as a float.

    """
    # calculate the sum of scores weighted by frequency distribution
    num = 0
    for word in ranked_keywords:
        # get the closest key in freq_dist using the Levenshtein distance
        key_for_freq_dist = get_closest_score_from_tfidf_dict(word, freq_dist)
        try:
            num += ranked_keywords[word] * freq_dist[key_for_freq_dist]
        except KeyError:
            # if key is not in freq_dist, continue to next iteration
            continue

    # normalize the score by the threshold value and return as a float
    return float(num / threshold_n)


def get_n_val(average_td_idf_score: float, score_json: Dict[str, float]) -> int:
    """
    To obtain the count of terms in score_json that have a score greater than or equal to the average_td_idf_score, follow this instruction.

        Args:
        ----
            average_td_idf_score: A float representing the average TF-IDF score.
            score_json: A dictionary mapping string terms to float TF-IDF scores.

        Returns:
        -------
            An integer representing the number of terms with a score greater than or equal to average_td_idf_score.

    """
    count = 0
    for i in score_json:
        if score_json[i] >= average_td_idf_score:
            count += 1
    return count


def get_top_n(dict_elem: Dict[str, float], n: int) -> Dict[str, float]:
    """
    To obtain the top n elements from dict_elem based on their values, follow these instructions.

    Args:
    ----
        dict_elem: A dictionary mapping string keys to float values.
        n: An integer representing the number of elements to return.

    Returns:
    -------
        A dictionary mapping the top n keys with their values from dict_elem, sorted by descending value.

    """
    # sort the dictionary by descending value, then take the top n elements
    result = dict(sorted(dict_elem.items(), key=itemgetter(1), reverse=True)[:n])
    return result
