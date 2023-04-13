from AhoCorasick import *
from operator import itemgetter

def text_scoring(ranked_keywords,freq_dist,threshold_n):
  num = 0

  for word in ranked_keywords:
    key_for_freq_dist = get_closest_score_from_tfidf_dict(word,freq_dist)
    try:
      num += ranked_keywords[word]*freq_dist[key_for_freq_dist]
    except:
      continue
  return float(num/threshold_n)

def get_n_val(average_td_idf_score,score_json):
  count = 0
  for i in score_json:
    if score_json[i] >= average_td_idf_score:
      count += 1
  return count

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result