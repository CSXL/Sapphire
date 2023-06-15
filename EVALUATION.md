# Standards Rubric

- [ ] Documentation
  - [ ] README.md
    - [x] Name
    - [ ] Brief Description - Needs a tagline or brief description of the project. Can copy over from the project's description.
    - [ ] User Setup Instructions (if applicable)
    - [ ] Overview of the project
      - [x] Mission & Vision
      - [x] Problem & Solution
      - [x] Functionality
      - [x] Purpose
      - [x] Current State or Future Directions
      - [ ] Take long paragraphs and break them up into bullet points
      - [ ] Run text through a grammer checker
    - [ ] Links to any relevant documentation
    - [ ] Contact information for the project's maintainer(s) - srujanm@csxlabs.org
  - [ ] REQUIREMENTS.md
    - [ ] Mission & Vision
    - [ ] Functional Requirements
    - [ ] Non-Functional Requirements
    - [ ] Technical Requirements
    - [ ] Security Requirements
  - [ ] CONTRIBUTING.md
    - [ ] Developer Setup Instructions
    - [ ] Contributing Instructions
    - [ ] Project Structure
    - [ ] Project-Specific Standards and Practices
      - [ ] Code-Style
      - [ ] Documentation
      - [ ] Code-Review Process
      - [ ] Project Management
    - [ ] Contact information for the project's maintainer(s)
    - [ ] Link to the code of conduct - You can copy Solus.
  - [ ] Code of Conduct
- [ ] Code Standards
  - [ ] Testing - [Test Output](test_results.txt)
    - [x] Unified test suite
    - [ ] HTTP Endpoints are mocked and tested
    - [x] User-facing interfaces are tested
  - [ ] Static Analysis Tools - [Lint Output](static_analysis.txt)
    - [x] Linters
    - [x] Formatters
    - [ ] Checks Pass
  - [x] Inline documentation for all user-facing interfaces
  - [ ] Idiomatic practices of the language are followed - This will be filled once the static analysis passes.
    - [x] Opinionated style guide or philosophy is followed
    - [x] Appropriately used design patterns and language features
  - [x] Version control system is used
  - [ ] CI/CD pipeline
    - [ ] Static Analysis
    - [ ] Unit Testing
    - [ ] Release (when applicable)
  - [ ] Release system
    - [ ] Single command
    - [ ] Linked to an action such as a push to a branch or a pull request
    - [ ] Semantic versioning
  - [ ] Environments
    - [ ] Seperation of development and production environments
    - [ ] Secure storage of credentials and data
  - [x] Security
    - [x] No exposed or hard-coded credentials
    - [x] No severley outdated dependencies

## Report

README.md is mostly good, though there needs to be a seperation of concerns from the README.md and a seperate REQUIREMENTS.md. You also need a tagline or small description of your project (which you can copy from the GitHub description). The large paragraphs have to be broken up into bullet points that have depth but brevity. Also, run your bullet points (when created) through a grammar checker. Imagine you are selling your project to someone.

There needs to be a CONTRIBUTING.md and CODE_OF_CONDUCT.md (you can copy the code of conduct from Solus). The CONTRIBUTING.md should have all the instructions required to setup your project on ANY environment.

There needs to be a makefile with all the scripts needed to run, build, and maintain your project.

Tests fail due to two reasons:

- No documented specific configuration specs, inconsistant dependencies from project and requirements.txt
- HTTP mocking is not implemented in some modules.
  You can see the full test output in [test_results.txt](test_results.txt).

Linting throws many errors, all listed in [static_analysis.txt](static_analysis.txt).

There needs to be some export mechanism for exposing and hiding user and non-user related interfaces.

We'll discuss CI/CD pipelines and releases when all of the above are fixed.

## Evaluation Checksum

Lines 1-83

SHA256:ecaca514ef37aed91759095ffc4460a91ef8b41282c871462bcd6a4fabfddb9f
