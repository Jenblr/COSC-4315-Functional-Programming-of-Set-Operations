const fs = require('fs');

// Utils
const splitRec = (x, y) => {
    if (x.indexOf(y) === -1 || x.length <= 1) {
        return [x];
    } else if (x.indexOf(y) === x.length - 1) {
        return [x.slice(0, x.indexOf(y))];
    } else if (y === '') {
        if (x.length === 1) {
            return [x];
        }
        return [x[x.indexOf(y)]].concat(splitRec(x.slice(x.indexOf(y) + 1), y));
    } else if (x.indexOf(y) === 0) {
        return [].concat(splitRec(x.slice(x.indexOf(y) + 1), y));
    } else {
        return [x.slice(0, x.indexOf(y))].concat(splitRec(x.slice(x.indexOf(y) + 1), y));
    }
};

// Lambda lowercase that uses recursive function to generate lowercase characters
const l_toLower = (x) => x.map((word) => l_toLowerHelper(word));
const l_toLowerHelper = (word) => {
    if (!word) return '';
    if (!/[A-Z]/.test(word[0])) return word[0] + l_toLowerHelper(word.slice(1));
    return String.fromCharCode(word.charCodeAt(0) + 32) + l_toLowerHelper(word.slice(1));
};

// Strips white space and removes symbols except for periods
const l_replaceSymbols = (text, symbols) => {
    if (!text) return '';
    if (binarySearchRec(text[0], symbols, 0, null)) return ' '.concat(l_replaceSymbols(text.slice(1), symbols));
    return text[0].concat(l_replaceSymbols(text.slice(1), symbols));
};

// Recursive lambda function to remove periods and split where necessary
const l_removePeriods = (item) => {
    if (!binarySearchRec('.', l_mergeSort([...item]), 0, null) || l_isNum(item)) return [item];
    return splitRec(item, '.');
};
const l_isNum = (item) => {
    if (splitRec(item, '.').length === 2 && !item.endsWith('.')) return item.replace('.', '').match(/^\d+$/);
    return item.replace('.', '').match(/^\d+$/) || (item.slice(0, -1).match(/^\d+$/) && item.endsWith('.'));
};

// Function to recursively process words in the list
const l_processWords = (lst) => {
    if (!lst.length) return [];
    return l_removePeriods(lst[0]).concat(l_processWords(lst.slice(1)));
};

// Remove duplicates from a given list
const l_removeDuplicates = (x) => {
    if (!x.length) return [];
    return [x[0], ...l_removeDuplicates(l_search((y) => y !== x[0], x.slice(1)))];
};

// Merge sort: Θ(n log(n))
const l_mergeSort = (lst) => {
    if (lst.length <= 1) return lst;

    const mid = Math.floor(lst.length / 2);
    const left = l_mergeSort(lst.slice(0, mid));
    const right = l_mergeSort(lst.slice(mid));
    
    return l_merge(left, right);
};

const l_merge = (left, right) => {
    if (!right.length) return left;
    if (!left.length) return right;

    if (typeof left[0] === 'number' && typeof right[0] === 'number') {
        if (left[0] < right[0]) {
            return [left[0], ...l_merge(left.slice(1), right)];
        } else if (left[0] > right[0]) {
            return [right[0], ...l_merge(left, right.slice(1))];
        } else {
            return [left[0], right[0], ...l_merge(left.slice(1), right.slice(1))];
        }
    } else if (typeof left[0] === 'number' && typeof right[0] === 'string') {
        return [left[0], ...l_merge(left.slice(1), right)];
    } else if (typeof left[0] === 'string' && typeof right[0] === 'number') {
        return [right[0], ...l_merge(left, right.slice(1))];
    } else {
        if (left[0] < right[0]) {
            return [left[0], ...l_merge(left.slice(1), right)];
        } else if (left[0] > right[0]) {
            return [right[0], ...l_merge(left, right.slice(1))];
        } else {
            return [left[0], right[0], ...l_merge(left.slice(1), right.slice(1))];
        }
    }
};

// Recursive search algorithm for set operations
const l_search = (f, lst) => {
    if (!lst.length) return [];
    if (f(lst[0])) {
        return [lst[0], ...l_search(f, lst.slice(1))];
    } else {
        return l_search(f, lst.slice(1));
    }
};

// Recursive algorithm to check if a given value is in a list
const binarySearchRec = (elem, arr, start = 0, end = arr.length - 1) => {
    if (end == null) end = arr.length - 1;
    if (start > end) return false;

    const mid = Math.floor((start + end) / 2);

    if (String(elem) == String(arr[mid])) {
        return true;
    } else if (String(elem) < String(arr[mid])) {
        return binarySearchRec(elem, arr, start, mid - 1);
    } else {
        return binarySearchRec(elem, arr, mid + 1, end);
    }
};

// Intersection between 2 lists - and
const l_intersect = (x, y) => {
    return l_search((element) => binarySearchRec(String(element), y, 0, null), x.map((item) => String(item)));
};

// Union between 2 lists - or
const l_union = (x, y) => {
    return l_removeDuplicates([...x, ...y]);
};

// Difference - in x but not in y
const l_difference = (x, y) => {
    return l_search((element) => !binarySearchRec(String(element), y.map(String), 0, null), x.map((item) => String(item)));
};

function parseArguments() {
    // Create an ArgumentParser object
    const args = process.argv.slice(2);
    const command = args.join(" ");

    // Split the command string by semicolons to get individual arguments
    const arguments = splitRec(command,';');
    
    // Initialize variables to store set names and operation
    let set1, set2, operation;
    
    // Iterate over each argument and parse it
    for (let arg of arguments) {
        const [key, value] = splitRec(arg, '=');
        if (key === 'set1') {
            set1 = value;
        } else if (key === 'set2') {
            set2 = value;
        } else if (key === 'operation') {
            operation = value;
        } else {
            throw new Error(`Unknown argument: ${key}`);
        }
    }
    
    return [set1, set2, operation];
}

// Recursive function to read input files and parse words
function readFile(filename) {
    const commonSymbols = l_mergeSort(["!", "?", "'", "\"", ",", "/", "\\", "~", "-", "(", ")", "\n", "\t", "\r", ";", ":", "[", "]", "{", "}", "+", "-", "&", "*", "%", "$", "@", "#", "^", "_", "=", "`", "<", ">", "|"]);
    try { 
        const fileContents = fs.readFileSync(filename, 'utf8');
        const fileContentsCopy = fileContents.slice();

        let text = l_removeDuplicates(l_toLower(l_processWords(splitRec(l_replaceSymbols(fileContentsCopy, commonSymbols), ' '))));

        // Convert numerical strings to integers or floats
        text = text.map((word) => {
            if (/^\d+$/.test(word)) {
                return parseInt(word);
            } else if (/^\d+(\.\d+)?$/.test(word)) {
                return parseFloat(word);
            } else {
                return word;
            }
        });

        return l_mergeSort(text);
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error(`File not found: ${filename}`);
        }
        throw error;
    }
}

// Method to handle set operations
function handleOperations(set1, set2, operation) {
    if (operation === "union") return l_union(set1, set2);
    else if (operation === "difference") return l_difference(set1, set2);
    else if (operation === "intersection") return l_intersect(set1, set2);
}

function main() {
    if (process.argv.length < 3) {
        console.error("Missing arguments");
        console.error("Usage: node setops.js set1=[filename];set2=[filename];operation=[difference|intersection|union]");
        process.exit(1);
    }
    
    // Parse the command string
    let input1, input2, operation;
    try {
        [input1, input2, operation] = parseArguments();
    } catch (error) {
        console.error("Error parsing command string:", error.message);
        process.exit(1);
    }

    // A unknown operation was encountered
    const operations = ["intersection", "union", "difference"];
    if (!operations.includes(operation)) {
        console.error("Error: Invalid operation.");
        process.exit(1);
    }

    let set1 = null;
    let set2 = null;

    try {
        // Read input files
        set1 = readFile(input1);
        set2 = readFile(input2);
    } catch (error) {
        console.error(error.message);
        process.exit(1);
    }

    // Perform set operations
    if (set1 === null || set2 === null) {
        console.error("Error reading input files.");
        process.exit(1);
    }

    try {
        const result = handleOperations(set1, set2, operation);

        // Recursively sort the result: numbers first, then words alphabetically
        const sortedResult = l_mergeSort(result) || [];
        console.log("Sorted result:", sortedResult);
        // Output to result.txt file
        try { 
            fs.writeFileSync("result.txt", sortedResult.join("\n"));
        } catch (error) {
            console.error("Error writing to file", error);
            process.exit(1);
        }
    } catch (error) {
        console.error("Error performing set operation:", error);
        process.exit(1);
    }
}

main();
