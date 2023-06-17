# Sapphire

![Project Logo](IMG-9758.jpg)



## Table of Contents

- [Sapphire](#Sapphire)
  - [Table of Contents](#table-of-contents)
  - [Mission](#Mission)
  - [Resources](#Resources)
  - [Overview](#Overview)
  - [Why?](#Why?)
  - [Requirements](#Requirements)
    - 1.[YouTube transcription](#YouTube-transcription)
    - 2.[Text pre-processing](#Text pre-procesing)
    - 3.[TF-IDF evaluators](#TF-IDF-evaluators)
    - 4.[Keyword Qualifiers](#Keyword-Qualifiers)
   - [Current Status](#Current-Status)



## Mission

To score YouTube videos based on information rigor.


## Resources
Interested in contributing to or testing this project? Check out our [contributing guide](CONTRIBUTING.md).


## Overview

 Sapphire is an innovative open source tool that leverages TF-IDF scoring and frequency distributions to score transcripts of a YouTube video. By analyzing the statistics of important words in the transcript, Sapphire is able to determine the depth and Emphasis covered in a video, making it an effective evaluation system for YouTube videos. This unique tool aims to bridge the gap between text scoring and token analysis, offering a powerful solution for content creators and researchers alike. 


## Why?

There are several commonly used algorithms and software packages that utilize Natural Language Processing (NLP) scoring techniques to sequence and score YouTube videos. However, many of these algorithms do not take into consideration important factors, such as the weightage of vocabulary in the video's transcript, when determining the level of emphasis provided. Currently, YouTube primarily relies on the "watch time" algorithm, which considers viewership statistics to score videos. While this algorithm is useful for determining based on video popularity, it is not designed to assess comprehensiveness. Therefore, there is a need for an algorithm that can analyze video content and accurately determine the level of emphasis based on factors such as vocabulary richness and depth of the transcript to evaluate a YouTube video.

## Requirements
Vision: An algorithm that scores YouTube videos based on information rigor

 ### Youtube transcription ###
 Sapphire needs to retrieve the content of a YouTube video. Here are the steps below of how it is performed.
* Raw transcript of the YouTube video is obtained using wrappers such as [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/).
* The obtained raw transcript is sent for pre-processing for refinement.
* Pre-processing involves eliminating unnecessary elements such as timestamps, speaker labels, and noise from the transcript.
### Text pre-processing ###
* To produce an accurate score for the YouTube video, the text needs to undergo preprocessing and polishing.
* The preprocessing involves cleaning the text by removing special characters and converting it to lowercase for consistency.
* After preprocessing, the text is tokenized into individual words or phrases to prepare for TF-IDF (Term Frequency-Inverse Document Frequency) analysis.
* In addition to text processing, the length of the video is checked to determine the portion of the transcript that should be used.
* Based on the optimal bounds provided, the most important part of the video's transcript is selected for further evaluation.
* The selected portion of the transcript is then subjected to vocabulary weighting to assess its significance and impact.
### TF-IDF evaluators ###
TF-IDF (Term Frequency-Inverse Document Frequency) evaluation is a crucial part of the algorithm for scoring YouTube videos based on their content.TF-IDF involves assigning scores to words based on their contribution to the context of the text.
* Traditionally, TF-IDF is calculated using documents or transcripts from multiple sources to determine the Inverse Document Frequency (IDF) part of the score.
* In this algorithm, a simplified approach is used by performing lexical analysis on the transcript of the YouTube video itself.
* The process begins by tokenizing the pre-processed transcript into sentences.
* The algorithm analyzes the words within these sentences and scores them based on their frequency (Term Frequency or TF) within the specific video's context.
* The words are also scored based on their rarity (Inverse Document Frequency or IDF) within that transcript.
* This allows the algorithm to determine the weight or significance of each word in the given transcript.
* TF-IDF scores assigned to the words are used to determine their importance or contribution to the content of the video.
* Words with higher TF-IDF scores are considered more relevant and significant.
* Words with lower scores are considered less important.
* TF-IDF evaluation helps in evaluating YouTube videos based on the emphasis or relevance of their content in a specific context.
### Score Assessment ###
* The evaluation process comprises several steps, and the second most crucial step involves the meticulous implementation of an assessor.
* The primary role of the assessor is to filter out words based on their TF-IDF (Term Frequency-Inverse Document Frequency) score, a metric that quantifies the importance of a word in a document relative to a corpus of other documents.
* To enhance the efficiency of the TF-IDF method, the documents undergo preprocessing by means of tokenization, which involves splitting them into individual sentences.
* The assessor establishes an average standard for the word weight score, acting as a threshold for determining which words are deemed valuable and which ones are deemed unnecessary.
* Words with a score higher than the average are retained for further analysis, while those with a score equal to or lower than the average are discarded.
* The Keyword Qualifier plays a vital role in the ranking process by aiding in the determination of the average score.
* The Keyword Qualifier ensures that only words meeting or surpassing the average score are considered for further analysis, while words below the average are eliminated from consideration.
* This approach is highly significant as it systematically eliminates superfluous words, enabling the scoring process to concentrate solely on words that possess value and relevance.
* By excluding words with lower scores, the assessing process can prioritize words that are more pertinent and informative within the context of the given task, such as keyword ranking for search engine optimization or text classification for information retrieval.
* To summarize, the meticulous implementation of an assessor, incorporating a Keyword Qualifier that sets an average standard for the TF-IDF score and filters out words based on this threshold, constitutes a critical step in the evaluation process.
* This step ensures that only words of substantive value are considered, thereby resulting in more precise, accurate, and relevant calculations. 
## Current Status
The current status of the package is that it is undergoing MVP (Minimum Viable Product) development. The evaluations are currently being optimized to enhance performance. Notably, Sapphire now possesses the capability to evaluate transcripts of video lengths up to one day in mere seconds.
