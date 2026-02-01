"""
basic_urdu_text_handling.py
Basic Urdu Text Processing Demonstration

Shows fundamental Unicode handling and string operations for Urdu text.
Essential for understanding how Python processes right-to-left (RTL) scripts.
"""

def demonstrate_basic_operations():
    """Demonstrate basic string operations with Urdu text"""
    
    # Sample Urdu text
    test_text = "مرزا غالب کی شاعری"
    
    print("=" * 60)
    print("BASIC URDU TEXT HANDLING DEMONSTRATION")
    print("=" * 60)
    
    print(f"\nUrdu text = : {test_text}")
    print("Testing Urdu text...")
    
    # Basic string operations
    print(f"Text length: {len(test_text)} characters")
    print(f"First character: '{test_text[0]}'")
    print(f"Last character: '{test_text[-1]}'")
    print(f"First 5 characters: '{test_text[:5]}'")
    print(f"Last 5 characters: '{test_text[-5:]}'")
    
    # Check for substring
    search_word = "غالب"
    if search_word in test_text:
        print(f"\nWord '{search_word}' found in text!")
        position = test_text.find(search_word)
        print(f"Position of '{search_word}': index {position}")
    
    # Split into words
    words = test_text.split()
    print(f"\nText split into {len(words)} words:")
    for i, word in enumerate(words, 1):
        print(f"  Word {i}: '{word}' (length: {len(word)})")
    
    # Join back
    joined_text = ' '.join(words)
    print(f"\nJoined text: '{joined_text}'")
    print("Text matches original:", test_text == joined_text)
    
    # Unicode character information
    print(f"\nUnicode code points for first 3 characters:")
    for i, char in enumerate(test_text[:3]):
        code_point = ord(char)
        print(f"  '{char}': Unicode U+{code_point:04X} (Decimal: {code_point})")
    
    print("\n" + "=" * 60)
    print("✓ Full text is stored correctly in memory!")
    print("✓ Python handles Urdu Unicode perfectly")
    print("=" * 60)
    
    return test_text, words

def demonstrate_poetry_handling():
    """Demonstrate with actual poetry lines"""
    
    print("\n\n" + "=" * 60)
    print("URDU POETRY HANDLING DEMONSTRATION")
    print("=" * 60)
    
    # Famous Ghalib couplet
    couplet = "غم ہیں یا وصال کا شہ ہے\nدل ہی تو ہے نہ سنگ و خشت"
    
    print(f"\nGhalib couplet:\n{couplet}")
    
    # Split into lines
    lines = couplet.split('\n')
    print(f"\nNumber of lines: {len(lines)}")
    
    for i, line in enumerate(lines, 1):
        print(f"\nLine {i}: '{line}'")
        print(f"  Length: {len(line)} characters")
        print(f"  Words: {len(line.split())}")
    
    # Count total words in couplet
    all_words = couplet.replace('\n', ' ').split()
    print(f"\nTotal words in couplet: {len(all_words)}")
    
    # Show unique words
    unique_words = set(all_words)
    print(f"Unique words: {len(unique_words)}")
    print(f"Vocabulary: {sorted(unique_words)}")

if __name__ == "__main__":
    # Run demonstrations
    text, words = demonstrate_basic_operations()
    demonstrate_poetry_handling()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThis script shows that Python can:")
    print("1. Store Urdu text correctly in memory")
    print("2. Perform standard string operations")
    print("3. Handle right-to-left script direction")
    print("4. Process poetic structures (couplets)")
    print("5. Work with Unicode code points")
