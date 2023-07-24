use std::collections::{HashMap, HashSet};

pub fn tf_idf(tokens: &[String], sentences: &[String]) -> HashMap<String, f64> {
    // Get the number of documents (sentences)
    let num_docs = sentences.len();

    // Create a set of unique tokens
    let tokens_set: HashSet<&str> = tokens.iter().map(|s| s.as_str()).collect();

    // Get the total count of tokens and the count of unique tokens
    let tokens_len = tokens.len();
    let tokens_set_len = tokens_set.len();

    // Calculate term frequency (tf) for each token in each sentence
    let term_freq: HashMap<String, Vec<usize>> = tokens_set
        .iter()
        .map(|&token| {
            let token_freqs: Vec<usize> = sentences
                .iter()
                .map(|sentence| sentence.split_whitespace().filter(|&w| w == token).count())
                .collect();
            (token.to_string(), token_freqs)
        })
        .collect();

    // Calculate document frequency (df) for each token
    let doc_freq: HashMap<&str, usize> = term_freq
        .keys()
        .map(|token| {
            let doc_freq_count = term_freq[token].iter().filter(|&&f| f > 0).count() + 1;
            (token.as_str(), doc_freq_count)
        })
        .collect();

    // Calculate TF-IDF scores for each token
    let mut tf_idf_scores: HashMap<String, f64> = HashMap::new();
    for (token, freqs) in term_freq.iter() {
        let doc_freq_count = doc_freq[token.as_str()];
        let tf_idf_score = freqs
            .iter()
            .enumerate()
            .fold(0.0, |acc, (i, &freq)| {
                // Calculate term frequency (tf)
                let tf = (freq + 1) as f64 / (tokens_len + tokens_set_len) as f64;
                // Calculate inverse document frequency (idf)
                let idf = (num_docs + 1) as f64 / (doc_freq_count as f64 + 1.0).ln();
                acc + tf * idf
            });
        tf_idf_scores.insert(token.to_string(), tf_idf_score);
    }

    tf_idf_scores
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tfidf() {
        let tokens = vec![
            String::from("apple"),
            String::from("banana"),
            String::from("cherry"),
        ];
        let sentences = vec![
            String::from("apple banana apple"),
            String::from("banana cherry"),
            String::from("cherry apple"),
        ];

        let tfidf_scores = tfidf(&tokens, &sentences);

        // Verify tf-idf scores for specific tokens
        println!("{:#?}",tfidf_scores.get("cherry"));
        assert_eq!(tfidf_scores.get("apple"), Some(&2.8853900817779268));
        assert_eq!(tfidf_scores.get("banana"), Some(&2.404491734814939));
        assert_eq!(tfidf_scores.get("cherry"), Some(&2.404491734814939));
    }
}
