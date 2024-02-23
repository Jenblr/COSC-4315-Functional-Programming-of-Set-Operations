from argparse import ArgumentParser
import sys
sys.setrecursionlimit(10000)

# Lambda lowercase that uses recursive function to generate lowercase characters
l_toLower = lambda x: list(map(lambda word: l_toLowerHelper(word), x))
l_toLowerHelper = lambda word: ('' if not word else word[0] + l_toLowerHelper(word[1:])) if not word or not 'A' <= word[0] <= 'Z' else (chr(ord(word[0]) + 32) + l_toLowerHelper(word[1:]))

# Strips white space and removes symbols except for periods
l_replaceSymbols = lambda text,symbols: '' if not text else (' ' + l_replaceSymbols(text[1:],symbols)) if binarySearchRec(text[0], symbols, 0, None) else text[0] + l_replaceSymbols(text[1:],symbols)

# Recursive lambda function to remove periods and split where necessary
l_removePeriods = lambda item: [item] if not binarySearchRec('.', l_mergeSort(list(item)), 0, None) or l_isNum(item) else item.replace('.', ' ', 1).split()
l_isNum = lambda item: (item.replace('.', '', 1).isdigit() if item.count('.') == 1 and item[-1] != '.' else item.replace('.', '', 1).isdigit() or (item[:-1].isdigit() and item[-1] == '.'))

# Function to recursively process words in the list
l_processWords = lambda lst: [] if not lst else l_removePeriods(lst[0]) + l_processWords(lst[1:])

# Remove duplicates from a given list
l_removeDuplicates = lambda x: [] if not x else [x[0]] + l_removeDuplicates(list(filter(lambda y: y != x[0], x[1:])))

# Merge sort: Θ(n log(n))
l_merge = lambda left, right: left if not right else right if not left else [left[0]] + l_merge(left[1:], right) if str(left[0]) < str(right[0]) else [right[0]] + l_merge(left, right[1:])
l_mergeSort = lambda lst: lst if len(lst) <= 1 else l_merge(l_mergeSort(lst[:len(lst)//2]), l_mergeSort(lst[len(lst)//2:]))

# Recursive search algorithm for set operations
l_search = lambda f, lst: [] if not lst else [lst[0]] + l_search(f, lst[1:]) if f(lst[0]) else l_search(f, lst[1:])

# Recursive algorithm to check if a given value is in a list
def binarySearchRec(elem, arr, start, end):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return True
    if elem < arr[mid]:
        return binarySearchRec(elem, arr, start, mid-1)
    # elem > arr[mid]
    return binarySearchRec(elem, arr, mid+1, end)

# Intersection between 2 lists - and
l_intersect = lambda x, y: l_search(lambda element: binarySearchRec(element, y, 0, None), x)

# Union between 2 lists - or
l_union = lambda x, y: l_removeDuplicates(x + y)

# Difference - in x but not in y
l_difference = lambda x, y: l_search(lambda element: not binarySearchRec(element, y, 0, None), x)

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
    commonSymbols = l_mergeSort(["!", "?", "'", "\"", ",", "/", "\\", "~", "-", "(", ")", "\n", "\t", "\r", ";", ":", "[", "]", "{", "}", "+", "-", "&", "*", "%", "$", "@", "#", "^", "_", "=", "`", "<", ">", "|"])
    try: 
        with open(filename, 'r') as file:
            file_contents = file.read()
            print("File Contents:", file_contents)

            file_contents_copy = file_contents[:]

            text = l_removeDuplicates(l_toLower(l_processWords(l_replaceSymbols(file_contents_copy, commonSymbols).split())))
            print("Processed test:", text)
            return text
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Method to handle set operations
def handleOperations(set1, set2, operation):
    if operation == "union": return l_union(set1, set2)
    elif operation == "difference": return l_difference(set1, set2)
    elif operation == "intersection": return l_intersect(set1, set2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 setops.py <argument>")
        sys.exit(1)

    # Parse the command string
    try:
        input1, input2, operation = parseArguments()
    except (ValueError, FileNotFoundError) as e:
        print("Error parsing command string:", e)
        sys.exit(1)

    # Output the parsed arguments
    print(f"Input 1: {input1}")
    print(f"Input 2: {input2}")
    print(f"Operation: {operation}")

     # Validate the operation
    operations = l_mergeSort(["intersection", "union", "difference"])
    if not binarySearchRec(operation, operations, 0, None):
        print("Error: Invalid operation.")
        sys.exit(1)

    # Read input files
    set1 = l_mergeSort(readFile(input1))
    set2 = l_mergeSort(readFile(input2))

    # Perform set operations
    if set1 is None or set2 is None:
        print("Error reading input files.")
        sys.exit(1)

    try:
        result = handleOperations(set1, set2, operation)
    except ValueError as e:
        print("Error performing set operation:", e)
        sys.exit(1)

    # Check if the result is empty for intersection or union
    if operation == "intersection" and not result:
        result = ["empty set"]
    elif operation == "union" and not result:
        result = ["empty set"]
    elif operation == "difference" and not result:
        result = ["all elements in set A are in B"]

    # Recursively sort the result: numbers first, then words alphabetically
    sorted_result = l_mergeSort(result)

    print("Result:", sorted_result)

    # Output to result.txt file
    try: 
        with open("result.txt", "w") as file:
            for word in sorted_result:
                file.write(word + "\n")
    except IOError as e:
        print("Error writing to file", e)
        sys.exit(1)
        
if __name__ == '__main__':
    main()