# Example Analysis Scripts for German Linguistics Research

This directory contains example scripts demonstrating state-of-the-art computational methods for German language research.

## Contents

### 1. Corpus Analysis
- `corpus_frequency_analysis.py` - Word frequency and n-gram analysis
- `collocation_extraction.R` - Statistical collocation extraction
- `concordance_search.py` - KWIC concordance generation

### 2. Dialect Analysis
- `dialect_classification.py` - Machine learning dialect classifier
- `acoustic_analysis.praat` - Praat script for formant extraction
- `dialectometry.R` - Distance-based dialect analysis

### 3. Register Analysis
- `register_features.py` - Automated register feature extraction
- `mda_analysis.R` - Multidimensional analysis
- `text_classification.py` - Register classification with ML

### 4. SLA Analysis
- `learner_corpus_analysis.py` - Error analysis and proficiency measures
- `caf_calculator.py` - Complexity, Accuracy, Fluency metrics
- `developmental_analysis.R` - Longitudinal growth curve modeling

## Requirements

### Python
```bash
pip install spacy pandas numpy scikit-learn matplotlib seaborn
pip install gensim nltk transformers torch
python -m spacy download de_core_news_lg
```

### R
```r
install.packages(c("tidyverse", "quanteda", "lme4", "ggplot2", 
                   "stringdist", "cluster", "mgcv", "sf"))
```

### Other
- Praat (for acoustic analysis)
- ELAN (for annotation)

## Usage

Each script includes:
- Detailed docstrings
- Example data format
- Expected output
- Visualization examples

See individual script headers for specific usage instructions.
