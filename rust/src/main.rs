mod transcription {
    pub mod transcription;
}
mod tokenization {
    pub mod tokenization;
}

mod abstractfunctions {
    pub mod arraymanipulations;
}
mod freqdist {
    pub mod freqdist;
}
mod tf_idf{
    pub mod tf_idf;
}
mod scoreevaluation{
    pub mod scoreevaluation;
}

use std::collections::HashMap;
use tf_idf::tf_idf::tf_idf;
use abstractfunctions::arraymanipulations;
use freqdist::freqdist::freq_dist;
use tokenization::tokenization::Tokenization;
use transcription::transcription::get_transcript;
use transcription::transcription::get_sent_tokens;
use scoreevaluation::scoreevaluation::evaluatescore;

const BASE_URL: &str = "http://localhost:8000";
const VIDEO_ID: &str = "bNu26dHGDtY";
#[tokio::main]
// Main function for processing transcript and calculating score

/// Asynchronous main function
async fn main() {
    // Get the transcript from a specified URL and video ID
    let transcript = get_transcript(BASE_URL.to_string(), VIDEO_ID.to_string()).await;

    // Tokenize the transcript
    let tokenizer = Tokenization {
        cleansed_transcript: transcript.to_string(),
    };
    let tokens = tokenizer.tokenize();

    // Get sentence tokens from a specified URL and video ID
    let sentence_tokens = get_sent_tokens(BASE_URL.to_string(), VIDEO_ID.to_string()).await;
    let sentence_tokens: Vec<&str> = sentence_tokens.iter().map(|s| s.as_str()).collect();

    // Purify the sentence tokens
    let sentence_tokens = arraymanipulations::purify_array(&sentence_tokens);

    match tokens {
        Ok(v) => {
            // Purify the tokens
            let tokens = arraymanipulations::purify_array(&v);

            // Calculate frequency distribution of tokens in the transcript
            let freq = freq_dist(&tokens, &transcript.as_str());

            // Convert tokens to Vec<String>
            let tokens: Vec<String> = tokens.iter().map(|s| s.to_string()).collect();
            let slice_string: &[String] = &tokens;

            // Convert sentence_tokens to Vec<String>
            let sentence_tokens: Vec<String> = sentence_tokens.iter().map(|s| s.to_string()).collect();
            let sentence_tokens: &[String] = &sentence_tokens;

            // Calculate TF-IDF matrix
            let tfidf_matrix = tf_idf(&tokens, &sentence_tokens);

            // Filter out NaN values from the TF-IDF matrix
            let tfidf_matrix: HashMap<String, f64> = tfidf_matrix
                .into_iter()
                .filter(|(_, v)| !v.is_nan())
                .collect();

            // Filter out numeric keys from the TF-IDF matrix
            let tfidf_matrix = tfidf_matrix
                .into_iter()
                .filter(|(k, _)| {
                    k.parse::<i64>().is_err() && k.parse::<f64>().is_err()
                })
                .collect::<HashMap<String, f64>>();

            // Evaluate the score using TF-IDF matrix and frequency distribution
            let score: f64 = evaluatescore(tfidf_matrix, freq);

            // Print the score
            println!("{}", score);
        }
        Err(e) => {
            println!("Error: {}", e);
            println!("The provided YouTube Video does not have enabled transcription");
        }
    }
}
