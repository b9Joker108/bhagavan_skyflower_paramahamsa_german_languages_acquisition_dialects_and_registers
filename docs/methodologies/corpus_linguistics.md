# Corpus Linguistics Methodologies for German Language Research

## Overview

Corpus linguistics provides empirical, data-driven approaches to studying German language patterns, variation, and change. This document outlines state-of-the-art methodologies for corpus-based German linguistics research.

## Major German Corpora

### 1. Written Language Corpora

#### DeReKo (Deutsches Referenzkorpus)
- **Size**: >50 billion tokens
- **Coverage**: Written German from 1950s to present
- **Access**: COSMAS II web interface
- **Applications**: 
  - Lexicography
  - Grammar research
  - Historical linguistics

#### DWDS (Digitales Wörterbuch der deutschen Sprache)
- **Size**: >20 billion tokens
- **Coverage**: 20th and 21st century German
- **Features**: 
  - Time-based analysis
  - Word profiles
  - Collocation analysis
- **API**: Programmatic access available

### 2. Spoken Language Corpora

#### FOLK (Forschungs- und Lehrkorpus Gesprochenes Deutsch)
- **Size**: >300 hours of transcribed speech
- **Coverage**: Authentic everyday conversations
- **Annotation**: 
  - Prosodic features
  - Overlapping speech
  - Non-verbal elements
- **Format**: GAT (Gesprächsanalytisches Transkriptionssystem)

#### DGD (Datenbank für Gesprochenes Deutsch)
- **Platform**: Online database at IDS Mannheim
- **Contents**: Multiple spoken corpora
- **Tools**: Integrated query and analysis

### 3. Learner Corpora

#### FALKO (Fehlerannotiertes Lernerkorpus)
- **Size**: ~2 million tokens
- **Learner Groups**: 
  - L1 German
  - L2 German (various L1 backgrounds)
- **Annotation Layers**:
  - Error annotation
  - Target hypotheses
  - Grammatical categories

#### MERLIN
- **Focus**: CEFR-rated learner texts
- **Languages**: German, Italian, Czech
- **Levels**: A1-C2
- **Applications**: Proficiency assessment research

## Corpus Analysis Methods

### Frequency Analysis

#### Word Frequency
```python
from collections import Counter
import spacy

nlp = spacy.load("de_core_news_lg")

def get_word_frequencies(text):
    doc = nlp(text)
    words = [token.lemma_.lower() for token in doc 
             if not token.is_punct and not token.is_space]
    return Counter(words)

# Example usage
text = "Die Katze sitzt auf der Matte. Die Katze schläft."
freqs = get_word_frequencies(text)
print(freqs.most_common(5))
```

#### N-gram Analysis
- **Bigrams**: Two-word sequences
- **Trigrams**: Three-word sequences
- **Applications**: 
  - Collocation discovery
  - Phrase identification
  - Predictive text models

### Collocation Analysis

#### Statistical Measures
1. **Mutual Information (MI)**
   - Identifies strong associations
   - Formula: log₂(O/E)
   - Good for low-frequency pairs

2. **T-score**
   - Statistical significance measure
   - Better for frequent collocations
   - Less sensitive to corpus size

3. **Log-likelihood**
   - Compares observed vs. expected frequencies
   - Robust across different corpus sizes

#### Example: Finding Collocations
```r
library(quanteda)
library(quanteda.textstats)

# Create corpus
german_corpus <- corpus(texts)

# Generate tokens
toks <- tokens(german_corpus, remove_punct = TRUE)

# Find collocations
colls <- textstat_collocations(toks, size = 2, min_count = 5)
head(colls, 20)
```

### Concordancing

#### KWIC (Key Word in Context)
- **Purpose**: Examine word usage in context
- **Applications**:
  - Semantic analysis
  - Grammatical pattern identification
  - Translation studies

#### Example: KWIC Analysis
```python
from nltk import ConcordanceIndex

def kwic_analysis(corpus, keyword, window=5):
    """
    Generate KWIC display for a keyword
    """
    concordance = ConcordanceIndex(corpus)
    return concordance.find_concordance(keyword, window)
```

### Register and Genre Analysis

#### Multidimensional Analysis (MDA)
1. **Dimension Identification**
   - Extract linguistic features
   - Factor analysis to identify dimensions
   - Interpret dimensions functionally

2. **Key Features for German**
   - Verb forms (present, past, passive)
   - Nominalizations
   - Modal particles
   - Subordination complexity

#### Example Features
```python
def extract_register_features(doc):
    """
    Extract register-relevant linguistic features
    """
    features = {
        'type_token_ratio': len(set(doc)) / len(doc),
        'avg_word_length': sum(len(token.text) for token in doc) / len(doc),
        'noun_ratio': sum(1 for token in doc if token.pos_ == 'NOUN') / len(doc),
        'verb_ratio': sum(1 for token in doc if token.pos_ == 'VERB') / len(doc),
        'adjective_ratio': sum(1 for token in doc if token.pos_ == 'ADJ') / len(doc),
        'passive_constructions': count_passive(doc),
        'compound_nouns': count_compounds(doc),
        'modal_particles': count_modal_particles(doc)
    }
    return features
```

### Diachronic Analysis

#### Time-Series Analysis
- **Tracking language change** over time
- **Frequency trends** of lexical items
- **Grammaticalization** processes

#### Example: Historical Frequency
```r
library(ggplot2)

# Plot word frequency over time
ggplot(time_freq_data, aes(x = year, y = frequency, color = word)) +
  geom_line() +
  geom_smooth(method = "loess") +
  labs(title = "Frequency Change Over Time",
       x = "Year", y = "Normalized Frequency")
```

## Advanced Computational Methods

### Word Embeddings

#### Word2Vec for German
```python
from gensim.models import Word2Vec
import spacy

# Load and prepare corpus
nlp = spacy.load("de_core_news_lg")
sentences = [doc for doc in nlp.pipe(corpus_texts)]

# Train Word2Vec model
model = Word2Vec(sentences, 
                 vector_size=100, 
                 window=5, 
                 min_count=5, 
                 workers=4)

# Find similar words
similar = model.wv.most_similar('Sprache', topn=10)
```

#### BERT-based Embeddings
```python
from transformers import BertTokenizer, BertModel
import torch

# Load German BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-german-cased')
model = BertModel.from_pretrained('bert-base-german-cased')

# Get contextualized embeddings
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state
```

### Topic Modeling

#### Latent Dirichlet Allocation (LDA)
```python
from gensim import corpora
from gensim.models import LdaModel

# Prepare documents
processed_docs = [preprocess(doc) for doc in documents]

# Create dictionary and corpus
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Train LDA model
lda_model = LdaModel(corpus=corpus,
                     id2word=dictionary,
                     num_topics=10,
                     random_state=42,
                     passes=10)

# Get topics
topics = lda_model.print_topics(num_words=10)
```

### Sentiment Analysis

#### German Sentiment Lexicons
- **SentiWS**: Sentiment Wortschatz
- **GermanPolarityClues**: Polarity lexicon

```python
from textblob_de import TextBlobDE

def analyze_sentiment(text):
    """
    Analyze sentiment of German text
    """
    blob = TextBlobDE(text)
    return {
        'polarity': blob.sentiment.polarity,
        'subjectivity': blob.sentiment.subjectivity
    }
```

## Quality Control and Validation

### Annotation Quality

#### Inter-Annotator Agreement
```python
from sklearn.metrics import cohen_kappa_score

# Calculate Cohen's Kappa
kappa = cohen_kappa_score(annotator1_labels, annotator2_labels)
print(f"Cohen's Kappa: {kappa:.3f}")

# Interpretation:
# < 0.00: Poor agreement
# 0.00-0.20: Slight agreement
# 0.21-0.40: Fair agreement
# 0.41-0.60: Moderate agreement
# 0.61-0.80: Substantial agreement
# 0.81-1.00: Almost perfect agreement
```

#### Krippendorff's Alpha
```python
import krippendorff

# For multiple annotators
alpha = krippendorff.alpha(reliability_data=annotations,
                           level_of_measurement='nominal')
```

### Corpus Representativeness

- **Balance**: Proportional representation of text types
- **Sampling**: Random vs. stratified sampling
- **Size**: Sufficient tokens for statistical reliability
- **Documentation**: Metadata and provenance

## Best Practices

### 1. Reproducibility
- Document corpus version
- Record query parameters
- Share preprocessing scripts
- Use version control (Git)

### 2. Ethical Considerations
- Copyright and licensing
- Privacy protection
- Informed consent for spoken data
- Anonymization of personal data

### 3. Statistical Validity
- Report confidence intervals
- Use appropriate significance tests
- Control for confounding variables
- Validate on held-out data

### 4. Interpretation
- Contextualize quantitative findings
- Triangulate with qualitative analysis
- Consider corpus composition effects
- Acknowledge limitations

## Tools and Software

### Corpus Query Systems
- **CQP** (Corpus Query Processor)
- **CQL** (Corpus Query Language)
- **AntConc**: Desktop concordancer
- **Sketch Engine**: Online corpus tool

### Programming Libraries

#### Python
- `spaCy`: Industrial-strength NLP
- `NLTK`: Natural Language Toolkit
- `gensim`: Topic modeling
- `pandas`: Data manipulation

#### R
- `quanteda`: Quantitative text analysis
- `tidytext`: Text mining with tidy data
- `tm`: Text mining
- `udpipe`: UDPipe NLP toolkit

## References

- Lemnitzer, L., & Zinsmeister, H. (2015). *Korpuslinguistik: Eine Einführung*. Narr.
- Scherer, C. (2006). *Korpuslinguistik*. Winter.
- McEnery, T., & Hardie, A. (2012). *Corpus Linguistics: Method, Theory and Practice*. Cambridge University Press.
- Biber, D., & Conrad, S. (2019). *Register, Genre, and Style*. Cambridge University Press.
