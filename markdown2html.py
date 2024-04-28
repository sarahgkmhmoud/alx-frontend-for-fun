#!/usr/bin/python3
"""0. Start a script"""

import sys 
import markdown2html
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    filename_input = sys.argv[1]
    filename_output = sys.argv[2]

    try:
        with open (filename_input, 'r') as f:
            markedown_content = f.read()
    except  FileNotFoundError:
        print(f"Missing {filename_input}")
        sys.exit(1)
    sys.exit(0)
