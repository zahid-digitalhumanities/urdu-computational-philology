"""
simple_file_handling.py
Basic File Handling for Urdu Text

Demonstrates fundamental file operations for Urdu poetry corpus.
Shows proper encoding handling for right-to-left scripts.
"""

import os

def demonstrate_basic_reading():
    """Demonstrate basic file reading operations."""
    
    print("=" * 60)
    print("BASIC URDU FILE HANDLING")
    print("=" * 60)
    
    # First, let's check what files are available
    data_dir = "../data"
    print(f"\nChecking data directory: {data_dir}")
    
    if os.path.exists(data_dir):
        files = os.listdir(data_dir)
        print(f"Available files in data directory:")
        for file in files:
            filepath = os.path.join(data_dir, file)
            size = os.path.getsize(filepath)
            print(f"  • {file} ({size} bytes)")
    else:
        print("Data directory not found!")
        return
    
    print("\n" + "-" * 60)
    print("DEMONSTRATION 1: Reading Entire File")
    print("-" * 60)
    
    # Read the sample ghazal file
    sample_file = os.path.join(data_dir, "sample_ghazal.txt")
    
    if os.path.exists(sample_file):
        print(f"\nStep 1: Opening file for reading")
        print(f"File: {sample_file}")
        print("Mode: 'r' (read)")
        print("Encoding: 'utf-8' (standard for Urdu text)")
        
        # Step 1: Open the file for reading
        with open(sample_file, 'r', encoding='utf-8') as file:
            # Step 2: Read the entire content
            content = file.read()
        
        # Step 3: Display the content
        print("\nStep 2: File content loaded successfully!")
        print("\nStep 3: Displaying content:")
        print("-" * 40)
        print(content)
        print("-" * 40)
        
        # Show statistics
        print(f"\nFile Statistics:")
        print(f"Total characters: {len(content)}")
        print(f"Total lines: {content.count(chr(10)) + 1}")
        print(f"File size: {os.path.getsize(sample_file)} bytes")
    else:
        print(f"File not found: {sample_file}")

def demonstrate_line_by_line():
    """Demonstrate reading file line by line."""
    
    print("\n" + "-" * 60)
    print("DEMONSTRATION 2: Reading Line by Line")
    print("-" * 60)
    
    sample_file = "../data/sample_ghazal.txt"
    
    if os.path.exists(sample_file):
        print(f"\nReading: {sample_file}")
        print("Method: readline() for controlled reading")
        
        with open(sample_file, 'r', encoding='utf-8') as file:
            print("\nFirst 3 lines:")
            for i in range(3):
                line = file.readline()
                if line:
                    print(f"Line {i+1}: {line.strip()}")
                else:
                    break
        
        # Alternative: read all lines at once
        print("\nAlternative: readlines() method")
        with open(sample_file, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            print(f"Total lines read: {len(all_lines)}")
            
            # Show with and without newline characters
            print("\nComparison: With and without newline characters")
            print(f"First line with newline: '{all_lines[0]}'")
            print(f"First line stripped: '{all_lines[0].strip()}'")

def demonstrate_different_encodings():
    """Demonstrate different encoding options."""
    
    print("\n" + "-" * 60)
    print("DEMONSTRATION 3: Understanding Encodings")
    print("-" * 60)
    
    print("\nCommon encodings for Urdu text:")
    print("1. 'utf-8'       - Standard Unicode encoding (recommended)")
    print("2. 'utf-8-sig'   - UTF-8 with BOM (Byte Order Mark)")
    print("3. 'utf-16'      - UTF-16 encoding")
    print("4. 'cp1256'      - Windows Arabic encoding")
    
    print("\nWhy 'utf-8' is recommended for Urdu:")
    print("• Supports all Urdu characters")
    print("• Compatible across platforms")
    print("• Most web standards use UTF-8")
    print("• Works with Python string operations")

def create_sample_output():
    """Create a sample output file."""
    
    print("\n" + "-" * 60)
    print("DEMONSTRATION 4: Writing to File")
    print("-" * 60)
    
    output_file = "urdu_sample_output.txt"
    
    # Sample Urdu text to write
    sample_text = """مرزا غالب کا شعر:
غم ہیں یا وصال کا شہ ہے
دل ہی تو ہے نہ سنگ و خشت"""

    print(f"\nStep 1: Creating output file: {output_file}")
    print("Mode: 'w' (write)")
    print("Encoding: 'utf-8'")
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(sample_text)
    
    print(f"\nStep 2: File written successfully!")
    print(f"File size: {os.path.getsize(output_file)} bytes")
    
    # Read it back to verify
    print("\nStep 3: Verifying by reading back:")
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\nContent read back:")
        print("-" * 30)
        print(content)
        print("-" * 30)

def summarize_learning():
    """Summarize what was learned."""
    
    print("\n" + "=" * 60)
    print("LEARNING SUMMARY")
    print("=" * 60)
    
    print("\nKey Concepts Demonstrated:")
    print("1. File opening modes: 'r' (read), 'w' (write)")
    print("2. Encoding handling for Urdu: 'utf-8'")
    print("3. Reading methods: read(), readline(), readlines()")
    print("4. File path management with os.path")
    print("5. Basic file statistics (size, lines, characters)")
    
    print("\nDigital Humanities Applications:")
    print("• Loading poetry corpora for analysis")
    print("• Preparing text data for computational methods")
    print("• Creating processed outputs for archives")
    print("• Ensuring encoding consistency in research pipelines")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("URDU TEXT FILE HANDLING WORKSHOP")
    print("Fundamental Skills for Digital Humanities")
    print("=" * 60)
    
    # Run all demonstrations
    demonstrate_basic_reading()
    demonstrate_line_by_line()
    demonstrate_different_encodings()
    create_sample_output()
    summarize_learning()
    
    print("\n" + "=" * 60)
    print("WORKSHOP COMPLETE")
    print("=" * 60)
    print("\nNext Steps:")
    print("• Try with larger corpus files")
    print("• Experiment with different encodings")
    print("• Combine with text processing modules")
    print("• Apply to your research datasets")
