#!/usr/bin/env python

import sys
import io
from collections import Counter

def calculate_hash(text):
    """Calculate hash of the given text."""
    return hash(text)

def check_text_length(text, length):
    """Check if the given text has the specified length."""
    return len(text) == int(length)

def check_file_length(file_path, length, num_words=None):
    """Check if the given file contains words of the specified length."""
    words_with_duplicates = []
    try:
        with io.open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if len(word) == int(length):
                        words_with_duplicates.append(word)
    except IOError:
        print("Error: File '{}' not found.".format(file_path))
        return []

    word_counts = Counter(words_with_duplicates)
    words = list(word_counts.keys())
    if num_words is None:
        return words, word_counts
    else:
        return words[:num_words], word_counts

def display_usage():
    """Display usage information."""
    print("Welcome to Hash and Length Checker Tool")
    print("Options:")
    print("1. calculate <text>")
    print("   Example: calculate 'Hello'")
    print("2. checktextlength <text> <length>")
    print("   Example: checktextlength 'Hello' 5")
    print("3. checkfilelength <file_path> <length> [<num_words>]")
    print("   Example: checkfilelength file.txt 5 10 (to output 10 words)")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        display_usage()
        sys.exit(0)

    option = sys.argv[1]
    arguments = sys.argv[2:]

    if option == "calculate":
        if len(arguments) < 1:
            print("Error: Missing text argument.")
            sys.exit(1)
        text = arguments[0]
        result = calculate_hash(text)
        print("Hash of '{}' is: {}".format(text, result))
    
    elif option == "checktextlength":
        if len(arguments) < 2:
            print("Error: Missing text or length argument.")
            sys.exit(1)
        text = arguments[0]
        length = arguments[1]
        result = check_text_length(text, length)
        print("Text '{}' has length {}? {}".format(text, length, result))

    elif option == "checkfilelength":
        if len(arguments) < 2:
            print("Error: Missing file path or length argument.")
            sys.exit(1)
        file_path = arguments[0]
        length = arguments[1]
        num_words = int(arguments[2]) if len(arguments) >= 3 and arguments[2].isdigit() else None
        words, word_counts = check_file_length(file_path, length, num_words)
        if num_words is None:
            if words:
                print("File '{}' contains the following words of length {} with their counts:".format(file_path, length))
                for word in words:
                    print("{} ({})".format(word, word_counts[word]))
            else:
                print("File '{}' does not contain any words of length {}.".format(file_path, length))
        else:
            if words:
                print("File '{}' contains the following words of length {} ({} out of {}):".format(file_path, length, min(num_words, len(words)), len(words)))
                for word in words:
                    print("{} ({})".format(word, word_counts[word]))
            else:
                print("File '{}' does not contain any words of length {}.".format(file_path, length))

if __name__ == "__main__":
    main()
