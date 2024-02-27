# Set Operations Program

# Authors: Jennifer Nguyen, Elinnoel Nunez

**INTRODUCTION:**
This program, available in both Python and JavaScript versions, is designed to perform set operations such 
as union, intersection, and difference on two sets of data read from files. It provides a command-line 
interface for specifying the sets and the operation to perform and outputs the result to a file named
"result.txt".

# Table of Contents
- [Features](#FEATURES)
- [Usage](#USAGE)
- [Lamda Functions Overview](#LAMDA-FUNCTION-OVERVIEW)
- [Search Algorithm](#SEARCH-ALGORITHM)
- [Sort Algorithm](#SORT-ALGORITHM)
- [Error Handling](#ERROR-HANDLING)
- [Issues Encountered](#ISSUE-ENCOUNTERED)
- [Dependencies](#DEPENDENCIES)
- [Files Includes](#FILES-INCLUDED)


## FEATURES:
**1. Set Operations:**
    * Union: Combines elements from both sets, excluding duplicates.
    * Intersection: Finds common elements between both sets.
    * Difference: Finds elements that are in the first set but not in the second.
**2. Input File Handing:**
    * The program reads data f rom input files specified in the command string.
    * It processes the data to remove symbols, excluding periods given a valid floating-point, and converts
    characters into lowercase.
    * Numerical strings are converted to itnegers or floats, where applicabale.
**3. Error Handling:**
    * The program gracefully handles file not found errors, invalid operations, and other exceptions.
    * Error messages are disdplayed to guide the user on how to recity the issues.
**4. Output:**
    * The result of the set operation is written to a file name 'result.txt'.
    * If the result is empty for intersection or union, appropriate messages are written to the file.

## USAGE:
*** Command Line Interface:**
    * The program is executed from the command line using Python 3 or Node.js for Python and JavaScript 
    versions respectively.
    * Users provide a command line string contianing the names of the input files, the operation to
    perform, and other parameteres.
*** Command String Format:**
    * For Python: python 3 setops.py "set1=<filename>;set2=<filename>;operation=<operation>"
    * For JavaScript: node setops.js "set1=<filename>;set2=<filename>;operation=<operation>"
*** Valid Operations:**
    * Users can specify one of the following operations: 'union', 'intersection', or 'difference'

## LAMBDA FUNCTIONS OVERVIEW:
* Both Python and JavaScript versions of this program make extensive use of lambda function for various
operations, enhancing the readability and conciseness of the code.
* Lambda functions are anonymous fucntions that can be defined inline, elmindating the need for separate
function definitions.

### Lambda Functions: 
_Note: Python's lambda function and JavaScript's arrow functions serve similar purposes as anonymous
functions, but each language has differences for their own syntax, handling of arguments, and support 
for expressions versus block bodies._
*** Lowercase Conversion:**
    * Lambda function 'l_toLower' utilizes the 'map()' function to iterate over each word in the input
    list and applies 'l_toLowerHelper' function to each word recursively.
    * Lambda function 'l_toLowerHelper' is a recursive function that performs the actual conversion of
    uppcase characters to lowercase within a word.
*** Symbol Stripping:**
    * Lambda function 'l_replaceSymbols' removes symbols from text while preserving periods.
    * The program uses a recursive approach to replace syumbols with spaces or remove them entirely.
*** Period Removal and Splitting:**
    * Lambda function 'l_removePeriods' splits text where necessary while retaining periods in valid
    numerical values.
    * It ensures proper segmentation of words and numerical values.
***String Checker:**
    * Lambda function 'l_checkString' checks if a string contains a mixture of characters and digits.
    * The Python program uses the 'all()' function to check if all characters in the string are alphabetic or 
    if there contain digits
    * The JavaScript program uses the'every()' function to check if all characters in the string are 
    alphabetic or if there contains digits
***Splitting Words and Number Literals:**
    * Lambda function 'l_splitNumbersWords' separates numbers and words from a string recursively.
    * The program uses '1_search' to identify if a string contains only words, else it uses 'splitStringRec' 
    to split the digits from the characters
***Word Proccesor:**
    * Lambda function 'l_processWords:' recursively processes words in a list.
    * The program utilizes 'l_splitNumberWords' to split each words into numbers and words.
***Remove Duplicates:**
    * Lambda function 'l_removeDuplicates' removes duplicates froms a given list.
    * The program uses a recursive search lambda function 'l_serach' to identify and remove duplicates.
***Merge Sort Algorithm:**
    * Lambda function 'l_mergeSort' sorts a list using the merge sort algorithm recursively.
    * It uses 'l_merge' to merge two sorted lists into a single sorted list
*** Set Operations and Search:**
    * Lambda function 'l_search' is employed for recursive search operations within lists.
    * The program enables efficient searchign for elements based on custom criteria.
*** Merge Sort:** 
    * Lambda functions 'l_mergeSort' and 'l_merge' implement the merge sort algorithm recursively.
    * The program facilitate sorting of elemnts, ensuring efficient set operations.
*** Set Operations:**
    * Lambda function 'l_intersect' computes the intersection between two lists using 'l_search' to identify
    elements present in both lists.
    * Lambda function 'l_union' computes the concatenation of two lists and removes duplicates using
    'l_removeDuplicates'.
    * Lambda function 'l_difference' computes the difference between two lists using 'l_search' to identify
    elements present in the first list but not in the second list.

## SEARCH ALGORITHM:
* Algorithm: Recursive Sequential Search
* Time Complexity: O(n)
    * In the worst-case scenario, the algorithm needs to traverse through all elements of the array 
    or list once to find the target element.
* Space Complexity: O(1)
    * The space required by the algorithm is constant as it does not utilize additional memory 
    proportional to its input size

## SORT ALGORITHM:
* Algorithm: Merge Sort
* Time Complexity: O(nlog(n))
* The merge sort algorithm is utilized within the program for:
    1. Sorting elements before performing set operations.
    2. Ensuring the proper order of elements in the final result.
    3. Handling numerical and alphabetical sorting requirements.
* Space Complexity: O(n)
    * Merge sort requires additional memory proportional to the size of its input list to store
    temporary arrays during the merge process.

## ERROR HANDLING:
Error handling in the Set Operations Program is comprehensive and designed to guide users through potential 
issues encountered during execution. Both the Python and JavaScript versions implement robust error handling 
mechanisms to ensure smooth program operation and provide informative feedback to users.

### Types of Errors Handled:
**1. File-related Errors:**
    * File Not Found: If one or both input files specified in the command string are not found, the program 
    raises a FileNotFoundError. This error message guides the user to check the specified filenames and verify 
    their existence.
    * File Read/Write Errors: Any errors occurring during the reading or writing of files, such as permission 
    issues or file corruption, are captured and presented to the user with descriptive error messages.
**2. Command String Parsing Errors:**
    * Invalid Command Format: The program expects a specific command string format specifying the input filenames 
    (set1 and set2) and the set operation (operation). If the command string does not adhere to this format, the 
    program raises an Exception with a message instructing the user to provide the correct format.
    * Unknown Argument: If an unrecognized argument is provided in the command string, the program raises an 
    Exception with a message indicating the unknown argument and suggesting possible corrections.
**3. Invalid Set Operations:**
    * Invalid Operation: The program validates the specified set operation (operation) to ensure it is one of the 
    supported operations: union, intersection, or difference. If an unsupported operation is provided, the program 
    raises an Exception informing the user about the invalid operation and suggesting valid options.
**4. Data Processing Errors:**
    * Data Format Error: During the processing of input files, if the program encounters unexpected data formats or 
    inconsistencies, it raises appropriate errors with informative messages. For example, if a numerical value 
    cannot be converted to an integer or float, an error is raised, indicating the issue to the user.

## ISSUES ENCOUNTERED:
_Note: Although the program's requirements outlined in the 'string-setops.pdf' did not specifically state that these issues
should be addressed, our authors acknowledged and proceeded with solutions should the program encounter test cases that fail 
to meet result expectations._
    1. Floating-Point Error: 
        * Initially, this program did not properly identify and separate floating-points, should they contain more 
        than 1 decimal points.
        * Example: '12.54.32' should separate as '12.54' and '32'. Instead, the program separated it as '12' and '54.32'.
        * Solution:
            * In the JavaScript version, a modification was made in the splitStringRec function to properly handle floating-point 
            numbers by considering the first occurrence of the decimal point.
            * In the Python version, the castString function was introduced to correctly convert numerical strings to integers or 
            floats, accounting for multiple decimal points.
    2. Non-Separation of Mixed Characters and Digits:
        * Initially, this program did not properly identify and separate strings that contain both numbers and words.
        * Example: 'test2case3.5below' should separate as ['test', '2', 'case', '3.5', 'below']. Instead the program 
        never separated it and kept it as 'test2case3.5below'.
        * Solution: In both the Python and JavaScript versions, adjustments were made in the respective functions (splitStringRec
        and l_splitNumbersWordsRec) to correctly split the input into distinct elements comprising both numbers and words.
    3. Ordering of Result:
        * Initially, this program did not properly ordered the elements in the array based on numbers first in numerical
        value-order and then words in lexicographical order.
        * Example: ['1','11','12','123','13','50','apple','bat','dog','frog'] should be ordered as 
        [1, 11, 12, 13, 50, 123, 'apple', 'bat', 'dog', 'frog'].
        * Solution: Both the Python and JavaScript versions were updated to utilize the l_mergeSort function, which implements 
        the merge sort algorithm to sort the elements in the desired order. Additionally, a custom sorting logic was applied to 
        ensure proper ordering based on the data type (numeric or string). 
    4. Searching Through Array Elements:
        * Initially, this program did not reliably search through the array for elements, especially if the elements contained
        a mix of numeric and string values.
        * Solution: Both the Python and JavaScript versions were updated to utilize sequential search instead of binary search, 
        given that it has better time complexity and aligns better with the characteristics of the data and requirements of the 
        operations.


## DEPENDENCIES:
*** For the Python Script('setops.py'):**
    * Python3 installed on the system
    * The 'argparse' module for parsing command-line arguments
*** For the JavaScript script('setops.js'):**
    * Node.js installed on the system
    * The 'yargs' module for parsing command-line arguments

## FILES INCLUDED:
1. 'setops.py' : The main Python script containing the set operations program.
2. 'setops.js' : The equivalent JavaScript script containing the set operations program.