# counter
The Hash and Length Checker Tool allows users to calculate hashes of text, check if text has a specified length, and analyze text files for words of a given length. It supports finding duplicates and displaying word counts."
Hash and Length Checker Tool

The Hash and Length Checker Tool is a command-line utility written in Python that provides various functionalities for text analysis and file processing. It allows users to calculate hashes of text, check the length of text, and analyze text files for words of a specific length. The tool supports finding duplicates and displaying word counts.
Features:

    Calculate Hash: Calculate the hash value of a given text input.
    Check Text Length: Verify if a text string has a specified length.
    Check File Length: Analyze a text file to find words of a specified length.

Usage:

The tool can be invoked from the command line with the following options:

    Calculate Hash:

    arduino

python hash_checker.py calculate <text>

Example: python hash_checker.py calculate 'Hello'

Check Text Length:

php

python hash_checker.py checktextlength <text> <length>

Example: python hash_checker.py checktextlength 'Hello' 5

Check File Length:

php

    python hash_checker.py checkfilelength <file_path> <length> [num_words]

    Example: python hash_checker.py checkfilelength file.txt 32

    Optional: Specify num_words to output a specific number of words from the file.

Output:

    For hash calculation and text length checking, the tool provides a simple true/false result.
    For file length checking, the tool outputs the words found along with the number of duplicates (if any) and the total word count in the file.

Notes:

    Ensure the correct usage of quotes for text inputs containing spaces.
    For file paths, provide the absolute or relative path to the file.

Example Usage:

    Calculate the hash of a text:

    arduino

python hash_checker.py calculate 'Hello'

Check if a text has a specified length:

arduino

python hash_checker.py checktextlength 'Hello' 5

Analyze a text file for words of a specific length:

python hash_checker.py checkfilelength file.txt 32

Output 10 words from the file:

python hash_checker.py checkfilelength file.txt 32 10
