import re

# given a string, can we figure out how many times each letter appears in it?
def letter_count(s):
    # keep track of count of letters
    # Dictionary where Keys are letters and values will be an incrementing counter 
    # loop through string and calculate whether or not it appears 
    # ignore space character 
    d = {}
    for char in s:
        if char.isspace():
            continue
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d 
        


# print(letter_count("aaabbc"))
# print(letter_count("Hello!"))
# print(letter_count("The quick brown fox jumps over the lazy dog"))



################################################################################################################
# Start of Project - Practice Above 


## Input

# This function takes a single string as an argument.
# ```
# Hello, my cat. And my cat doesn't say "hello" back.
# ```

# ## Output
# It returns a dictionary of words and their counts:
# ```
# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
# ```
# Case should be ignored. Output keys must be lowercase.
# Key order in the dictionary doesn't matter.
# Split the strings into words on any whitespace.
# Ignore each of the following characters:
# ``
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```
# If the input contains no ignored characters, return an empty dictionary.




def word_count(s):
    # Your code here
    refact_str = re.sub("[^\w']", " ", s.lower()).split()
    d = {}

    for word in refact_str: 
        if word not in d: 
            d[word] = 1
        else:
            d[word] += 1
    return d





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))