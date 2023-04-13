import ahocorasick
from LevensteinDistance import *
def get_closest_score_from_tfidf_dict(key_from_tfidf, freq_dist_dict):
    # create an Aho-Corasick automaton from the keys in freq_dist_dict
    automaton = ahocorasick.Automaton()
    for key, freq_dist in freq_dist_dict.items():
        automaton.add_word(key, (key, freq_dist))
    automaton.make_automaton()
    
    # find the closest match for key_from_tfidf in the automaton
    closest_match = None
    closest_distance = float('inf')
    for end_index, (key, freq_dist) in automaton.iter(key_from_tfidf):
        distance = levenshtein_distance(key, key_from_tfidf)
        if distance < closest_distance:
            closest_match = key
            closest_distance = distance
    
    return closest_match