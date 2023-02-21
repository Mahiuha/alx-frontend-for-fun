#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import sys
import markdown

def main():
    """
    Main function to convert a Markdown file to HTML.
    """
    # Check if the correct number of arguments were passed in
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py [input_file] [output_file]\n")
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    try:
        with open(input_file, 'r') as f:
            pass
    except FileNotFoundError:
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Convert the Markdown to HTML
    with open(input_file, 'r') as f:
        html = markdown.markdown(f.read())

    # Write the HTML to the output file
    with open(output_file, 'w') as f:
        f.write(html)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()

