# Requirements

## 1. Introduction

The purpose of this document is to outline the requirements for Sapphire. It provides a comprehensive description of the project's objectives, functional and non-functional requirements, constraints, and any relevant assumptions.

## 2. Project Overview

Sapphire is an advanced Natural Language Processing (NLP) model designed to provide transcript ranking for YouTube videos using TF-IDF (Term Frequency-Inverse Document Frequency) scores derived from a single transcript. Its primary target audience comprises users seeking to assess the complexity levels of YouTube videos through transcription analysis.

## 3. Scope

The model is capable of evaluating videos with transcription enabled only and of english language only. The model consists of features such as YouTube transcription, Text preprocessing, TF-IDF evaluation and, score assessment. The model's English language capability allows for accurate evaluation of videos in English, ensuring reliable results for users relying on English transcripts.

## 4. Functional Requirements

### 4.1. YouTube transcription

[Provide a clear and concise description of the feature, including its purpose and any relevant user stories or scenarios.]

- Requirement 1: The system shall integrate with the [YouTube API](https://developers.google.com/youtube/v3/docs/captions) to retrieve video content for transcription
- Requirement 2: The transcription process shall handle variations in speech patterns, accents, and background noise to ensure accurate transcriptions..
- Requirement 3: The transcription output shall be time-aligned, associating each word or phrase with its corresponding timestamp in the video.
- Requirement 4: The system shall handle speaker diarization, distinguishing between multiple speakers in the video and attributing the transcribed text accordingly.
- ...

### 4.2. Text Preprocessing

[Provide a clear and concise description of the feature, including its purpose and any relevant user stories or scenarios.]

- Requirement 1: The scoring model shall tokenize the text, splitting it into individual words or tokens, considering language-specific rules and exceptions.
- Requirement 2: The system shall handle capitalization variations, applying techniques such as lowercasing or case normalization to ensure consistent processing and matching.
- Requirement 3: The scoring model shall remove commonly occurring words or stop words that do not contribute significantly to the overall meaning or scoring of the text.
- Requirement 4: The scoring model shall handle negation or polarity modifications, accounting for terms that change their meaning based on negations or intensifiers.
- ...

### 4.3. TF-IDF Evaluation

[Provide a clear and concise description of the feature, including its purpose and any relevant user stories or scenarios.]

- Requirement 1: The scoring model shall incorporate TF-IDF (Term Frequency-Inverse Document Frequency) as a feature evaluation technique.
- Requirement 2: The system shall calculate the term frequency (TF) for each term in the input text, representing the frequency of a term within a document.
- Requirement 3: The system shall calculate the inverse document frequency (IDF) for each term, representing the importance of a term across multiple documents.
- Requirement 4: The scoring model shall combine the TF and IDF values to generate a weighted score for each term, indicating its relevance and importance in the given text.
- Requirement 5: The system shall allow for customizable adjustments to the TF-IDF weighting scheme, enabling users to assign different weights or importance factors to specific terms or groups of terms.
- Requirement 6: TF-IDF (Term Frequency-Inverse Document Frequency) evaluation shall involve additive smoothing to work on a variety on transcripts.
- ...

### 4.3. Score Assessment

[Provide a clear and concise description of the feature, including its purpose and any relevant user stories or scenarios.]

- Requirement 1: The scoring model shall support weighted averages, allowing users to assign different weights or importance factors to each criterion.
- Requirement 2: The scoring model shall consider the relative importance of each criterion in the overall score assessment process.
- Requirement 3: The system shall allow users to define the criteria and their corresponding weights for score calculation and assessment.
- Requirement 4: The system shall provide flexibility in adjusting the criteria and their weights to accommodate changes in scoring requirements or domain-specific variations.
- Requirement 5: The scoring model shall generate an overall score based on the calculated averages, representing the comprehensive assessment of the input text across multiple dimensions.
- Requirement 6: The system shall present the individual criterion scores and the overall score to users in a clear and easily interpretable format.
- ...

## 5. Non-Functional Requirements

### 5.1. Accuracy and Precision

- Requirement 1: The NLP scoring model shall exhibit high accuracy in predicting and assigning scores to text data based on predefined criteria.
- Requirement 2: The model should demonstrate precise scoring capabilities, minimizing false positives and false negatives in its predictions.
- Requirement 3: The scoring model should be able to handle noisy or imperfect text data, applying appropriate preprocessing and normalization techniques to enhance accuracy.
- ...

### 5.2. Performance

- Requirement 1: The scoring model should provide rapid results for every transcript
- Requirement 2: The system should be able to handle a high volume of scoring requests concurrently, maintaining acceptable response times and performance.
- Requirement 3: The scoring model should demonstrate efficient resource utilization, minimizing computational and memory requirements for scoring operations.
- ...

### 5.3. Security

- Requirement 1: The system should incorporate appropriate security measures to protect API credentials such as the `api_key`.
- ...

## 6. Constraints

- Sapphire is currently only constrained to YouTube Videos with transcription enabled. It also can evaluate large scale transcripts relatively fast due to efficient algorithms but takes up to one minute at most.

## 7. Assumptions

- Sapphire operates under the assumption that the `videoID` parameter provided as input to the `sapphire` function is captioned.

## 8. Dependencies

- Sapphire relies on certain open-source modules and packages in order to successfully execute. The packages can be found in [requirements.txt](requirements.txt). Additionally, the algorithm depends on the [YouTube-captions-api](https://pypi.org/project/youtube-transcript-api/) and [YouTube-data-api](https://developers.google.com/youtube/v3/docs/videos).

## 9. Risks

- Exposing `API` credentials can pose significant risks to a program due to potential consequences arising from unauthorized access or misuse, especially in the event of pull requests being made.

## 10. Approval

- The requirements outlined in this document have been reviewed and approved by the following stakeholders for the development of the scoring model:

Approval signifies the acknowledgment and agreement that the documented requirements accurately capture the desired functionality, performance expectations, and security considerations of the scoring model. Any subsequent changes to the requirements will require re-evaluation and re-approval by the designated stakeholders.

Please ensure that all necessary stakeholders have reviewed and provided approval before proceeding with the implementation and deployment of `Sapphire`.
