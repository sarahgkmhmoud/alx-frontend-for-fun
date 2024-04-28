#!/usr/bin/python3
"""0. Start a script"""

import sys
import markdown
if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    filename_input = sys.argv[1]
    filename_output = sys.argv[2]

    try:
        with open(filename_input, 'r') as f:
            markedown_content = f.read()
            html_content = markdown.markdown(markedown_content)
    except FileNotFoundError:
        sys.stderr.write(f"Missing {filename_input}\n")
        sys.exit(1)
    
    with open(filename_output, 'w') as file:
        file.write(html_content)
    sys.exit(0)
