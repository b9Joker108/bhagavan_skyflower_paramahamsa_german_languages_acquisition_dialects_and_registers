# Contributing Guidelines

Thank you for your interest in contributing to this repository! This document provides guidelines for contributing to the German Language Acquisition, Dialects, and Registers SOTA Methodologies repository.

## Ways to Contribute

### 1. Adding New Methodologies
- Document emerging state-of-the-art approaches
- Include theoretical background and practical applications
- Provide code examples where applicable
- Cite relevant sources

### 2. Updating Bibliography
- Add recent publications (last 5 years preferred)
- Include DOIs or stable URLs when available
- Follow existing citation format
- Organize by relevant section

### 3. Sharing Code Examples
- Provide working, documented code
- Include installation requirements
- Add example data or data format specifications
- Follow language-specific best practices

### 4. Proposing Case Studies
- Document real-world applications of methodologies
- Include dataset descriptions and analysis procedures
- Share reproducible results
- Discuss limitations and lessons learned

### 5. Improving Documentation
- Fix typos and grammatical errors
- Clarify unclear explanations
- Add missing information
- Improve code comments

## Contribution Process

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/bhagavan_skyflower_parmahamsa_german_languages_acquisition_dialects_and_registers.git
cd bhagavan_skyflower_parmahamsa_german_languages_acquisition_dialects_and_registers
```

### Step 2: Create a Branch

```bash
# Create a descriptive branch name
git checkout -b add-neural-network-dialectology
# or
git checkout -b update-sla-bibliography
# or
git checkout -b fix-typo-in-corpus-docs
```

### Step 3: Make Your Changes

Follow the structure and style of existing content:

#### For Methodology Documents
```markdown
# Methodology Name

## Overview
Brief description of the methodology

## Theoretical Background
Foundational concepts and theories

## Methods
Detailed procedures and techniques

## Implementation
Code examples and practical guidance

## Applications
Real-world use cases

## References
Relevant citations
```

#### For Code Examples
```python
#!/usr/bin/env python3
"""
Brief description of what the script does.

This script demonstrates [methodology/technique] for [purpose].
Requires: [dependencies]
"""

# Clear imports
import necessary_libraries

# Well-documented functions
def main_function():
    """
    Clear docstring explaining:
    - Purpose
    - Parameters
    - Returns
    - Example usage
    """
    pass

# Example usage
if __name__ == "__main__":
    # Demonstrate functionality
    pass
```

### Step 4: Test Your Changes

- Verify all links work
- Test code examples
- Check formatting (Markdown preview)
- Ensure proper citation format

### Step 5: Commit Your Changes

```bash
# Add your changes
git add .

# Write a clear commit message
git commit -m "Add deep learning methods for dialect classification

- Added new section on transformer-based models
- Included code example with BERT fine-tuning
- Updated bibliography with recent papers"
```

### Step 6: Push and Create Pull Request

```bash
# Push to your fork
git push origin your-branch-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Detailed description of what was added/changed
- Reference to any related issues
- Screenshots if applicable (for documentation changes)

## Style Guidelines

### Markdown Formatting

- Use ATX-style headers (`# Header`)
- Include blank lines between sections
- Use code fences with language specification
- Indent nested lists properly

### Code Style

#### Python
- Follow PEP 8
- Use meaningful variable names
- Include docstrings for functions and classes
- Add type hints where helpful

```python
def extract_features(text: str) -> dict:
    """
    Extract linguistic features from German text.
    
    Args:
        text: Input German text string
        
    Returns:
        Dictionary of extracted features
    """
    pass
```

#### R
- Follow tidyverse style guide
- Use snake_case for variables
- Comment complex operations
- Load libraries at the top

```r
# Load required libraries
library(tidyverse)
library(quanteda)

# Extract collocation patterns
extract_collocations <- function(corpus, min_count = 5) {
  # Implementation
}
```

### Citations

Use APA format:

```
Author, A. A. (Year). Title of work. Publisher.
Author, A. A., & Author, B. B. (Year). Title of article. 
    Journal Name, volume(issue), pages. https://doi.org/...
```

## Content Guidelines

### Quality Standards

✅ **Include:**
- State-of-the-art, current methodologies
- Peer-reviewed sources
- Reproducible examples
- Clear explanations
- Practical applications

❌ **Avoid:**
- Outdated methods without historical context
- Non-academic or unreliable sources
- Overly complex examples without explanation
- Opinions without supporting evidence
- Plagiarism (always cite sources)

### Language

- Write in clear, academic English
- Define technical terms on first use
- Use active voice when possible
- Be concise but comprehensive
- Include examples to illustrate concepts

### Code Examples

- Must be functional and tested
- Include comments explaining logic
- Specify required dependencies
- Show expected output
- Handle common errors gracefully

## Repository Structure

When adding new content, place files in appropriate directories:

```
docs/
├── methodologies/           # Methodology documents
│   ├── corpus_linguistics.md
│   ├── dialectology.md
│   ├── register_analysis.md
│   └── sla_frameworks.md
├── examples/               # Code examples
│   ├── README.md
│   ├── corpus_analysis/
│   ├── dialect_analysis/
│   └── register_analysis/
├── data/                   # Data documentation
│   └── DATA_COLLECTION.md
└── BIBLIOGRAPHY.md        # References
```

## Review Process

1. **Automated Checks**: Pull requests will be checked for:
   - Markdown formatting
   - Broken links
   - File organization

2. **Manual Review**: Maintainers will review for:
   - Content accuracy
   - Relevance to repository scope
   - Code functionality
   - Documentation quality

3. **Feedback**: You may be asked to:
   - Clarify explanations
   - Add missing information
   - Fix formatting issues
   - Update citations

4. **Approval**: Once approved, your contribution will be merged!

## Code of Conduct

### Expected Behavior

- Be respectful and inclusive
- Provide constructive feedback
- Accept criticism gracefully
- Focus on what is best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other unprofessional conduct

## Questions or Need Help?

- Open an issue for questions about methodology or content
- Tag issues appropriately (`question`, `enhancement`, `bug`)
- Be specific and provide context
- Check existing issues first to avoid duplicates

## Recognition

Contributors will be acknowledged in:
- Repository README (significant contributions)
- Commit history (all contributions)
- Release notes (version updates)

## License

By contributing, you agree that your contributions will be licensed under the same GNU General Public License v3.0 that covers the project.

## Additional Resources

### Learning Resources
- [Markdown Guide](https://www.markdownguide.org/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Tidyverse Style Guide](https://style.tidyverse.org/)

### Relevant Standards
- [FAIR Data Principles](https://www.go-fair.org/fair-principles/)
- [CLARIN Standards](https://www.clarin.eu/content/standards)
- [TEI Guidelines](https://tei-c.org/guidelines/)

---

Thank you for contributing to advancing research in German linguistics!
