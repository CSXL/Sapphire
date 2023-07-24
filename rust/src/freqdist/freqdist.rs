
use std::collections::HashMap;

/// Calculates the frequency distribution of words in the given text.
///
/// # Arguments
///
/// * `words` - An array of words to calculate the frequency distribution for.
/// * `text` - The text in which the frequency distribution should be calculated.
///
/// # Returns
///
/// A `HashMap` containing the word-frequency pairs.
pub fn freq_dist<'a, T: AsRef<str>>(words: &'a [T], text: &'a str) -> HashMap<&'a str, usize> {
    // Create an empty HashMap to store the frequency distribution.
    let mut freq_map: HashMap<&str, usize> = HashMap::new();

    // Iterate over each word in the provided array.
    for word in words {
        // Convert the word to a string reference.
        let word_ref = word.as_ref();

        // Count the number of matches for the current word in the text and add it to the frequency map.
        *freq_map.entry(word_ref).or_insert(0) += count_matches(text, word_ref);
    }

    // Return the frequency map.
    freq_map
}

/// Counts the number of occurrences of a word in a given text.
///
/// # Arguments
///
/// * `text` - The text in which to count occurrences.
/// * `word` - The word to count occurrences of.
///
/// # Returns
///
/// The number of occurrences of the word in the text.
fn count_matches(text: &str, word: &str) -> usize {
    let mut count = 0;
    let mut start = 0;

    // Iterate over the text, finding occurrences of the word.
    while let Some(index) = text[start..].find(word) {
        // Increment the count for each occurrence.
        count += 1;
        start += index + word.len(); // Update the starting position for the next iteration.
    }

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_freq_dist() {
        let words = ["apple", "banana", "cherry"];
        let text = "apple banana cherry banana apple";
        let freq_map = freq_dist(&words, text);
        
        assert_eq!(freq_map.get("apple"), Some(&2));
        assert_eq!(freq_map.get("banana"), Some(&2));
        assert_eq!(freq_map.get("cherry"), Some(&1));
    }
}

