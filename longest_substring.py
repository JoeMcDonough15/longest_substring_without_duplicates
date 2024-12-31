# Longest Substring Without Duplicates

'''
Brute Force Solution 

Synopsis
Keep track of a longest_so_far which starts as an empty string. Iterate through every character of the original string, and from that character's index
build a new current_substring until we either 1) reach the end of the original_string or 2) discover a duplicate character that's in our current_substring.
At that point, set longest_so_far to the current_substring only if current_substring's length is longer than longest_so_far.

Complexity
I think the time complexity would be O(n^2) because we need to loop through the entire string from whatever index we are at.  If there are millions of characters
in the string, we have to repetitively loop through millions of characters, even if the inner loop is not starting at the beginning of the string more than once.

I think the space complexity would be O(n).  Each iteration of the inner loop, we are building a new string that starts empty and ends with potentially many characters.
We are not storing more than one of these, however, since current_substring is reset at each iteration of the outer loop.

example input/output:
original_string = "clementisacap"
solution = "mentisac"

Polya's
1. initialize an empty string to longest_so_far
2. construct a definite loop that acts as the outer loop, over every character of original_string.  iteration variable i
3. within each iteration of that outer loop, initialize a new string called current_substring
    a. reset current_seen_chars to an empty set.
4. construct an inner loop that begins at original_string[i]. iteration variable can be called j; initialize j to be i
   a. break this inner loop if j is ever the length of original_string
   b. break this inner loop if the character at original_string[j] is already in our set current_seen_chars
5. as we move through the inner loop, set the current character to our current_substring
'''

def longest_substring(original_string):
    longest_so_far = ''
    for i in range(0, len(original_string)):
        current_substring = ''
        characters_seen = set()
        j = i
        while j < len(original_string):
            current_char = original_string[j]
            if current_char in characters_seen:
                break
            current_substring += current_char
            characters_seen.add(current_char)
            j += 1
        if len(current_substring) > len(longest_so_far):
            longest_so_far = current_substring    

    return longest_so_far

print(longest_substring('clementisacap')) # "mentisac"
print(longest_substring("aaaaaaaaaaaa")) # "a"
print(longest_substring('')) # ''