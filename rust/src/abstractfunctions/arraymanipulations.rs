

pub fn purify_array<T: Eq + Copy>(arr: &[T]) -> Vec<T> {
    // Create a new empty vector to store the purified elements
    let mut result = Vec::new();

    // Iterate over each element in the input array
    for &elem in arr {
        // Check if the element is already present in the result vector
        if !result.contains(&elem) {
            // If the element is not present, add it to the result vector
            result.push(elem);
        }
    }

    // Return the purified vector
    result
}

#[test]
fn test_purify_array() {
    // Test case with repeated elements
    let arr = [1, 2, 2, 3, 4, 4, 4, 5];
    let expected = vec![1, 2, 3, 4, 5];
    assert_eq!(purify_array(&arr), expected);

    // Test case with no repeated elements
    let arr = [1, 2, 3, 4, 5];
    let expected = vec![1, 2, 3, 4, 5];
    assert_eq!(purify_array(&arr), expected);

    // Test case with a single element
    let arr = [1];
    let expected = vec![1];
    assert_eq!(purify_array(&arr), expected);

    // Test case with an empty array
    let arr: [i32; 0] = [];
    let expected: Vec<i32> = vec![];
    assert_eq!(purify_array(&arr), expected);
}
