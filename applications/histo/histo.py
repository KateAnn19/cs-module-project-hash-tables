import re

# Your code here
file1 = open("robin.txt","r+") 
text = file1.read()



def hash_count_of_word(txt):
    refact_str = re.sub("[^\w']", " ", txt.lower()).split()
    if len(txt) == len(refact_str):
        return ''
    d = {}

    for word in refact_str: 
        if word not in d: 
            d[word] = '#'
        else:
            d[word] += '#'
    return d

dict_text = hash_count_of_word(text)


sorted_dict_text_2 = {k: v for k, v in sorted(dict_text.items(), key=lambda item: item[1], reverse=True)}
sorted_dict_text_3 = sorted(dict_text, key=lambda k: (dict_text[k], k))
sorted_dict_text_4 = {k:v for k, v in sorted(dict_text.items(), key=lambda x: (x[1],x[0]), reverse=True)}

#print(sorted_dict_text_2)
#print(sorted_dict_text_3)
print(sorted_dict_text_4)