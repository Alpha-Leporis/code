'''
Implement a simple prototype service to find the difference between two JSON (JavaScript Object Notation) objects.

To keep the prototype simple, a JSON will contain only key-value pairs and no nested objects or arrays in it. 
Given two JSON strings, json1 and json2, find the list of keys for which the values are different. 
If a key is present in only one of the JSONs, it should not be considered in the result. 
The list of keys should be sorted in lexicographically ascending order.

Example:
Suppose json1 = "{"hello":"world", "hi":"hello", "you":"me"}" and json2 = "{"hello":"world", "hi":"helloo", "you":"me"}"

The only common key where the values differ is "hi". Hence the answer is ["hi"].

Function Description
Complete the function getJSONDiff in the editor below.

getJSONDiffhas the following parameter(s):
	json 1: the first JSON string
	json2: the second JSON string

Returns
string[]: a sorted list of keys that have different associated values in the two JSONs.

Constraints
• 1 <= |json1|, |json1| <= 10^5
• There are no white spaces in the string
'''

# solution:
'''
To solve this problem in Python, we can parse the JSON strings into dictionaries using the json module, 
then iterate through the keys of both dictionaries to compare their values. 
We'll store the keys with different values in a list and return it after sorting it lexicographically.

In this implementation:
    1. We first parse the JSON strings json1 and json2 into dictionaries using json.loads().
    2. We then initialize an empty list different_keys to store the keys with different values.
    3. We iterate through the keys of both dictionaries using a set intersection operation (&), which gives us the common keys.
    4. For each common key, if the corresponding values in the dictionaries are different, we append the key to the different_keys list.
    5. Finally, we sort the list of different keys lexicographically and return it.

time complexity is O(n + m), where n is the length of the JSON strings and m is the number of keys in the larger dictionary.
space complexity is O(n), where n is the length of the JSON strings
'''

import json

def getJSONDiff(json1, json2):
    # Parse JSON strings into dictionaries
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)

    # Initialize a list to store keys with different values
    different_keys = []

    # Iterate through keys of both dictionaries
    for key in set(dict1.keys()) & set(dict2.keys()):
        if dict1[key] != dict2[key]:
            different_keys.append(key)

    # Sort the list of different keys lexicographically
    different_keys.sort()

    return different_keys

# Example usage:
json1 = '{"hello":"world", "hi":"hello", "you":"me"}'
json2 = '{"hello":"world", "hi":"helloo", "you":"me"}'
result = getJSONDiff(json1, json2)
print("Keys with different values:", result)

# optimized solution:

'''
We can optimize the solution by avoiding the creation of dictionaries and instead directly
comparing the JSON strings character by character. We'll split  
the JSON strings into key-value pairs, sort them, and then compare corresponding key-value pairs. 
This way, we eliminate the need for parsing JSON strings into dictionaries, reducing the overhead.

In this optimized implementation:
    1. We split the JSON strings into key-value pairs using split(',') and remove the outer curly braces using strip('{}').
    2. We sort the key-value pairs to ensure that they are in lexicographically ascending order.
    3. We then iterate through the corresponding key-value pairs of both JSON strings using zip() and compare their values directly without parsing into dictionaries.
    4. If the values are different, we append the corresponding key to the different_keys list.
    5. Finally, we return the list of keys with different values.
time complexity: O(n log n)
Space complexity is O(n) for storing the key-value pairs and O(min(n, m)) for the list different_keys.
'''

def getJSONDiff(json1, json2):
    # Split JSON strings into key-value pairs and sort them
    pairs1 = sorted(json1.strip('{}').split(','))
    pairs2 = sorted(json2.strip('{}').split(','))

    # Initialize a list to store keys with different values
    different_keys = []

    # Iterate through corresponding key-value pairs
    for pair1, pair2 in zip(pairs1, pairs2):
        key1, value1 = pair1.split(':')
        key2, value2 = pair2.split(':')

        # Compare values and store keys with different values
        if value1 != value2:
            different_keys.append(key1)

    return different_keys

# Example usage:
json1 = '{"hello":"world", "hi":"hello", "you":"me"}'
json2 = '{"hello":"world", "hi":"helloo", "you":"me"}'
result = getJSONDiff(json1, json2)
print("Keys with different values:", result)

