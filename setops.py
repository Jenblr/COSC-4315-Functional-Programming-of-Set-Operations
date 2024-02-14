import re
import sys

# Recursive function to read input files and parse words
def read_file(filename):
    try: 
        with open(filename, 'r') as file:
            file_contents = file.read()

            # Extract words while separating digits
            words = re.findall(r'\b(?:\w+|\d+)\b', file_contents)
            # Convert words to lowercase recursively
            words = list(map(lambda word : word.lower(), words))

            return words
    except FileNotFoundError:
        print(f"Error: File not found: %s" % filename)
        return []

def main():
    # Check if correct number of command line arguments are given
    if len(sys.argv) != 2:
        print("Usage: python setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        sys.exit(1)

    # Parse command line arguments
    try:
        args = sys.argv[1].split(';')
        set1 = args[0].split('=')[1]
        set2 = args[1].split('=')[1]
        operation = args[2].split('=')[1]
        
        if operation not in ['difference', 'union', 'intersection']:
            raise ValueError("Invalid operation specified")
        
    except IndexError:
        print("Invalid command line arguments.")
        sys.exit(1)

    # Read input files
    fileA = read_file(set1)
    fileB = read_file(set2)

if __name__ == '__main__':
    main()