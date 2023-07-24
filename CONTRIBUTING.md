# Welcome to Sapphire

Thank you for joining us on the expedition of changing online education through Natural Language Processing.

## Table of Contents

- [Welcome to Sapphire](#welcome-to-sapphire)
  - [Table of Contents](#table-of-contents)
  - [Executive Summary](#executive-summary)
    - [Mission](#mission)
    - [Why Sapphire](#why-sapphire)
  - [Downloading, Testing, and Running](#downloading,-testing,-and-running)
    - [Environment Secrets](#environment-secrets)
    - [Running the Project](#building-and-running-the-project)
    - [Running Tests](#running-tests)
    - [Linting](#linting)
  - [Contributing](#contributing)
    - [Code of Conduct](#code-of-conduct)
    - [Contributing Guidelines](#contributing-guidelines)
    - [Types of Contributions](#types-of-contributions)
    - [How to Contribute](#how-to-contribute)
  - [Thank You](#thank-you)

## Executive Summary

### Mission

To automate the process of creating a project from requirements.

### Why Sapphire

These are the areas where Sapphire can change the online learning scene for researchers.

For CSX Labs' core values please refer to our [Business Plan](https://docs.google.com/document/d/1PhPFI1YXRd-XHMvfvRZhFwnqzzdXLTcpo0Kmbw803-I/edit?usp=sharing).

- **Topic Rigor Ranking:** Sapphire ranks YouTube Videos with transcription enabled based on comprehensiveness and how much variety of information is offered. By focusing on how much vocabulary is utilised in the context of the video, Sapphire is able to determine the granularity of a YouTube Video.
- **Efficiency:**
  Sapphire harnesses the power of advanced algorithms, such as Aho-Corasick, TF-IDF evaluation (with additive smoothing), and transcript fragmentation, to optimize efficiency and accuracy. These algorithms are essential components of Sapphire's codebase, providing developers with powerful tools to enhance performance and generate reliable results.

  Aho-Corasick algorithms are utilized to efficiently perform string matching, enabling the determination of the significance of specific vocabulary within a given corpus, which, in the case of Sapphire, is the transcript. This facilitates the extraction of relevant information and contributes to the overall accuracy of the cumulative result.

  The incorporation of additive smoothing in TF-IDF evaluation is another crucial aspect of Sapphire. This technique allows for the calculation of weighted words in a  
   transcript across a wide range of corpuses, accommodating various linguistic patterns and enhancing the model's adaptability to different data sources. By employing
  additive smoothing, Sapphire ensures consistent and robust results for developers working with diverse textual data.

  Transcript fragmentation is an additional feature provided by Sapphire. It offers developers the capability to select a partial amount of sentence tokens based on the
  complexity of the sentences. The granularity of the corpus determines the level of detail and precision achievable through transcript fragmentation. This functionality
  enhances the flexibility of Sapphire, empowering developers to tailor the analysis to their specific requirements and optimize resource usage.

  By integrating these powerful algorithms, Sapphire streamlines time complexity, enabling efficient processing and delivering accurate cumulative results.

- **Learning convenience:**
  Sapphire provides researchers with a more comprehensive selection of resources, facilitating access to a diverse array of content from various platforms. However, it is important to note that while platforms like YouTube offer valuable information, they may not always meet the rigorous standards required in academic or professional settings.

## Downloading, Testing and, Running

### Environment Secrets

Create a [Google Cloud Platform](https://cloud.google.com/) account and then create an [YouTube Transcript API](https://developers.google.com/youtube/v3/docs/captions) and set it as an environment variable named `api_key`.

You can also set the environment variables in a `.env` file in the root of the project. The `.env` file is ignored by git, so you can safely store your API key in it.

We are not responsible for any charges incurred by your Google Cloud accounts.

### Downloading the Project

To Download the project, you will need to have [Python](https://www.python.org/) and [Make](https://www.gnu.org/software/make/) installed if you are using the general version. However, there is a specific implementation in [Rust](https://www.rust-lang.org/) available inside the [rust](rust) folder.

To download dependencies for the project, run `make download`.This will install all the resources needed for Sapphire to run for both the Python and Rust version

### Running Tests

Run `make test` to run all the unit tests in the project. We are using the [unittest](https://docs.python.org/3/library/unittest.html) package of python in order to perform the unit tests.

### Linting

Linting is done with [trunk](https://trunk.io), there are common IDE plugins for it. The binary is provided in the repo, so you can run `./trunk fmt` (`make lint`) or `./trunk fmt --all` to lint the project. In order to lint the files in the codebase, run `make link`, then `make check` to check the linting.
If you are using the Rust version, we are using [Clippy](https://doc.rust-lang.org/nightly/clippy/) to lint the source code. Ultimately, the command remains the same.
### Running the project(Python)
Run `make run` to execute the project for a specific YouTube video by passing the Video ID into the [Sapphire](sapphire.py) function.

### Running the project(Rust)
Open up two terminal windows to run the python server, which will be used for tokenization and lexical analysis, and another window for running the main program. On one terminal window, enter the command `make run_server` and on the other window, enter the command `make run_main`.
## Contributing

### Code of Conduct

We have a [Code of Conduct](CODE_OF_CONDUCT.md) that we expect all contributors to follow. Please read it before contributing.

Please report unacceptable behavior to [opensource@csxlabs.org](mailto:opensource@csxlabs.org).

### Contributing Guidelines

If you have any questions about our code of conduct, guidelines, or operation, feel free to reach out to us at [opensource@csxlabs.org](mailto:opensource@csxlabs.org).

### Types of Contributions

We welcome contributions of all kinds. Here are some examples of the types of contributions we are looking for:

- **Code:** Found a bug, want to fill a TODO, or want to enhance our operation? File an issue with a pull request and our open source team will review your changes. If you need help setting up the project or have any questions about the codebase, feel free to reach out to us at [opensource@csxlabs.org](mailto:opensource@csxlabs.org).
- **Documentation:** Have you found a typo in the documentation? Do you have a suggestion for improving the documentation? We would love to hear from you! Feel free to open an issue and/or pull request with your changes.
- **Logic:** If you have any suggestions for improving the project's logic and algorithms, feel free to open an issue and/or pull request with your methods and reasoning.

### How to Contribute

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the repository.
2. [Open an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) describing the changes you would like to make. If you are not sure if your changes are necessary, feel free to open an issue and ask us.
3. If you want to make changes to the repository, [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) and reference it in your issue. If you are not sure how to make the changes, feel free to open a pull request with your proposed changes and ask us for feedback.

## Thank You

Thank you for taking the time to read this document. We hope you enjoy using Sapphire and that it helps you in your work. If you have any questions, comments, or concerns, feel free to reach out to us at [opensource@csxlabs.org](mailto:opensource@csxlabs.org). If you have any business inquiries about Solus or CSX Labs, fill out our [contact form](https://csxlabs.org/#contact) or email us at [info@csxlabs.org](mailto:info@csxlabs.org).
