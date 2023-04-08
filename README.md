# Sapphire
Sapphire is a NLP based model that ranks transcripts from a given YouTube video with the help of TFIDF scores from a single trancript.
When provided with a YouTube video transcript performs various text processing tasks using several Python libraries including NLTK, spaCy, and scikit-learn.

The tasks include:

Tokenizing the input text into individual words and sentences
Removing stop words and custom stop words from the tokenized words
Removing specific words such as pronouns and common nouns
Generating string representations of numbers from 0 to 9999
Creating a frequency distribution of the remaining words
Calculating the term frequency-inverse document frequency (tf-idf) values of the sentences in the input text
Using an Aho-Corasick automaton to search for certain patterns in the input text
The code also defines several functions to perform these tasks and prints out some of the results.
