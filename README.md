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
    - 2.[Text pre-processing](#Text-pre-procesing)
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
* Sapphire needs to retrieve the content of a YouTube video.
* Raw transcript of the YouTube video is obtained using wrappers.
* The obtained raw transcript is sent for pre-processing.
* Pre-processing involves eliminating unnecessary elements such as timestamps, speaker labels, and noise from the transcript.
### Text pre-processing ###
In order to produce an accurate score for the YouTube video, the text has to be preprocessed/polished.This involves text cleaning, removal of special characters, and converting the text to lowercase for consistency. Next, the pre-processed text is tokenized into individual words or phrases in preparation for TF-IDF (Term Frequency-Inverse Document Frequency) analysis.The video length is also checked in order to determine how much of the transcript should be used. Based on the optimal bounds given, the most important part of the video in terms of the transcript is used for further evaluation, which is through vocabulary weighting.

### TF-IDF evaluators ###
TF-IDF (Term Frequency-Inverse Document Frequency) evaluation is a crucial part of the algorithm as it is being used for scoring YouTube videos based on their content. It involves assigning scores to words based on their contribution to the context of the text. Traditionally, TF-IDF is calculated using documents or transcripts from multiple sources to determine the Inverse Document Frequency (IDF) part of the score. However, in this algorithm, a simplified approach is used. Instead of using external documents, the algorithm performs lexical analysis on the transcript of the YouTube video itself. The process begins by tokenizing the pre-processed transcript into sentences. Then, the algorithm analyzes the words within these sentences. The words are scored based on their frequency (Term Frequency or TF) within the specific video's context, as well as their rarity (Inverse Document Frequency or IDF) within that transcript. This allows the algorithm to determine the weight or significance of each word in the given transcript. The TF-IDF scores assigned to the words are then used to determine their importance or contribution to the content of the video. Words with higher TF-IDF scores are considered more relevant and significant, while words with lower scores are considered less important. This helps the algorithm in evaluating YouTube videos based on the emphasis or relevance of their content in a specific context, as determined by the TF-IDF evaluation.

### Score Assessment ###
In the evaluation process, the second most crucial step is the implementation of an assessor. This assessor is responsible for filtering out words based on their TF-IDF score, the measure of word importance in a document when compared to a corpus of other documents. The TF-IDF method used here is made efficient as it is being pre processed through tokenizing docs into sentences. The assessor sets an average standard for the word weight score. This means that words with a score higher than the average will be retained, while those with a score equal to or lower than the average will be filtered out. This average serves as a threshold for determining which words are considered valuable and which are unnecessary. The Keyword Qualifier, as part of the ranking process, plays a vital role in establishing this average standard. It ensures that only words that meet or exceed the set average score are considered for further analysis, while those below the average are filtered out. This approach is important because it helps eliminate unnecessary words from consideration, allowing the scoring process to focus only on words that carry value. By filtering out words with lower scores, the assessing process can prioritize those words that are more relevant and informative in the context of the task at hand, such as keyword ranking for search engine optimization or text classification for information retrieval. In summary, the implementation of an assessor with a Keyword Qualifier that sets an average standard for the TF-IDF score and filters out words based on this threshold is a crucial step in the whole process. It helps ensure that only valuable words are considered, leading to more accurate and relevant calculations.
 
## Current Status
The current status of the package is that it is undergoing MVP (Minimum Viable Product) development. The evaluations are currently being optimized to enhance performance. Notably, Sapphire now possesses the capability to evaluate transcripts of video lengths up to one day in mere seconds.
