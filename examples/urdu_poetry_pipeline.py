"""
urdu_poetry_pipeline.py
Professional Data Pipeline for Urdu Poetry Corpus

A clean, production-ready pipeline demonstrating Urdu text
processing for Digital Humanities research.
"""

import os

class UrduPoetryPipeline:
    """End-to-end pipeline for Urdu poetry processing."""
    
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
        self.stats = {}
    
    def run(self, input_file):
        """Execute complete pipeline."""
        print("=" * 60)
        print("URDU POETRY DATA PIPELINE")
        print("=" * 60)
        
        # 1. INGEST: Read with UTF-8 encoding
        print("\n1. INGEST PHASE")
        print("-" * 30)
        with open(input_file, 'r', encoding=self.encoding) as f:
            content = f.read()
        print(f"File loaded: {len(content)} characters")
        
        # 2. PROCESS: Extract lines
        print("\n2. PROCESS PHASE")
        print("-" * 30)
        lines = content.split('\n')
        print(f"Lines extracted: {len(lines)}")
        
        # 3. CLEAN: Remove whitespace and empty lines
        print("\n3. CLEAN PHASE")
        print("-" * 30)
        clean_lines = [line.strip() for line in lines if line.strip()]
        print(f"Cleaned lines: {len(clean_lines)}")
        
        # 4. ANALYZE: Basic statistics
        print("\n4. ANALYZE PHASE")
        print("-" * 30)
        all_words = ' '.join(clean_lines).split()
        self.stats = {
            'total_lines': len(clean_lines),
            'total_words': len(all_words),
            'unique_words': len(set(all_words)),
            'avg_line_length': sum(len(l) for l in clean_lines) / len(clean_lines) if clean_lines else 0
        }
        
        print(f"Total lines: {self.stats['total_lines']}")
        print(f"Total words: {self.stats['total_words']}")
        print(f"Unique words: {self.stats['unique_words']}")
        print(f"Average line length: {self.stats['avg_line_length']:.1f} characters")
        
        # 5. OUTPUT: Save results
        print("\n5. OUTPUT PHASE")
        print("-" * 30)
        output_file = "processed_corpus.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(clean_lines))
        print(f"Cleaned corpus saved to: {output_file}")
        
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETE")
        print("=" * 60)
        
        return clean_lines, self.stats

def demonstrate():
    """Demonstrate the pipeline."""
    
    # Find sample file
    sample_file = "../data/sample_ghazal.txt"
    
    if os.path.exists(sample_file):
        pipeline = UrduPoetryPipeline()
        cleaned_data, stats = pipeline.run(sample_file)
        
        print("\nDIGITAL HUMANITIES APPLICATIONS")
        print("-" * 40)
        print("Cultural heritage digitization")
        print("Literary corpus management")
        print("Computational text analysis")
        print("Digital archive preparation")
        
        return cleaned_data, stats
    else:
        print(f"Sample file not found: {sample_file}")
        return None, None

if __name__ == "__main__":
    # Run demonstration
    data, statistics = demonstrate()
    
    if data:
        print(f"\nSAMPLE OF PROCESSED DATA")
        print("-" * 30)
        for i, line in enumerate(data[:3], 1):
            print(f"Line {i}: {line}")
