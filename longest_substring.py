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

# print(longest_substring('clementisacap')) # "mentisac"
# print(longest_substring("aaaaaaaaaaaa")) # "a"
# print(longest_substring('')) # ''

''' 
We can solve this problem more efficiently by traversing the string and storing the last position at which we see each character in a hash table
 which we'll call lastSeen. We'll also keep track of the longest string we've seen so far. As we traverse the string we'll keep track of a 
 variable called startIdx which will represent the most recent index from which we can start a substring with no duplicate characters, 
 ending at the current index. If we come across a character that we've already seen then we'll update our startIdx to be the maximum of the 
 current startIdx and the position of the element the last time we saw it + 1. Updating the startIdx in this way will make sure that we don't 
 end up moving the startIdx backward when we encounter a duplicate character late in the string. If the current string from the startIdx to the
current position + 1 is greater than the length of the longest string we've seen so far, we'll update longest to the current string.
'''


def longest_substring_optimized(string):
    last_seen = {}
    longest_so_far = ''
    startIdx = 0
    for current_index in range(0, len(string)):
        current_char = string[current_index]
        if current_char in last_seen:
            startIdx = max(startIdx, last_seen[current_char] + 1)
        last_seen[current_char] = current_index
        current_substring = string[startIdx:current_index + 1]
        if len(current_substring) > len(longest_so_far):
            longest_so_far = current_substring
    
    return longest_so_far



print(longest_substring_optimized('clementisacap')) # "mentisac"
print(longest_substring_optimized("aaaaaaaaaaaa")) # "a"
print(longest_substring_optimized('')) # ''

## The time complexity on the above solution is O(n) & the space is O(min(n, a)) where n is the length of the string and a is the number of unique characters in the string.