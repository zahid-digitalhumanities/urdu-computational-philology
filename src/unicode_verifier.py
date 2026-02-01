#!/usr/bin/env python3
"""
unicode_verifier.py
UTF-8 validation and verification for Urdu Nastaliq script.

This module ensures proper encoding handling for Urdu text processing,
addressing common issues in right-to-left (RTL) text workflows.
"""


class UnicodeVerifier:
    """Validates and inspects UTF-8 encoded Urdu text."""
    
    def verify(self, text: str) -> dict:
        """
        Comprehensive verification of Urdu text encoding.
        
        Args:
            text (str): Input Urdu text string
            
        Returns:
            dict: Verification results with detailed metrics
        """
        results = {
            "text": text,
            "length_chars": len(text),
            "length_bytes": len(text.encode('utf-8')),
            "encoding": "UTF-8",
            "valid": True,
            "rtl_check": self._check_rtl(text)
        }
        
        # UTF-8 validation
        try:
            text.encode('utf-8')
            results["encoding_status"] = "✓ Valid UTF-8"
        except UnicodeEncodeError:
            results["encoding_status"] = "✗ Invalid UTF-8 encoding"
            results["valid"] = False
        
        return results
    
    def _check_rtl(self, text: str) -> dict:
        """Check RTL-specific properties."""
        urdu_chars = sum(1 for c in text if '\u0600' <= c <= '\u06ff')
        
        return {
            "urdu_char_count": urdu_chars,
            "urdu_percentage": (urdu_chars / len(text)) * 100 if text else 0,
        }
    
    def print_report(self, results: dict):
        """Print a formatted verification report."""
        print("=" * 50)
        print("URDU TEXT VERIFICATION REPORT")
        print("=" * 50)
        print(f"Text: {results['text']}")
        print(f"Characters: {results['length_chars']}")
        print(f"Bytes (UTF-8): {results['length_bytes']}")
        print(f"Encoding: {results['encoding_status']}")
        
        rtl = results['rtl_check']
        print(f"Urdu Characters: {rtl['urdu_char_count']} ({rtl['urdu_percentage']:.1f}%)")
        print("=" * 50)


def verify_text(text: str):
    """Convenience function for quick verification."""
    verifier = UnicodeVerifier()
    results = verifier.verify(text)
    verifier.print_report(results)
    return results


if __name__ == "__main__":
    # Example usage
    sample = "غم ہیں یا وصال کا شہ ہے"
    print("Example: Verifying Urdu Text")
    verify_text(sample)
