# Second Language Acquisition (SLA) Methodologies for German

## Overview

This document outlines state-of-the-art methodologies for researching second language acquisition of German, including theoretical frameworks, research designs, and data collection methods.

## Theoretical Frameworks

### 1. Usage-Based Theory

#### Core Principles
- Language learning through exposure to input
- Frequency effects in acquisition
- Construction grammar approach
- Emergent grammar from usage patterns

#### German-Specific Applications
```
Frequency-based acquisition order:
1. High-frequency chunks: "Wie geht's?", "Guten Tag"
2. Core constructions: Subject-Verb-Object
3. Complex patterns: Verb-final subordinate clauses
```

#### Research Methods
```python
# Analyze frequency in learner input
from collections import Counter
import pandas as pd

def analyze_input_frequency(corpus):
    """
    Calculate frequency of linguistic items in input
    """
    constructions = extract_constructions(corpus)
    freq_dist = Counter(constructions)
    
    # Compare to acquisition order
    acquisition_data = pd.read_csv('acquisition_order.csv')
    correlation = correlate_freq_acquisition(freq_dist, acquisition_data)
    
    return correlation
```

### 2. Processability Theory (PT)

#### Pienemann's Hierarchy for German
```
Stage 1: Word/Lemma
- Single words, formulas

Stage 2: Category Procedure
- Lexical morphemes (plural -s, -en)

Stage 3: Phrasal Procedure
- SV agreement, ADJ-N agreement

Stage 4: S-procedure (Sentence procedure)
- Subject-Verb inversion (V2)
- Verb separation

Stage 5: Subordinate Clause Procedure
- Verb-final in subordinate clauses
- Perfect auxiliary selection

Stage 6: Main Clause + Subordinate Clause
- Integration of complex syntax
```

#### Assessment Protocol
```r
# Code learner production by PT stage
library(dplyr)

assess_pt_stage <- function(learner_data) {
  scores <- learner_data %>%
    mutate(
      stage1 = count_formulas(text),
      stage2 = count_lexical_morphemes(text),
      stage3 = check_agreement(text),
      stage4 = check_v2_separation(text),
      stage5 = check_verb_final(text),
      stage6 = check_complex_integration(text)
    ) %>%
    determine_current_stage()
  
  return(scores)
}
```

### 3. Sociocultural Theory (SCT)

#### Key Concepts
- **Zone of Proximal Development (ZPD)**: Gap between current and potential ability
- **Scaffolding**: Support provided by more capable peer/teacher
- **Mediation**: Language learning mediated by tools and interaction

#### Research Designs

**Dynamic Assessment**
```
Protocol:
1. Pre-test (learner's independent performance)
2. Mediation phase (graduated prompts)
3. Post-test (measure learning potential)
4. Transfer task (generalization)

Prompt hierarchy for German case system:
Level 1: "Is there an error?"
Level 2: "Look at the case marking"
Level 3: "What case does this verb require?"
Level 4: "Denken takes the accusative"
```

**Languaging Analysis**
```python
def analyze_languaging(interaction_transcript):
    """
    Analyze metalinguistic talk in interaction
    """
    languaging_episodes = {
        'form_focused': [],
        'meaning_focused': [],
        'self_correction': [],
        'other_correction': []
    }
    
    for turn in interaction_transcript:
        if is_metalinguistic(turn):
            episode_type = classify_episode(turn)
            languaging_episodes[episode_type].append(turn)
    
    return languaging_episodes
```

### 4. Complex Dynamic Systems Theory (CDST)

#### Principles
- Language as dynamic, non-linear system
- Variability is inherent, not error
- Development shows patterns and variation
- Multiple timescales (microgenetic, ontogenetic)

#### Methodological Implications
```r
library(ggplot2)
library(gridExtra)

# Longitudinal variability analysis
plot_development <- function(learner_data) {
  # Accuracy over time with variability
  p1 <- ggplot(learner_data, aes(x = session, y = accuracy)) +
    geom_line() +
    geom_smooth(method = "loess", color = "red") +
    labs(title = "Developmental Trajectory with Variability")
  
  # Moving min-max range
  p2 <- ggplot(learner_data, aes(x = session)) +
    geom_ribbon(aes(ymin = min_accuracy, ymax = max_accuracy), 
                alpha = 0.3) +
    geom_line(aes(y = mean_accuracy)) +
    labs(title = "Range of Variation Over Time")
  
  grid.arrange(p1, p2, ncol = 2)
}
```

## Research Designs

### 1. Cross-Sectional Studies

#### Design Features
- Multiple proficiency levels at one time point
- Reveals developmental sequences
- Cost-effective
- Cannot track individual development

#### Sampling Strategy
```
Proficiency levels:
- Beginner (A1-A2): n = 30
- Intermediate (B1-B2): n = 30  
- Advanced (C1-C2): n = 30

Controls:
- Native speakers: n = 30
- Age range: 18-35
- L1 backgrounds: Stratified sampling
```

#### Statistical Analysis
```r
library(lme4)
library(emmeans)

# Mixed-effects model with proficiency as predictor
model <- lmer(accuracy ~ proficiency_level + item_type + 
               (1|participant) + (1|item),
             data = crosssectional_data)

# Pairwise comparisons
emmeans(model, pairwise ~ proficiency_level)
```

### 2. Longitudinal Studies

#### Design Features
- Same learners over time
- Tracks individual trajectories
- Identifies developmental patterns
- Resource-intensive

#### Data Collection Schedule
```
Example 1-year study:
- Baseline (Week 0)
- Monthly sessions (Weeks 4, 8, 12, 16, 20, 24)
- Mid-point assessment (Week 12)
- Final assessment (Week 24)
- Delayed post-test (Week 36)

At each session:
- Writing sample (30 min)
- Speaking task (15 min)
- Grammar test (20 min)
- Self-assessment questionnaire (10 min)
```

#### Growth Curve Modeling
```r
library(lme4)
library(ggplot2)

# Individual growth curves
model <- lmer(score ~ time + I(time^2) + 
               (time | participant),
             data = longitudinal_data)

# Plot individual trajectories
ggplot(longitudinal_data, aes(x = time, y = score, group = participant)) +
  geom_line(alpha = 0.3) +
  geom_smooth(aes(group = 1), method = "loess", 
              color = "red", size = 1.5) +
  labs(title = "Individual Learning Trajectories",
       x = "Time (weeks)", y = "Proficiency Score")
```

### 3. Experimental Studies

#### Intervention Studies
```
Design: Pretest - Treatment - Posttest - Delayed Posttest

Groups:
- Experimental group (n = 30): Target instruction
- Comparison group (n = 30): Alternative instruction
- Control group (n = 30): No instruction

Randomization: Blocked by proficiency level
```

#### Example: Focus on Form Intervention
```python
import scipy.stats as stats
import pandas as pd

# Analyze intervention effect
def analyze_intervention(data):
    """
    Compare groups using mixed ANOVA
    """
    # Repeated measures ANOVA
    # Between-subjects: group
    # Within-subjects: time (pre, post, delayed)
    
    results = {
        'group_effect': f_test_group(data),
        'time_effect': f_test_time(data),
        'interaction': f_test_interaction(data),
        'pairwise': posthoc_comparisons(data)
    }
    
    return results
```

### 4. Case Studies

#### Intensive Individual Analysis
```
Data sources:
- Multiple elicitation methods
- Various contexts and tasks
- Longitudinal tracking
- Triangulation of methods

Analysis:
- Detailed qualitative coding
- Discourse analysis
- Conversation analysis
- Microgenetic analysis
```

## Data Collection Methods

### 1. Elicitation Tasks

#### Oral Picture Description
```
Standard materials:
- Cookie Theft picture (aphasia test)
- Frog Story (Mayer, 1969)
- DPNS (Developmental Picture Naming Study)

Procedure:
1. Familiarization (1 min)
2. Planning time (30 sec)
3. Description (2-3 min)
4. Recording and transcription

Analysis measures:
- Fluency (words per minute, pauses)
- Accuracy (error-free clauses)
- Complexity (subordination, lexical diversity)
```

#### Grammaticality Judgment Tasks (GJT)
```python
class GrammaticalityJudgment:
    def __init__(self):
        self.items = []
        self.responses = []
    
    def create_item(self, sentence, grammatical, target_structure):
        """
        Create GJT item
        """
        item = {
            'sentence': sentence,
            'grammatical': grammatical,
            'structure': target_structure,
            'distractor': not grammatical
        }
        self.items.append(item)
    
    def administer_test(self, participant):
        """
        Administer GJT with timing
        """
        for item in self.items:
            start_time = time.time()
            response = present_and_record(item['sentence'])
            rt = time.time() - start_time
            
            self.responses.append({
                'participant': participant,
                'item': item['sentence'],
                'judgment': response,
                'reaction_time': rt,
                'correct': response == item['grammatical']
            })
        
        return self.responses
```

#### Elicited Imitation
```
Procedure:
1. Listen to model sentence
2. Distractor task (e.g., answer question)
3. Repeat sentence
4. Audio recording

Target structures:
- Word order (V2, verb-final)
- Case marking
- Gender agreement
- Complex syntax

Analysis:
- Exact repetition rate
- Systematic deviations
- Simplification patterns
```

### 2. Corpus-Based Methods

#### Learner Corpus Construction
```
Corpus design:
- Size: 100,000+ words
- Learners: 100+ participants
- L1 backgrounds: Multiple (English, Spanish, Chinese, etc.)
- Proficiency levels: A1-C2
- Text types: Essays, emails, summaries
- Metadata: Age, L1, proficiency, instruction hours

Annotation layers:
- Error annotation
- Target hypothesis
- Part-of-speech tags
- Dependency parsing
- CEFR level
```

#### Error Analysis
```python
import pandas as pd

class ErrorAnalyzer:
    def __init__(self):
        self.error_categories = {
            'morphology': ['case', 'gender', 'number', 'tense'],
            'syntax': ['word_order', 'agreement', 'subordination'],
            'lexical': ['word_choice', 'collocation', 'register']
        }
    
    def annotate_errors(self, text, target_text):
        """
        Compare learner text with target hypothesis
        """
        errors = []
        # Implementation of error detection
        for i, (learner_token, target_token) in enumerate(zip(text, target_text)):
            if learner_token != target_token:
                error = self.classify_error(learner_token, target_token)
                errors.append({
                    'position': i,
                    'learner_form': learner_token,
                    'target_form': target_token,
                    'error_type': error['type'],
                    'category': error['category']
                })
        
        return errors
    
    def calculate_accuracy(self, errors, total_obligatory_contexts):
        """
        Calculate accuracy in obligatory contexts
        """
        correct = total_obligatory_contexts - len(errors)
        accuracy = correct / total_obligatory_contexts
        return accuracy
```

### 3. Experimental Methods

#### Self-Paced Reading
```python
import time

class SelfPacedReading:
    def __init__(self, sentences):
        self.sentences = sentences
        self.reading_times = []
    
    def run_trial(self, sentence):
        """
        Present sentence word-by-word
        """
        words = sentence.split()
        rts = []
        
        for word in words:
            start = time.time()
            display_word(word)
            wait_for_keypress()
            rt = time.time() - start
            rts.append(rt)
        
        return rts
    
    def analyze_critical_region(self, rts, critical_position):
        """
        Analyze reading times at critical region
        """
        critical_rt = rts[critical_position]
        spillover_rt = rts[critical_position + 1] if critical_position + 1 < len(rts) else None
        
        return {
            'critical': critical_rt,
            'spillover': spillover_rt
        }
```

#### Eye-Tracking
```
Measures:
- First fixation duration
- Total fixation duration
- Number of fixations
- Regression path duration
- Skip rate

Analysis regions:
- Pre-critical: Baseline processing
- Critical: Target structure
- Post-critical: Integration/spillover

Example: Case marking processing
"Der Mann sieht den/*der Jungen im Park."
         [critical region]
```

#### Event-Related Potentials (ERP)
```
ERP Components for German:
- N400 (300-500ms): Semantic violations
- P600 (500-900ms): Syntactic violations
- LAN (300-500ms): Morphosyntactic errors

Example study:
Condition 1: *Der Vater hat das Buch gelesen (correct)
Condition 2: *Der Vater haben das Buch gelesen (agreement error)
Condition 3: *Der Vater hat das Buch essen (semantic anomaly)

Expected patterns:
- Condition 2: LAN + P600
- Condition 3: N400
```

### 4. Interactional Data

#### Conversation Analysis (CA)
```
Transcription conventions (GAT2):
- [overlap]
- = latching
- (.) micropause
- (0.5) timed pause
- ? rising intonation
- . falling intonation
- ↑↓ pitch changes

Analysis focus:
- Turn-taking
- Repair sequences
- Preference organization
- Language alternation
```

#### Interaction Coding
```python
class InteractionCoder:
    def __init__(self):
        self.codes = {
            'negotiation_of_meaning': ['clarification_request', 'confirmation_check', 'comprehension_check'],
            'feedback': ['recast', 'explicit_correction', 'elicitation'],
            'uptake': ['repair', 'needs_repair', 'acknowledgement']
        }
    
    def code_interaction(self, transcript):
        """
        Code interactional features
        """
        coded_turns = []
        
        for turn in transcript:
            codes = self.identify_codes(turn)
            coded_turns.append({
                'speaker': turn['speaker'],
                'utterance': turn['text'],
                'codes': codes
            })
        
        return coded_turns
```

## Assessment Methods

### 1. Proficiency Assessment

#### CEFR-Based Assessment
```
A1: Basic user - Breakthrough
A2: Basic user - Waystage
B1: Independent user - Threshold
B2: Independent user - Vantage
C1: Proficient user - Effective operational proficiency
C2: Proficient user - Mastery

Assessment tasks by level:
A1-A2: Simple forms, basic interactions
B1-B2: Complex texts, detailed descriptions
C1-C2: Extended discourse, nuanced expression
```

#### Standardized Tests
- **TestDaF**: Academic German (B2-C1)
- **Goethe-Zertifikat**: A1-C2 levels
- **telc Deutsch**: Various levels and purposes
- **DSH**: University entrance exam

### 2. Developmental Measures

#### Complexity, Accuracy, Fluency (CAF)
```python
class CAFAnalyzer:
    def analyze_text(self, text, speech_duration=None):
        """
        Calculate CAF measures
        """
        doc = nlp(text)
        
        # Complexity
        complexity = {
            'mltt': self.mean_length_of_t_unit(doc),
            'subordination_ratio': self.subordination_ratio(doc),
            'lexical_diversity': self.type_token_ratio(doc)
        }
        
        # Accuracy
        accuracy = {
            'error_free_clauses': self.error_free_clause_ratio(doc),
            'target_like_use': self.calculate_tlu(doc)
        }
        
        # Fluency (if speech data)
        if speech_duration:
            fluency = {
                'speech_rate': len(doc) / speech_duration,
                'pause_frequency': self.count_pauses(text),
                'repair_frequency': self.count_repairs(text)
            }
        else:
            fluency = None
        
        return {
            'complexity': complexity,
            'accuracy': accuracy,
            'fluency': fluency
        }
```

## Statistical Analysis

### 1. Mixed-Effects Models
```r
library(lme4)
library(lmerTest)

# Example: L1 effect on acquisition
model <- lmer(accuracy ~ proficiency * l1_background + 
               (1 + proficiency | participant) + 
               (1 | item),
             data = sla_data)

summary(model)
anova(model)
```

### 2. Generalized Additive Models (GAM)
```r
library(mgcv)

# Non-linear developmental trajectories
gam_model <- gam(score ~ s(time, by = participant_group) + 
                  proficiency_level,
                data = longitudinal_data)

plot(gam_model)
```

## Best Practices

### 1. Ethical Considerations
- Informed consent
- Anonymization
- Data protection (GDPR)
- Participant rights
- Benefit to participants

### 2. Reproducibility
- Preregistration of studies
- Open data and materials
- Transparent reporting
- Replication studies

### 3. Validity and Reliability
- Triangulation of methods
- Inter-rater reliability
- Construct validity
- Ecological validity

## References

- Ellis, R., & Barkhuizen, G. (2005). *Analysing Learner Language*. Oxford University Press.
- Pienemann, M. (1998). *Language Processing and Second Language Development: Processability Theory*. Benjamins.
- Ortega, L. (2013). *Understanding Second Language Acquisition*. Routledge.
- Granger, S. (Ed.). (2015). *The Cambridge Handbook of Learner Corpus Research*. Cambridge University Press.
