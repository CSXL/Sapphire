from typing import Dict

from TokenSatisfaction.LevensteinDistance import levenshtein_distance


def get_closest_score_from_tfidf_dict(
    key_from_tfidf: str, freq_dist_dict: Dict[str, float]
) -> str:
    """
    Follow the steps to return the closest key to key_from_tfidf in freq_dist_dict, based on the Levenshtein distance.

    Args:
    ----
        key_from_tfidf: A string key from a TF-IDF dictionary.
        freq_dist_dict: A dictionary mapping string keys to float frequency distributions.

    Returns:
    -------
        The closest key in freq_dist_dict to key_from_tfidf, based on the Levenshtein distance.

    """
    import ahocorasick

    # create an Aho-Corasick automaton from the keys in freq_dist_dict
    automaton = ahocorasick.Automaton()
    for key in freq_dist_dict.keys():
        automaton.add_word(key, key)
    automaton.make_automaton()

    # find the closest match for key_from_tfidf in the automaton
    closest_match = None
    closest_distance = float("inf")
    for _end_index, key in automaton.iter(key_from_tfidf):
        distance = levenshtein_distance(key, key_from_tfidf)
        if distance < closest_distance:
            closest_match = key
            closest_distance = distance

    return closest_match
