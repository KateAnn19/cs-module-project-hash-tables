# Substitution Ciphers
# Or how to transform data from one thing to another 
# a hashmap allows us to transform data to another format (hashmaps allow us to do this)

encode_table = {
    'A' : 'H',
    'B' : 'Z',
    'C' : 'Y',
    'D' : 'W',
    'E' : 'O',
    'F' : 'R',
    'G' : 'J',
    'H' : 'D',
    'I' : 'P',
    'J' : 'T',
    'K' : 'I',
    'L' : 'G',
    'M' : 'L',
    'N' : 'C',
    'O' : 'E',
    'P' : 'X',
    'Q' : 'K',
    'R' : 'U',
    'S' : 'N',
    'T' : 'F',
    'U' : 'A',
    'V' : 'M',
    'W' : 'B',
    'X' : 'Q',
    'Y' : 'V',
    'Z' : 'S'
}

decode_table = {}

for key, value in encode_table.items():
    decode_table[value] = key
#print(decode_table)

def encode(plain_text):
    cipher = ""
    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else:
            cipher += encode_table[char.upper()]
    return cipher

def decode(cipher_text):
    decode = ""
    for char in cipher_text:
        if char.isspace():
            decode += ' '
        else: 
            decode += decode_table[char.upper()]
    return decode

#print(encode("Dictionaries are awesome"))
#print(decode(encode("Dictionaries are awesome")))

#############################################################################################
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# ```
# 'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
# 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
# ```

freqs_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


file1 = open("ciphertext.txt","r+") 
text = file1.read()

#finds the frequency of each letter ignoring non-alpha characters and space
def find_freqs(txt):
    freq_counts = {}
    ntxt = txt.encode("ascii", "ignore")
    nntxt = ntxt.decode()
    for char in nntxt:
        if char.isspace() or not char.isalpha():
            continue
        if char not in freq_counts:
            freq_counts[char] = 1
            # if it were a set it would be d.add(char) and no setting to 1 
        else:
            freq_counts[char] += 1
    return freq_counts

# now build a key based on the frequencies ... highest == 'E'
#first finds the frequency
dict_text = find_freqs(text)

#this sorts in descending order
sorted_dict_text = sorted(dict_text.items(), key=lambda x: x[1], reverse=True)
#clearprint(sorted_dict_text)

#this makes a representation of a dictionary in descending sorted order
sorted_dict_text_2 = {k: v for k, v in sorted(dict_text.items(), key=lambda item: item[1], reverse=True)}
#print(sorted_dict_text_2)

def create_key(sorted_dict, letters):
    key = {}
    i = 0
    for k in sorted_dict:
        key[k] = letters[i]
        i += 1
    return key

key = create_key(sorted_dict_text_2, freqs_letters)


def decode_text(cipher_txt, key):
    decode = ""
    ntxt = cipher_txt.encode("ascii", "ignore")
    nntxt = ntxt.decode()
    for char in nntxt:
        if key.get(char) is not None:
            decode += key[char]
        else:
            decode += char
    return decode

print(decode_text(text, key))












