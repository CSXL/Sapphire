
# Sapphire

Sapphire is a NLP based model that ranks transcripts from a given YouTube video with the help of TFIDF scores from a single trancript.


# Mission

To improve ranking results for educational purposes
# Vision

Create a smarter world where the best sources are provided to users

## table of contents
    1.Why?
    2.Overview
    3.How it works(shallow)?
    5.How it works(in-depth)?
    4.Requirements/Dependencies
    5.Installations
    6.current status

# Why?

The standard method used for ranking YouTube Videos, which is "watch time" (ratio of how much of the video is watched to the total video length) is insufficient to determine how great the source is based on the covered content. This python/cython based algorithm performs an in depth analysis to evaluate what content is being analysed and its quantity using lexical analysis and informational retrieval to ultimately provide more sophisticated ranking.

# How it works(simple)?

When provided with a YouTube video transcript performs various text processing tasks using several Python libraries including NLTK, spaCy, and scikit-learn.


The tasks include:

1.Tokenizing the input text into individual words and sentences

2.Removing stop words and custom stop words from the tokenized words

3.Removing specific words such as pronouns and common nouns

4.Generating string representations of numbers from 0 to 9999 for eliminating numerical stopwords

5.Creating a frequency distribution of the remaining words

6.Calculating the term frequency-inverse document frequency (tf-idf) values of the sentences in the input text

7.Using an Aho-Corasick automaton to search for certain patterns in the input text

8.The code also defines several functions to perform these tasks and prints out some of the results.

# How it works(in-depth)?

## Documentation

[Documentation](https://linktodocumentation)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Appendix

Any additional information goes here

