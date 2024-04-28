#!/usr/bin/python3
"""0. Start a script"""

import sys
import markdown2html
if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    filename_input = sys.argv[1]
    filename_output = sys.argv[2]

    try:
        with open(filename_input, 'r') as f:
            markedown_content = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Missing {filename_input}\n")
        sys.exit(1)
    sys.exit(0)
