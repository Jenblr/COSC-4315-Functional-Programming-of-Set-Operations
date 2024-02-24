# Set Operations Program

# Authors: Jennifer Nguyen, Elinnoel Nunez

**INTRODUCTION:**
This Python program is designed to perform set operations such as union, intersection, and difference on two
sets of data read from files. It provides a command-line interface for specifying the sets and the operation
to perform, and it outputs the result to a file name "result.txt".

# Table of Contents
- [Features](#FEATURES)
- [Usage](#USAGE)
- [Lamda Functions Overview](#LAMDA-FUNCTION-OVERVIEW)
- [Search Algorithm](#SEARCH-ALGORITHM)
- [Sort Algorithm](#SORT-ALGORITHM)
- [Issues Encountered](#ISSUE-ENCOUNTERED)
- [Dependencies](#DEPENDENCIES)
- [Files Includes](#FILES-INCLUDED)


**FEATURES:**
1. Set Operations:
    * Union: Combines elements from both sets, excluding duplicates.
    * Intersection: Finds common elements between both sets.
    * Difference: Finds elements that are in the first set but not in the second.
2. Input File Handing:
    * The program reads data f rom input files specified in the command string.
    * It processes the data to remove symbols, excluding periods given a valid floating-point, and converts
    characters into lowercase.
    * Numerical strings are converted to itnegers or floats, where applicabale.
3. Error Handling:
    * The program gracefully handles file not found errors, invalid operations, and other exceptions.
    * Error messages are disdplayed to guide the user on how to recity the issues.
4. Output:
    * The result of the set operation is written to a file name 'result.txt'.
    * If the result is empty for intersection or union, appropriate messages are written to the file.

**USAGE:**
* Command Line Interface:
    * The program is executed from the command line using Python 3.
    * Users provide a command line string contianing the names of the input files, the operation to
    perform, and other parameteres.
* Command String Format:
    * The command string should be formatted as followed: 
    python 3 setops.py "set1=<filename>;set2=<filename>;operation=<operation>"
    * Example: python3 setops.py "set1=a1.txt;set2=b1.txt;operation=union"
* Valid Operations:
    * Users can specify one of the following operations: 'union', 'intersection', or 'difference'

**LAMBDA FUNCTIONS OVERVIEW:**
* This program makes extensive use of lambda function for various operations, enhancing the readability
and conciseness of the code.
* Lambda functions are anonymous fucntions that can be defined inline, elmindating the need for separate
function definitions.

Lambda Functions: 
* Lowercase Conversion:
    * Lambda function 'l_toLower' converts the character to lowercase recursively.
    * It is used for processing words and ensuring uniformity in the input data
* Symbol Stripping:
    * Lambda function 'l_replaceSymbols' removes symbols from text while preserving periods.
    * It uses a recursive approach to replace syumbols with spaces or remove them entirely.
* Period Removal and Splitting:
    * Lambda function 'l_removePeriods' splits text where necessary while retaining periods in valid
    numerical values
    * It ensures proper segmentation of words and numerical values.
* Set Operations and Search:
    * Lambda function 'l_search' is employed for recursive search operations within lists.
    * It enables efficient searchign for elements based on custom criteria.
* Merge Sort: 
    * Lambda functions 'l_mergeSort' and 'l_merge' implement the merge sort algorithm recursively.
    * They  facilitate sorting of elemnts, ensuring efficient set operations.

**SEARCH ALGORITHM:**
* The program employs a binary search algorithm for efficient searching within lists. 
* Time Complexity: O(log(n))

**SORT ALGORITHM:**
* This program implements a merge sort algorithm to sort elements from input files.
* Time Complexity: O(nlog(n))
* The merge sort algorithm is utilized within the program for:
    1. Sorting elements before performing set operations.
    2. Ensuring the proper order of elements in the final result.
    3. Handling numerical and alphabetical sorting requirements.

**ISSUES ENCOUNTERED:**
1. Floating-Point Error:
    * This program does not properly identify and separate floating-points, should they contain more than 1
    decimal points.
    * Example: '12.54.32' should separate as '12.54' and '32'. Instead, this program separates it as '12'
    and '54.32'.

**DEPENDENCIES:**
* This program requires Python 3 to be installed on the system.
* No external libraries beyond the standard Python libary are required.

**FILES INCLUDED:**
1. 'setops.py' : The main Python script containing the set operations program.

