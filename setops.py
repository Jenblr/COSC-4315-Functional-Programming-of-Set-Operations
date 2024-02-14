from argparse import ArgumentParser
import sys
sys.setrecursionlimit(10000)

# Lambda lowercase that uses recursive function to generate lowercase characters
l_toLower = lambda x: list(map(lambda word: l_toLowerHelper(word), x))
l_toLowerHelper = lambda word: ('' if not word else word[0] + l_toLowerHelper(word[1:])) if not word or not 'A' <= word[0] <= 'Z' else (chr(ord(word[0]) + 32) + l_toLowerHelper(word[1:]))

# Strips white space and removes symbols except for periods
l_replaceSymbols = lambda text,symbols: '' if not text else (' ' + l_replaceSymbols(text[1:],symbols)) if text[0] in symbols else text[0] + l_replaceSymbols(text[1:],symbols)

# Recursive lambda function to remove periods and split where necessary
l_removePeriods = lambda item: [item] if '.' not in item or l_isNum(item) else item.replace('.', ' ', 1).split()
l_isNum = lambda item: (item.replace('.', '', 1).isdigit() if item.count('.') == 1 and item[-1] != '.' else item.isdigit()) if item.count('.') <= 1 else False

# Function to recursively process words in the list
l_processWords = lambda lst: [] if not lst else l_removePeriods(lst[0]) + l_processWords(lst[1:])

# Remove duplicates from a given list
l_removeDuplicates = lambda x: [] if not x else [x[0]] + l_removeDuplicates(list(filter(lambda y: y != x[0], x[1:])))

# Merge sort
l_merge = lambda left, right: left if not right else right if not left else [left[0]] + l_merge(left[1:], right) if left[0] < right[0] else [right[0]] + l_merge(left, right[1:])
l_mergeSort = lambda lst: lst if len(lst) <= 1 else l_merge(l_mergeSort(lst[:len(lst)//2]), l_mergeSort(lst[len(lst)//2:]))

# Intersection between 2 lists
ll_intersect = lambda x, y: [] if not x else [x[0]] + ll_intersect(x[1:], y) if x[0] in y else ll_intersect(x[1:], y)
l_intersect = lambda x, y: list(filter(lambda z: z in x, y))

# Union between 2 lists
l_union = lambda x, y: l_removeDuplicates(x + y)

# TODO: Difference between two lists
# l_difference = lambda x, y: list(filter(lambda z: z in x and z not in y))
def difference(list1, list2):
    return []

def parseArguments():
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Process set operations.')

    # Add an argument for the command string
    parser.add_argument('command', type=str, help='Command string containing set1, set2, and operation.')

    # Parse the arguments
    args = parser.parse_args()
    # Split the command string by semicolons to get individual arguments
    arguments = args.command.split(';')
    
    # Initialize variables to store set names and operation
    set1, set2, operation = None, None, None
    
    # Iterate over each argument and parse it
    for arg in arguments:
        key, value = arg.split('=')
        if key == 'set1':
            set1 = value
        elif key == 'set2':
            set2 = value
        elif key == 'operation':
            operation = value
    
    return set1, set2, operation

# Recursive function to read input files and parse words
def readFile(filename):
    commonSymbols = ["!", "?", "'", "\"", ",", "/", "\\", "~", "-", "(", ")", "\n", "\t", "\r", ";", ":", "[", "]", "{", "}", "+", "-", "&", "*", "%", "$", "@", "#", "^", "_", "=", "`", "<", ">", "|"]
    try: 
        with open(filename, 'r') as file:
            file_contents = file.read()
            print(file_contents)
            text = l_removeDuplicates(l_toLower(l_processWords(l_replaceSymbols(file_contents, commonSymbols).split())))
            return text
    except FileNotFoundError:
        print(f"Error: File not found: %s" % filename)
        return []

# Method to handle set operations
def handleOperations(set1, set2, operation):
    if operation == "union": return l_union(set1, set2)
    elif operation == "difference": return difference(set1, set2)
    elif operation == "intersection": return l_intersect(set1, set2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 setops.py <argument>")
        sys.exit(1)

    # Parse the command string
    input1, input2, operation = parseArguments()

    # Output the parsed arguments
    print(f"Input 1: {input1}")
    print(f"Input 2: {input2}")
    print(f"Operation: {operation}")

    # Read input files
    set1 = readFile(input1)
    print(set1)
    
    set2 = readFile(input2)
    print(set2)

    # TODO: Output to result.txt file
    print(l_mergeSort(handleOperations(set1, set2, operation)))

if __name__ == '__main__':
    main();