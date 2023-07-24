use std::collections::HashMap;

pub fn evaluatescore<'a>(tfidf: HashMap<String, f64>, freqdist: HashMap<&'a str, usize>) -> f64 {
    let mut num: f64 = 0.0;

    // Iterate over each key-value pair in the tfidf HashMap
    for (key, value) in &tfidf {
        // Get the frequency from the freqdist HashMap using the key as a string
        let floatfrmt: f64 = *freqdist.get(key.as_str()).unwrap() as f64;

        // Multiply the tfidf value with the frequency and accumulate the sum
        num += value * floatfrmt;
    }

    // Calculate the denominator as the length of the tfidf HashMap
    let den = tfidf.len() as f64;

    // Calculate the ratio by dividing the numerator by the denominator
    let ratio = num / den;

    // Return the ratio as the final score
    ratio as f64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_evaluatescore() {
        let mut tfidf: HashMap<String, f64> = HashMap::new();
        tfidf.insert(String::from("apple"), 0.5);
        tfidf.insert(String::from("banana"), 0.8);
        tfidf.insert(String::from("cherry"), 0.3);

        let mut freqdist: HashMap<&str, usize> = HashMap::new();
        freqdist.insert("apple", 2);
        freqdist.insert("banana", 3);
        freqdist.insert("cherry", 1);

        let score = evaluatescore(tfidf, freqdist);
        println!("im looking for {}",score);
        assert_eq!(score, 1.2333333333333334);
    }
}
