from argparse import ArgumentParser
import sys
sys.setrecursionlimit(10000)

# Utils
def splitRec(x, y):
    if x.find(y) == -1 or len(x) <= 1:
        return [x]
    elif x.find(y) == len(x)-1:
        return [x[:x.find(y)]]
    elif y == '':
        if len(x) == 1:
            return [x]
        return [x[x.find(y)]] + splitRec(x[x.find(y)+1:], y)
    elif x.find(y) == 0:
        return [] + splitRec(x[x.find(y)+1:], y)
    else:
        return [x[:x.find(y)]] + splitRec(x[x.find(y)+1:], y)

# Lambda lowercase that uses recursive function to generate lowercase characters
l_toLower = lambda x: list(map(lambda word: l_toLowerHelper(word), x))
l_toLowerHelper = lambda word: ('' if not word else word[0] + l_toLowerHelper(word[1:])) if not word or not 'A' <= word[0] <= 'Z' else (chr(ord(word[0]) + 32) + l_toLowerHelper(word[1:]))

# Strips white space and removes symbols except for periods
l_replaceSymbols = lambda text, symbols: '' if not text else (' ' + l_replaceSymbols(text[1:],symbols)) if seqSearchRec(text[0], symbols) else text[0] + l_replaceSymbols(text[1:], symbols)

# Checks if a string contains a mixture of characters and digits
l_checkString = lambda text: all(map(lambda c: c.isalpha(), text)) or all(map(lambda c: c.isdigit(), text))

# Split numbers and words from a string
l_splitNumbersWords = lambda text: [text] if l_checkString(text) else splitStringRec(text, [], '')

# Define a recursive function to split the string into words and digits: Example: test2right35below
def splitStringRec(string, result=[], current=''):
    # Base case: if the string is empty, add the current word or digit to the result list and return it
    if not string:
        if l_isNum(current):
            result.append(current)
        elif current.isalpha():
            result.append(current)
        else:
            if current[0] == '.' and current[-1] == '.':
                temp = current[1:-1]
                if temp:
                    result.append(current[1:-1])
            elif current[0] == '.':
                result.append(current[1:])
            else:
                if len(current) != 0:
                    result.append(current[:-1])
        return result

    if l_isNum(current) and not l_isNum(current + string[0]):
        result.append(current)
        newstr = string[1:] if len(string) > 1 and string[0] == '.' else string
        string = newstr
        current = ''
    elif current.isalpha() and (string[0].isdigit() or string[0] == '.'):
        result.append(current)
        current = ''

    current += string[0]

    # Recursively split the rest of the string
    return splitStringRec(string[1:], result, current)

l_isNum = lambda item: (item.replace('.', '', 1).isdigit() if item.count('.') == 1 and item[-1] != '.' else item.replace('.', '', 1).isdigit() or (item[:-1].isdigit() and item[-1] == '.'))

# Function to recursively process words in the list
l_processWords = lambda lst: [] if not lst else l_splitNumbersWords(lst[0]) + l_processWords(lst[1:])

# Remove duplicates from a given list
l_removeDuplicates = lambda x: [] if not x else [x[0]] + l_removeDuplicates(l_search(lambda y: y != x[0], x[1:]))

# Merge sort: Θ(n log(n))
l_mergeSort = lambda lst: lst if len(lst) <= 1 else l_merge(l_mergeSort(lst[:len(lst)//2]), l_mergeSort(lst[len(lst)//2:]))

def l_merge(left, right):
    if not right:
        return left
    if not left:
        return right

    tempLeft = int(left[0]) if str(left[0]).isdigit() else float(left[0]) if left[0].replace('.', '', 1).isdigit() else left[0]
    tempRight = int(right[0]) if str(right[0]).isdigit() else float(right[0]) if right[0].replace('.', '', 1).isdigit() else right[0]

    if isinstance(tempLeft, (int, float)) and isinstance(tempRight, (int, float)):
        if tempLeft < tempRight:
            return [left[0]] + l_merge(left[1:], right)
        else:
            return [right[0]] + l_merge(left, right[1:])
    else:
        if str(tempLeft) < str(tempRight):
            return [left[0]] + l_merge(left[1:], right)
        else:
            return [right[0]] + l_merge(left, right[1:])


# Recursive search algorithm for set operations
l_search = lambda f, lst: [] if not lst else [lst[0]] + l_search(f, lst[1:]) if f(lst[0]) else l_search(f, lst[1:])

# Recursive sequential search algorithm
def seqSearchRec(target, arr):
    # Base case: if the array is empty, return False
    if not arr:
        return False

    # If the first element is the target, return True
    if target == arr[0]:
        return True

    # Recursively search the rest of the array
    return seqSearchRec(target, arr[1:])

# Intersection between 2 lists - and
l_intersect = lambda x, y: l_search(lambda element: seqSearchRec(element, y), x)

# Union between 2 lists - or
l_union = lambda x, y: l_removeDuplicates(x + y)

# Difference - in x but not in y
l_difference = lambda x, y: l_search(lambda element: not seqSearchRec(element, y), x)

def parseArguments():
    # Create an ArgumentParser object
    parser = ArgumentParser(description='Process set operations for 2 input text files.')

    # Add an argument for the command string
    parser.add_argument('command', type=str, help='python3 setops.py set1=[filename];set2=[filename];operation=[difference|intersection|union]')

    # Parse the arguments
    args = parser.parse_args()
    # Split the command string by semicolons to get individual arguments
    arguments = splitRec(args.command, ';')
    
    # Initialize variables to store set names and operation
    set1, set2, operation = None, None, None
    
    # Iterate over each argument and parse it
    for arg in arguments:
        key, value = splitRec(arg, '=')
        if key == 'set1':
            set1 = value
        elif key == 'set2':
            set2 = value
        elif key == 'operation':
            operation = value
        else:
            raise Exception('Unknown argument: ' + key)
    
    return set1, set2, operation

# Recursive function to read input files and parse words
def readFile(filename):
    commonSymbols = l_mergeSort(["!", "?", "'", "\"", ",", "/", "\\", "~", "-", "(", ")", "\n", "\t", "\r", ";", ":", "[", "]", "{", "}", "+", "-", "&", "*", "%", "$", "@", "#", "^", "_", "=", "`", "<", ">", "|"])
    try: 
        with open(filename, 'r') as file:
            file_contents = file.read()

            file_contents_copy = file_contents[:]

            text = l_removeDuplicates(l_toLower(l_processWords(splitRec(l_replaceSymbols(file_contents_copy, commonSymbols), ' '))))
            
            # Convert numerical strings to integers or floats
            text = [int(word) if word.isdigit() else format(float(word), f".{len(word.split('.')[1])}f") if word.replace('.', '', 1).isdigit() else word for word in text]
            
            return l_mergeSort(text)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: File not found: {filename}") from e
    except Exception as e:
        raise Exception(f"Error reading file: {e}") from e


# Method to handle set operations
def handleOperations(set1, set2, operation):
    if operation == "union": return l_union(set1, set2)
    elif operation == "difference": return l_difference(set1, set2)
    elif operation == "intersection": return l_intersect(set1, set2)

def main():
    if len(sys.argv) < 2:
        print("Missing arguments")
        print("Usage: python3 setops.py set1=[filename];set2=[filename];operation=[difference|intersection|union]")
        sys.exit(1)
    
    # Parse the command string
    try:
        input1, input2, operation = parseArguments()
    except (ValueError, FileNotFoundError, Exception) as e:
        print("Error parsing command string:", e)
        sys.exit(1)

    # A unknown operation was encountered
    operations = l_mergeSort(["intersection", "union", "difference"])
    if not seqSearchRec(operation, operations):
        print("Error: Invalid operation.")
        sys.exit(1)

    # Read input files
    try:
        set1 = readFile(input1)
        set2 = readFile(input2)
    except (ValueError, FileNotFoundError) as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

    # Perform set operations
    if set1 is None or set2 is None:
        print("Error reading input files.")
        sys.exit(1)

    try:
        result = handleOperations(set1, set2, operation)
    except ValueError as e:
        print("Error performing set operation:", e)
        sys.exit(1)

    # Recursively sort the result: numbers first, then words alphabetically
    sorted_result = l_mergeSort(result) if result else []

    print("Final Result:", sorted_result)

    # Output to result.txt file
    try: 
        with open("result.txt", "w") as file:
            for word in sorted_result:
                file.write(str(word) + "\n")  # Convert word to string before concatenation
    except IOError as e:
        print("Error writing to file", e)
        sys.exit(1)
            
if __name__ == '__main__':
    main()