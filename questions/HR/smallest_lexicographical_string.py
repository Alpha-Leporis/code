'''
Write a function that removes all question mark characters from a list in minimal time. 

                                   OR

2. String Replacement

Two strings are given. word and substr. Some of the
characters in word are a question mark (?). Find the
lexicographically smallest string that can be
obtained by replacing "?" characters such
that substr appears at least once. If it is not possible
to do so, return "-1".

Note:
• A substring is a contiguous sequence of characters
Within a string. For example, "bcd" is a of "abcde" but "ac" is not.
• For two strings a and b of the same length. a is
lexicographically smaller than b If ai < bj, for
some 0 <= i <= |a|, and  ai = bj for all 0 <= j < i.

Example:
word = "as?b?e?gf"
substr = "dbk"

Replace the 3rd and 5th characters with 'd' and 'k' to
get "asdbke?gf" which has substr = "dbk" as a
substring, Replace the remaining '?' with 'a'. The
final string is "asdbkeagf".

The answer is "asdbkeagf", without quotes.
'''

'''
Time complexity: O((len_word - len_substr + 1) * len_substr + len_word)
Space complexity: O(len_word + len_substr)
'''

# class Solution:
def smallest_lexicographical_string(word: str, substr: str) -> str:
    len_word = len(word)
    len_substr = len(substr)

    for i in range(len_word - len_substr + 1):
        match_found = True
        temp_word = list(word)
        
        for j in range(len_substr):
            if word[i + j] != '?' and word[i + j] != substr[j]:
                match_found = False
                break
            temp_word[i+j] = substr[j]
            
        if match_found:
            for k in range(len_word):
                if temp_word[k] == '?':
                    temp_word[k] = 'a'
            return ''.join(temp_word)
	    
    return "-1"

# Example usage:
word = "as?b?e?gf"
substr = "dbk"
print(smallest_lexicographical_string(word, substr))  # Output: "asdbkeagf"


# optimized Solution:
'''
Time complexity: O(len_word * len_substr)
Space complexity: O(len_word + len_substr)
'''

def smallest_lexicographical_string(word: str, substr: str) -> str:
    len_word = len(word)
    len_substr = len(substr)

    for i in range(len_word - len_substr + 1):
        match_found = True
        
        for j in range(len_substr):
            if word[i + j] != '?' and word[i + j] != substr[j]:
                match_found = False
                break
        
        if match_found:
            temp_word = list(word)
            temp_word[i:i+len_substr] = substr
            temp_word = ['a' if char == '?' else char for char in temp_word]
            return ''.join(temp_word)
	    
    return "-1"

# Example usage:
word = "as?b?e?gf"
substr = "dbk"
print(smallest_lexicographical_string(word, substr))  # Output: "asdbkeagf"

