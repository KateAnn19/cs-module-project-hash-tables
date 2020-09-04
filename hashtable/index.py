records = [
    ("Alice", "Engineering"),
    ("Bob", "Engineering"),
    ("Larry", "Engineering"),
    ("Tina", "Engineering"),
    ("Donny", "Sales"),
    ("Terry", "Sales"),
    ("Toni", "Sales"),
    ("Katie", "Sales"),
    ("Pat", "Engineering"),
    ("Greg", "Marketing"),
    ("Rick", "Engineering"),
    ("John", "Marketing"),
    ("Alice", "Engineering"),
    ("Peter", "Engineering"),
    ("Fred", "Engineering"),
    ("Sarah", "Marketing"),
    
]

# proposed dictionary
# keys will be departments
# valyes will be array of names, or list of names 
# function to build the index for accessing lists or large sets of data (indexing this data)
# a hash table can be used to make work after forever easier 
# what is a downside of all this?
    # we've used more space 
def build_index(recs):
    index = {}
    for record in recs:
        # rec[0] = key
        # rec[1] = value 
        # this is same as above but quicker 
        name, dept = record
        #check if department is already in index
        # we're checking if key exists already
        if dept in index: 
            index[dept].append(name)
        else:
            index[dept] = [name] 
    return index
            
        
        # if it is, add name to the list
        # else create new key with list with the name in it


department_index = build_index(records)
# print all the departments
print(department_index.keys())

# print everyone in Engineering
print(department_index['Engineering'])

# print everyone in Sales:
print(department_index['Sales'])

# print everyone in Marketing 
print(department_index['Marketing'])



