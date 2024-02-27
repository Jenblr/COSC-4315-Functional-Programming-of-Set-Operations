const yargs = require('yargs');
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
    if (seqSearchRec(text[0], symbols)) return ' '.concat(l_replaceSymbols(text.slice(1), symbols));
    return text[0].concat(l_replaceSymbols(text.slice(1), symbols));
};

const l_isAlpha = (str) => {
    return str.match(/^[a-zA-Z]+$/) !== null;
}

// Checks if a string contains a mixture of characters and digits
const l_checkString = (text) => {
    return l_isAlpha(text) || splitRec(text,'').every((c) => c.match(/\d/));
}

// Split numbers and words from a string
const l_splitNumbersWordsRec = (text) => {
    if (l_checkString(text)) return [text];
    return splitStringRec(text, [], '');
}

// Define a recursive function to split the string into words and digits: Example: test2right35below
const splitStringRec = function(string, result=[], current='') {
    if (!string) {
        if (l_isNum(current)) {
            result.push(current);
        } else if (l_isAlpha(current)) {
            result.push(current);
        } else {
            if (current[0] === '.' && current.slice(-1) === '.') {
                const temp = current.slice(1, -1);
                if (temp) {
                    result.push(current.slice(1, -1));
                }
            } else if (current[0] === '.') {
                result.push(current.slice(1));
            } else {
                if (current.length !== 0) {
                    result.push(current.slice(0, -1));
                }
            }
        }
        return result;
    }

    if (l_isNum(current) && !l_isNum(current + string[0])) {
        result.push(current);
        const newstr = string.length > 1 && string[0] === '.' ? string.slice(1) : string;
        string = newstr;
        current = '';
    } else if (l_isAlpha(current) && (string[0].match(/\d/) || string[0] === '.')) {
        result.push(current);
        current = '';
    }

    current += string[0];
    return splitStringRec(string.slice(1), result, current);
}

const l_isNum = (item) => {
    if (splitRec(item, '.').length === 2 && !item.endsWith('.')) return item.replace('.', '').match(/^\d+$/);
    return item.replace('.', '').match(/^\d+$/) || (item.slice(0, -1).match(/^\d+$/) && item.endsWith('.'));
};

// Function to recursively process words in the list
const l_processWords = (lst) => {
    if (!lst.length) return [];
    return l_splitNumbersWordsRec(lst[0]).concat(l_processWords(lst.slice(1)));
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

// Convert numerical strings to integers or floats else return the string
const castString = (word) => {
    if (/^\d+$/.test(word)) {
        return parseInt(word);
    } else if (/^\d+(\.\d+)?$/.test(word)) {
        return parseFloat(word);
    } else {
        return word;
    }
};

const l_merge = (left, right) => {
    if (!right.length) return left;
    if (!left.length) return right;

    // Convert numerical strings to integers or floats or the given string
    const tempLeft = castString(left[0].toString());
    const tempRight = castString(right[0].toString());

    if (typeof tempLeft === 'number' && typeof tempRight === 'number') {
        if (tempLeft < tempRight) {
            return [left[0], ...l_merge(left.slice(1), right)];
        } else if (tempLeft > tempRight) {
            return [right[0], ...l_merge(left, right.slice(1))];
        } else {
            return [left[0], right[0], ...l_merge(left.slice(1), right.slice(1))];
        }
    } else if (typeof tempLeft === 'number' && typeof tempRight === 'string') {
        return [left[0], ...l_merge(left.slice(1), right)];
    } else if (typeof tempLeft === 'string' && typeof tempRight === 'number') {
        return [right[0], ...l_merge(left, right.slice(1))];
    } else {
        if (tempLeft < tempRight) {
            return [left[0], ...l_merge(left.slice(1), right)];
        } else if (tempLeft > tempRight) {
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

// Recursive sequential search algorithm
const seqSearchRec = (target, arr) => {
    if (!arr.length) return false;
    if (target === arr[0]) return true;
    return seqSearchRec(target, arr.slice(1));
};

// Intersection between 2 lists - and
const l_intersect = (x, y) => {
    return l_search((element) => seqSearchRec(element, y), x);
};

// Union between 2 lists - or
const l_union = (x, y) => {
    return l_removeDuplicates([...x, ...y]);
};

// Difference - in x but not in y
const l_difference = (x, y) => {
    return l_search((element) => !seqSearchRec(element, y), x);
};

function parseArguments() {
    const argv = yargs
        .usage('Usage: node $0 "set1=[filename];set2=[filename];operation=[difference|intersection|union]"')
        .help() // Enable built-in help option
        .alias('h', 'help') // Alias for help option
        .argv;

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
                const decimalPlaces = splitRec(word, '').reverse().join('').indexOf('.')
                return parseFloat(word).toFixed(decimalPlaces);
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
        console.log("Final Result:", sortedResult);
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
