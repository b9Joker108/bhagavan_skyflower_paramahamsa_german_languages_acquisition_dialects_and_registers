#!/usr/bin/env python3
"""
Register Feature Extraction for German Texts

This script demonstrates automated extraction of linguistic features
relevant for register analysis of German texts.
"""

import spacy
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class GermanRegisterAnalyzer:
    """
    Automated register feature extraction for German texts.
    
    Extracts lexical, grammatical, and syntactic features used in
    multidimensional analysis and register classification.
    """
    
    def __init__(self, model="de_core_news_lg"):
        """Initialize with German spaCy model"""
        self.nlp = spacy.load(model)
        
        # Modal particles (characteristic of spoken/informal German)
        self.modal_particles = {
            'halt', 'eben', 'mal', 'doch', 'ja', 'schon', 
            'wohl', 'etwa', 'eigentlich', 'bloß', 'nur'
        }
        
        # Discourse connectives (formal/written)
        self.connectives = {
            'deshalb', 'daher', 'folglich', 'demzufolge', 'somit',
            'jedoch', 'dennoch', 'trotzdem', 'allerdings',
            'zudem', 'darüber hinaus', 'außerdem'
        }
        
    def extract_all_features(self, text):
        """
        Extract comprehensive feature set for register analysis.
        
        Args:
            text: Input German text string
            
        Returns:
            Dictionary of extracted features
        """
        doc = self.nlp(text)
        
        features = {}
        
        # Lexical features
        features.update(self._lexical_features(doc))
        
        # Grammatical features
        features.update(self._grammatical_features(doc))
        
        # Syntactic features
        features.update(self._syntactic_features(doc))
        
        # Register-specific markers
        features.update(self._register_markers(doc))
        
        return features
    
    def _lexical_features(self, doc):
        """Extract lexical complexity features"""
        tokens = [t for t in doc if not t.is_punct and not t.is_space]
        
        if not tokens:
            return {}
        
        # Type-Token Ratio
        lemmas = [t.lemma_.lower() for t in tokens]
        ttr = len(set(lemmas)) / len(lemmas)
        
        # Average word length
        avg_word_len = np.mean([len(t.text) for t in tokens])
        
        # Lexical density (content words / total words)
        content_pos = {'NOUN', 'VERB', 'ADJ', 'ADV'}
        content_words = sum(1 for t in doc if t.pos_ in content_pos)
        lexical_density = content_words / len(tokens)
        
        return {
            'type_token_ratio': ttr,
            'avg_word_length': avg_word_len,
            'lexical_density': lexical_density
        }
    
    def _grammatical_features(self, doc):
        """Extract grammatical feature frequencies"""
        total_tokens = len([t for t in doc if not t.is_punct])
        
        if total_tokens == 0:
            return {}
        
        # POS frequencies (normalized)
        pos_counts = Counter(t.pos_ for t in doc if not t.is_punct)
        
        return {
            'noun_frequency': pos_counts['NOUN'] / total_tokens,
            'verb_frequency': pos_counts['VERB'] / total_tokens,
            'adjective_frequency': pos_counts['ADJ'] / total_tokens,
            'adverb_frequency': pos_counts['ADV'] / total_tokens,
            'pronoun_frequency': pos_counts['PRON'] / total_tokens,
            'determiner_frequency': pos_counts['DET'] / total_tokens
        }
    
    def _syntactic_features(self, doc):
        """Extract syntactic complexity features"""
        sentences = list(doc.sents)
        
        if not sentences:
            return {}
        
        # Average sentence length
        avg_sent_len = len(doc) / len(sentences)
        
        # Subordination (count subordinate clauses)
        subordinate_markers = sum(1 for t in doc if t.dep_ in ['mark', 'acl', 'advcl', 'csubj'])
        subordination_ratio = subordinate_markers / len(sentences)
        
        # Passive voice
        passive_count = self._count_passives(doc)
        verb_count = sum(1 for t in doc if t.pos_ == 'VERB')
        passive_ratio = passive_count / verb_count if verb_count > 0 else 0
        
        # Dependency tree depth (average)
        depths = [self._get_tree_depth(sent.root) for sent in sentences]
        avg_tree_depth = np.mean(depths) if depths else 0
        
        return {
            'avg_sentence_length': avg_sent_len,
            'subordination_ratio': subordination_ratio,
            'passive_ratio': passive_ratio,
            'avg_tree_depth': avg_tree_depth
        }
    
    def _register_markers(self, doc):
        """Extract register-specific markers"""
        total_tokens = len([t for t in doc if not t.is_punct])
        
        if total_tokens == 0:
            return {}
        
        # Modal particles (informal/spoken)
        particle_count = sum(1 for t in doc 
                           if t.lemma_.lower() in self.modal_particles)
        
        # Discourse connectives (formal/written)
        connective_count = sum(1 for t in doc 
                              if t.lemma_.lower() in self.connectives)
        
        # Nominalizations (-ung, -heit, -keit, -schaft endings)
        nominalization_suffixes = ['ung', 'heit', 'keit', 'schaft', 'tät', 'ion']
        nominalization_count = sum(
            1 for t in doc 
            if t.pos_ == 'NOUN' and 
            any(t.text.lower().endswith(suffix) for suffix in nominalization_suffixes)
        )
        
        return {
            'modal_particle_frequency': particle_count / total_tokens,
            'connective_frequency': connective_count / total_tokens,
            'nominalization_frequency': nominalization_count / total_tokens
        }
    
    def _count_passives(self, doc):
        """Count passive constructions (werden + past participle)"""
        passive_count = 0
        
        for i, token in enumerate(doc):
            if token.lemma_ == 'werden' and token.pos_ == 'AUX':
                # Look ahead for past participle
                for j in range(i+1, min(i+10, len(doc))):
                    if doc[j].tag_ in ['VVPP', 'VAPP']:  # Past participle tags
                        passive_count += 1
                        break
        
        return passive_count
    
    def _get_tree_depth(self, token, depth=0):
        """Calculate dependency tree depth recursively"""
        if not list(token.children):
            return depth
        return max(self._get_tree_depth(child, depth + 1) 
                  for child in token.children)
    
    def analyze_multiple_texts(self, texts, labels=None):
        """
        Analyze multiple texts and return feature DataFrame.
        
        Args:
            texts: List of text strings
            labels: Optional list of register labels
            
        Returns:
            pandas DataFrame with features for each text
        """
        results = []
        
        for i, text in enumerate(texts):
            features = self.extract_all_features(text)
            features['text_id'] = i
            
            if labels:
                features['register'] = labels[i]
            
            results.append(features)
        
        return pd.DataFrame(results)


def example_usage():
    """Demonstrate register feature extraction"""
    
    # Initialize analyzer
    analyzer = GermanRegisterAnalyzer()
    
    # Example texts from different registers
    texts = [
        # Academic
        """Die vorliegende Untersuchung beschäftigt sich mit der Analyse 
        morphosyntaktischer Strukturen in der deutschen Gegenwartssprache. 
        Es wird untersucht, inwieweit regionale Variation einen Einfluss 
        auf die Realisierung grammatischer Phänomene ausübt.""",
        
        # Colloquial
        """Also ich hab gestern mal wieder den Hans getroffen, weißt du. 
        Der hat mir erzählt, dass er jetzt nach München zieht. 
        Ist doch echt krass, oder? Hab ich gar nicht mit gerechnet.""",
        
        # Formal written
        """Sehr geehrte Damen und Herren, bezugnehmend auf Ihr Schreiben 
        vom 15. März möchten wir Ihnen mitteilen, dass Ihr Antrag 
        positiv beschieden wurde. Die entsprechenden Unterlagen werden 
        Ihnen in Kürze zugesandt."""
    ]
    
    labels = ['academic', 'colloquial', 'formal']
    
    # Extract features
    df = analyzer.analyze_multiple_texts(texts, labels)
    
    # Display results
    print("\nRegister Feature Analysis Results:")
    print("=" * 60)
    print(df.to_string())
    
    # Visualize key differences
    features_to_plot = [
        'avg_sentence_length', 
        'subordination_ratio',
        'modal_particle_frequency',
        'nominalization_frequency'
    ]
    
    df_plot = df[['register'] + features_to_plot].set_index('register')
    df_plot.T.plot(kind='bar', figsize=(10, 6))
    plt.title('Register Feature Comparison')
    plt.ylabel('Feature Value')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Register')
    plt.tight_layout()
    plt.savefig('register_comparison.png')
    print("\nVisualization saved as 'register_comparison.png'")


if __name__ == "__main__":
    example_usage()
