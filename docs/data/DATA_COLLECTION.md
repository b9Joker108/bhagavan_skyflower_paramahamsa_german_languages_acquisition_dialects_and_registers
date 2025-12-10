# Data Collection and Management Guidelines

## Overview

This document outlines best practices for data collection, annotation, and management in German language research, covering corpus construction, learner data, dialectal recordings, and ethical considerations.

## General Principles

### FAIR Data Principles

Data should be:
- **F**indable: Persistent identifiers, rich metadata
- **A**ccessible: Open access when possible, clear access protocols
- **I**nteroperable: Standard formats, vocabularies
- **R**eusable: Clear licensing, comprehensive documentation

### Ethical Considerations

#### Informed Consent
```
Essential elements:
- Purpose of research clearly stated
- How data will be used
- Storage and retention period
- Anonymization procedures
- Right to withdraw
- Contact information for questions
```

#### GDPR Compliance (for EU data)
- Legal basis for processing
- Data minimization
- Purpose limitation
- Storage limitation
- Right to access and erasure
- Data protection by design

## Corpus Construction

### Design Principles

#### Representativeness
```
Considerations:
- Target population definition
- Sampling frame
- Sampling method (random, stratified, convenience)
- Sample size justification
- Potential biases
```

#### Balance
```
Stratification factors:
- Text type/register
- Genre
- Time period
- Regional variety
- Author demographics
- Publication venue
```

### Corpus Metadata

#### Essential Metadata Fields
```json
{
  "text_id": "unique_identifier",
  "title": "Text title or description",
  "author": {
    "name": "Author name or pseudonym",
    "age": 25,
    "gender": "female",
    "L1": "English",
    "education_level": "university"
  },
  "text_properties": {
    "genre": "essay",
    "register": "formal_written",
    "topic": "environmental_policy",
    "word_count": 1500,
    "date_created": "2024-03-15"
  },
  "collection": {
    "corpus_name": "GermanLearnerCorpus",
    "version": "2.0",
    "collector": "researcher_id",
    "collection_date": "2024-03-20"
  },
  "legal": {
    "license": "CC-BY-4.0",
    "consent_obtained": true,
    "consent_id": "consent_form_123"
  }
}
```

### File Formats

#### Text Files
- **Plain text**: UTF-8 encoding, .txt extension
- **Annotations**: XML, JSON, CoNLL-U formats
- **Metadata**: JSON, CSV, YAML

#### Audio Files
- **Uncompressed**: WAV (44.1 kHz, 16-bit minimum)
- **Compressed**: FLAC (lossless) or MP3 (320 kbps minimum)
- **Metadata**: TextGrid (Praat), ELAN (.eaf), Transcriber (.trs)

#### Video Files
- **Format**: MP4 (H.264 codec)
- **Resolution**: 1080p minimum for gesture/facial analysis
- **Audio**: Separate high-quality audio track

## Learner Corpus Data

### Participant Information

```
Learner profile:
- Unique participant ID
- Age at time of data collection
- Gender
- L1 and other languages known
- Age of onset of German learning
- Total hours of instruction
- Immersion experience
- Current proficiency level (CEFR)
- Education level
- Motivation for learning
```

### Task Design

#### Elicitation Tasks
```python
# Example task metadata structure
task = {
    'task_id': 'narrative_001',
    'task_type': 'oral_narrative',
    'instructions': 'Describe what you did last weekend',
    'time_limit': 300,  # seconds
    'preparation_time': 60,
    'elicitation_method': 'free_production',
    'target_structures': ['past_tense', 'time_expressions']
}
```

### Error Annotation

#### Multi-layer Annotation
```xml
<sentence id="s1">
  <original>*Ich habe gestern den Film gesehen.</original>
  <target>Ich habe gestern den Film gesehen.</target>
  <error_annotation>
    <token id="t1" form="Ich" target="Ich" error_type="none"/>
    <token id="t2" form="habe" target="habe" error_type="none"/>
    <token id="t3" form="gestern" target="gestern" error_type="none"/>
    <token id="t4" form="den" target="den" error_type="none"/>
    <token id="t5" form="Film" target="Film" error_type="none"/>
    <token id="t6" form="gesehen" target="gesehen" error_type="none"/>
  </error_annotation>
  <metadata>
    <proficiency_level>B1</proficiency_level>
    <L1>English</L1>
  </metadata>
</sentence>
```

#### Error Taxonomy
```
Categories:
1. Orthography
   - Spelling
   - Capitalization
   - Punctuation

2. Morphology
   - Case marking
   - Gender agreement
   - Number agreement
   - Verb conjugation
   - Tense/aspect

3. Syntax
   - Word order
   - Verb position
   - Missing elements
   - Redundant elements

4. Lexis
   - Word choice
   - Collocation
   - False friends
   - Register mismatch

5. Discourse
   - Coherence
   - Cohesion
   - Reference
```

## Dialectal Data

### Recording Protocol

#### Equipment Checklist
```
Required:
☐ Primary recorder (e.g., Zoom H4n Pro)
☐ Backup recorder
☐ High-quality microphone
☐ Windscreen/pop filter
☐ Headphones for monitoring
☐ Spare batteries
☐ Memory cards (multiple)
☐ Consent forms
☐ Metadata sheets

Optional:
☐ Lavalier microphones for multiple speakers
☐ Acoustic isolation booth
☐ Video camera
```

#### Recording Specifications
```
Audio settings:
- Sample rate: 44.1 kHz or 48 kHz
- Bit depth: 16-bit minimum, 24-bit preferred
- Format: WAV (uncompressed)
- Channels: Mono for single speaker, stereo for multiple

File naming convention:
YYYYMMDD_LocationCode_SpeakerID_TaskType_RecordingNumber.wav

Example:
20240315_MUC_SP001_Conversation_01.wav
```

### Speaker Metadata

```json
{
  "speaker_id": "SP001",
  "demographics": {
    "age": 65,
    "gender": "male",
    "birthplace": "München",
    "current_residence": "München",
    "education": "Hauptschule",
    "occupation": "retired craftsman"
  },
  "linguistic_background": {
    "native_dialect": "Bavarian",
    "other_languages": ["Standard German", "English (basic)"],
    "mobility_history": [
      {"location": "München", "years": "1955-present"}
    ],
    "language_use": {
      "dialect_at_home": "daily",
      "standard_german_use": "occasional",
      "code_switching_frequency": "moderate"
    }
  },
  "recording_info": {
    "date": "2024-03-15",
    "location": "participant's home",
    "duration_minutes": 45,
    "interlocutor": "fieldworker",
    "quality": "excellent"
  }
}
```

### Transcription

#### Transcription System (GAT2 - Gesprächsanalytisches Transkriptionssystem)

```
Basic conventions:
.               falling intonation
?               rising intonation
,               level intonation
-               cut-off
=               latching (no gap)
(.)             micropause
(0.5)           timed pause in seconds
[overlap]       simultaneous speech
<<soft> text>   paralinguistic features
(text)          uncertain transcription
(  )            unintelligible
((laughs))      non-verbal action

Phonetic notation:
- Use standard orthography when possible
- IPA for dialectal features
- Consistency within corpus
```

#### Example Transcription
```
01  SP001:  so des wor hoit scho a schee zeit↓
            'so that was indeed a nice time'
02          (0.8)
03  INT:    mhm=
04  SP001:  =ober heit↑ (.) is ois anders↓
            'but today, everything is different'
05          [des ko ma] scho song
            'that one can say'
06  INT:    [mhm ja  ]
            'mhm yes'
```

## Register-Specific Data

### Text Collection

#### Web Scraping Ethics
```python
# Example robots.txt compliance check
import urllib.robotparser

def can_scrape(url):
    """Check if scraping is allowed"""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)
```

#### Source Documentation
```
For each text:
- URL or publication details
- Author (if available)
- Publication date
- Collection date
- Copyright status
- License (if specified)
- Archive location
```

### Register Annotation

```json
{
  "text_id": "REG001",
  "register_classification": {
    "primary_register": "academic",
    "sub_register": "research_article",
    "discipline": "linguistics",
    "section": "introduction"
  },
  "situational_parameters": {
    "field": "language_acquisition_research",
    "tenor": {
      "formality": "formal",
      "relationship": "expert_to_expert",
      "power_distance": "symmetric"
    },
    "mode": {
      "channel": "written",
      "medium": "digital",
      "interactivity": "non-interactive"
    }
  }
}
```

## Data Storage and Archiving

### File Organization

```
project_root/
├── data/
│   ├── raw/
│   │   ├── audio/
│   │   ├── text/
│   │   └── video/
│   ├── processed/
│   │   ├── transcriptions/
│   │   ├── annotations/
│   │   └── features/
│   └── metadata/
│       ├── participant_info.csv
│       ├── corpus_metadata.json
│       └── data_dictionary.md
├── scripts/
│   ├── preprocessing/
│   ├── analysis/
│   └── visualization/
├── results/
│   ├── figures/
│   ├── tables/
│   └── statistical_output/
└── documentation/
    ├── README.md
    ├── CHANGELOG.md
    └── LICENSE.txt
```

### Backup Strategy

```
3-2-1 Rule:
- 3 copies of data
- 2 different storage media
- 1 off-site backup

Implementation:
- Primary: Working directory on local machine
- Secondary: External hard drive (encrypted)
- Tertiary: Cloud storage (encrypted) or institutional repository
```

### Long-term Archiving

#### Recommended Repositories
- **General**: Zenodo, OSF, GitHub (for code)
- **Linguistic Data**: CLARIN repositories, TalkBank, LDC
- **Institutional**: University data repositories

#### Archive Package Contents
```
Required files:
☐ README.md (overview, contents, usage)
☐ DATA_DICTIONARY.md (variable descriptions)
☐ LICENSE.txt (usage terms)
☐ CHANGELOG.md (version history)
☐ Metadata files (JSON/CSV)
☐ Code/scripts for reproducibility
☐ Example analyses
☐ Citation information
```

## Data Sharing

### Levels of Access

```
Level 1: Public (Open Access)
- Anonymized data
- No personal information
- Permissive license (e.g., CC-BY)

Level 2: Restricted (Registration Required)
- Semi-anonymized data
- Research use only
- Data use agreement

Level 3: Controlled (Application Required)
- Potentially identifiable data
- Ethics approval required
- Secure access environment

Level 4: Closed
- Not shareable (privacy concerns)
- Derivative data only (aggregated statistics)
```

### Data Use Agreements

```
Standard clauses:
1. Purpose limitation (research use only)
2. No re-identification attempts
3. No redistribution without permission
4. Citation requirement
5. Destruction after use
6. Security measures
7. Reporting requirements
```

## Quality Assurance

### Inter-Annotator Agreement

```python
from sklearn.metrics import cohen_kappa_score
import krippendorff

# Cohen's Kappa (2 annotators)
kappa = cohen_kappa_score(annotator1, annotator2)

# Krippendorff's Alpha (multiple annotators)
alpha = krippendorff.alpha(reliability_data=annotations,
                           level_of_measurement='nominal')

# Target thresholds:
# Kappa/Alpha > 0.8: Excellent agreement
# Kappa/Alpha 0.6-0.8: Substantial agreement
# Kappa/Alpha < 0.6: Requires discussion and refinement
```

### Data Validation

```python
# Example validation checks
def validate_corpus_data(data):
    """Run validation checks on corpus data"""
    issues = []
    
    # Check for missing values
    if data.isnull().any().any():
        issues.append("Missing values detected")
    
    # Check ID uniqueness
    if not data['text_id'].is_unique:
        issues.append("Duplicate IDs found")
    
    # Check value ranges
    if (data['proficiency_level'].isin(['A1','A2','B1','B2','C1','C2'])).all() == False:
        issues.append("Invalid proficiency levels")
    
    # Check file existence
    for filepath in data['file_path']:
        if not os.path.exists(filepath):
            issues.append(f"Missing file: {filepath}")
    
    return issues
```

## Version Control

### Semantic Versioning

```
Format: MAJOR.MINOR.PATCH

MAJOR: Incompatible changes (e.g., new annotation scheme)
MINOR: Backwards-compatible additions (e.g., new texts)
PATCH: Backwards-compatible fixes (e.g., corrected errors)

Example: v2.1.3
```

### Change Documentation

```markdown
# Changelog

## [2.1.0] - 2024-03-15
### Added
- 50 new learner texts (B2 level)
- Sentiment annotations for all texts

### Changed
- Updated error taxonomy to include pragmatic errors
- Improved metadata completeness

### Fixed
- Corrected 15 transcription errors in audio files
- Fixed encoding issues in 3 text files

## [2.0.0] - 2024-01-10
### Added
- Complete re-annotation with new scheme
- Video recordings for 30 participants

### Removed
- Deprecated annotation layer (v1 format)
```

## References

- Berez-Kroeker, A. L., et al. (2018). The Austin Principles of Data Citation in Linguistics. *Language Documentation & Conservation*, 12, 385-389.
- CLARIN. (2019). *Guidelines for the Informed Consent Process*. CLARIN ERIC.
- Mathet, Y., et al. (2015). The Agreement Measure Gamma-Cat: A Complement to Gamma Focused on Categorization of a Continuum. *Computational Linguistics*, 41(3), 437-479.
