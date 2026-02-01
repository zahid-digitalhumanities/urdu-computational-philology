"""
quantitative_literary_analysis.py
Quantitative Literary Analysis of Urdu Poetry

Applies computational methods to analyze classical Urdu poetry
using frequency analysis to reveal thematic patterns and stylistic features.

Implements the analytical framework from:
Zahid, M. (2026). Computational Framework for the Descriptive Analysis 
and Digital Preservation of Classical Urdu Poetry.
Liberal Journal of Language & Literature Review, 4(1).
"""

import re
from collections import Counter

def tokenize_urdu_text(text):
    """
    Tokenize Urdu text with punctuation handling.
    
    Args:
        text (str): Urdu text to tokenize
        
    Returns:
        list: Tokenized words (punctuation removed)
    """
    # Remove Urdu/Arabic punctuation and split
    cleaned = re.sub(r'[۔،؛؟!,.؟!]', ' ', text)
    tokens = cleaned.split()
    return tokens

def analyze_word_frequencies(text):
    """
    Perform comprehensive word frequency analysis.
    
    Args:
        text (str): Urdu text to analyze
        
    Returns:
        dict: Complete analysis results
    """
    tokens = tokenize_urdu_text(text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    
    # Calculate frequencies
    frequencies = Counter(tokens)
    
    # Calculate Type-Token Ratio (lexical richness)
    ttr = unique_words / total_words if total_words > 0 else 0
    
    # Find most common words
    most_common = frequencies.most_common(5)
    
    return {
        'tokens': tokens,
        'total_words': total_words,
        'unique_words': unique_words,
        'frequencies': dict(frequencies),
        'type_token_ratio': ttr,
        'most_common_words': most_common
    }

def interpret_literary_significance(frequencies):
    """
    Provide literary interpretation of frequency results.
    
    Args:
        frequencies (dict): Word frequency dictionary
        
    Returns:
        dict: Literary interpretations
    """
    interpretations = {
        'ہے': 'Existential themes, being/identity - central to Urdu poetic discourse',
        'غم': 'Sorrow, melancholy - foundational in Ghalib\'s poetic universe',
        'دل': 'Heart, emotion - core of romantic and spiritual expression',
        'عشق': 'Love, passion - primary theme in Urdu ghazal tradition',
        'خدا': 'Divine, God - spiritual and metaphysical dimensions',
        'زندگی': 'Life, existence - philosophical contemplation',
        'موت': 'Death, mortality - recurring memento mori theme',
        'آشنا': 'Beloved, familiar - central to love poetry',
        'سجدہ': 'Prostration, prayer - spiritual devotion',
        'جام': 'Wine cup - symbol of intoxication (literal and spiritual)'
    }
    
    significant_words = []
    for word, count in frequencies.items():
        if word in interpretations:
            significant_words.append({
                'word': word,
                'count': count,
                'interpretation': interpretations[word]
            })
    
    return significant_words

def analyze_ghalib_couplet():
    """
    Demonstrate analysis with a classic Ghalib couplet.
    """
    couplet = "غم ہے یا مسیحا کا نشہ ہے کوئی بات ہے غم ہے یا مسیحا کا نشہ ہے"
    
    print("=" * 70)
    print("QUANTITATIVE LITERARY ANALYSIS OF URDU POETRY")
    print("=" * 70)
    
    print(f"\nاصل شعر (Original Couplet):")
    print(f"\"{couplet}\"")
    
    # Tokenize
    tokens = tokenize_urdu_text(couplet)
    print(f"\nالفاظ کی فہرست (Tokens): {tokens}")
    
    # Analyze frequencies
    analysis = analyze_word_frequencies(couplet)
    
    print(f"\nلفظ گنتی کے نتائج (Word Frequency Results):")
    for word, count in sorted(analysis['frequencies'].items()):
        print(f"  '{word}': {count}")
    
    print(f"\nکل الفاظ (Total words): {analysis['total_words']}")
    print(f"منفرد الفاظ (Unique words): {analysis['unique_words']}")
    print(f"الفاظ کا تناسب (Type-Token Ratio): {analysis['type_token_ratio']:.3f}")
    
    # Literary interpretation
    print("\n" + "-" * 70)
    print("FREQUENCY ANALYSIS WITH LITERARY INTERPRETATION")
    print("-" * 70)
    
    significant = interpret_literary_significance(analysis['frequencies'])
    
    print(f"\n{'Word':<10} {'Frequency':<12} {'Literary Significance':<45}")
    print("-" * 70)
    
    for item in significant:
        print(f"{item['word']:<10} {item['count']:<12} {item['interpretation']:<45}")
    
    # Most common words analysis
    print("\n" + "-" * 70)
    print("MOST FREQUENT WORDS (Top 5):")
    print("-" * 70)
    
    for word, count in analysis['most_common_words']:
        print(f"  '{word}': {count}x")
    
    return analysis

def demonstrate_thematic_analysis():
    """
    Demonstrate thematic pattern discovery through repetition analysis.
    """
    print("\n" + "=" * 70)
    print("THEMATIC PATTERN DISCOVERY")
    print("=" * 70)
    
    couplet = "غم ہے یا مسیحا کا نشہ ہے کوئی بات ہے غم ہے یا مسیحا کا نشہ ہے"
    
    # Find repeated phrases
    words = couplet.split()
    repeated_phrases = []
    
    # Look for 2-word phrase repetition
    for i in range(len(words) - 1):
        phrase = f"{words[i]} {words[i+1]}"
        if couplet.count(phrase) > 1 and phrase not in repeated_phrases:
            repeated_phrases.append(phrase)
    
    print("\nRepetition Analysis:")
    print(f"Couplet: \"{couplet}\"")
    
    if repeated_phrases:
        print(f"\nRepeated phrases found:")
        for phrase in repeated_phrases:
            count = couplet.count(phrase)
            print(f"  \"{phrase}\": {count} times")
        
        print("\nTHEMATIC INTERPRETATION:")
        print("The repetition of 'غم ہے یا مسیحا کا نشہ' (2x) reveals:")
        print("• Structural parallelism characteristic of classical ghazal")
        print("• Tension between sorrow (غم) and spiritual ecstasy (مسیحا کا نشہ)")
        print("• Philosophical inquiry into human condition")
        print("• Binary opposition central to Ghalib's poetic thought")
    else:
        print("\nNo significant phrase repetition detected.")
    
    print("\nCOMPUTATIONAL INSIGHT:")
    print("Quantitative analysis reveals both structural patterns (repetition)")
    print("and thematic depth (sorrow vs. redemption), demonstrating how")
    print("computational methods can uncover literary richness.")

def generate_analysis_report(analysis, filename="analysis_report.txt"):
    """
    Generate a comprehensive analysis report.
    
    Args:
        analysis (dict): Analysis results
        filename (str): Output filename
    """
    report = []
    report.append("=" * 70)
    report.append("URDU POETRY QUANTITATIVE ANALYSIS REPORT")
    report.append("=" * 70)
    report.append("")
    report.append(f"Total words analyzed: {analysis['total_words']}")
    report.append(f"Unique vocabulary: {analysis['unique_words']}")
    report.append(f"Lexical richness (TTR): {analysis['type_token_ratio']:.3f}")
    report.append("")
    report.append("WORD FREQUENCY DISTRIBUTION:")
    report.append("-" * 70)
    
    for word, count in sorted(analysis['frequencies'].items(), 
                             key=lambda x: x[1], reverse=True):
        report.append(f"  {word:<15} {count:>3}")
    
    report.append("")
    report.append("RESEARCH METHODOLOGY:")
    report.append("This analysis implements the computational framework")
    report.append("described in: Zahid, M. (2026). Computational Framework")
    report.append("for the Descriptive Analysis and Digital Preservation")
    report.append("of Classical Urdu Poetry. Liberal Journal of Language")
    report.append("& Literature Review, 4(1).")
    
    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"\n✓ Analysis report saved to: {filename}")

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DIGITAL HUMANITIES: QUANTITATIVE LITERARY ANALYSIS")
    print("Computational Philology Toolkit - Research Module")
    print("=" * 70)
    
    # Run comprehensive analysis
    analysis_results = analyze_ghalib_couplet()
    demonstrate_thematic_analysis()
    
    # Generate report
    generate_analysis_report(analysis_results)
    
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE - KEY FINDINGS:")
    print("=" * 70)
    print("\n1. Quantitative Methods:")
    print("   • Word frequency analysis reveals thematic emphasis")
    print("   • Type-Token Ratio measures lexical diversity")
    print("   • Pattern detection identifies structural features")
    
    print("\n2. Literary Insights:")
    print("   • Repetition analysis uncovers poetic structure")
    print("   • Frequency patterns highlight central themes")
    print("   • Computational methods complement close reading")
    
    print("\n3. Research Applications:")
    print("   • Scalable analysis of large corpora")
    print("   • Comparative stylometry across poets")
    print("   • Digital preservation through quantitative profiling")
    
    print("\n" + "=" * 70)
    print("READY FOR INTEGRATION INTO LARGER RESEARCH PIPELINE")
    print("=" * 70)
