d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

# actual instance of a class
# d is actually an array filled with nodes 
# hashtables are great because they're fast at lookup O(1), inserting and deleting 
# read, write, delete
# stores things that are unique
# can access and store by string (human way of accessing data) instead of just an index 
# accessing data a lot and need to access it fast 
# checklist for coding problems...
    # is sorting this data going to be useful?
    # is putting this data into a hashtable going to help me?

print(d.get("foo"))
print(d["foo"])

# objects == dictionary == hashtable
# hashmap == hashtable
# hashtable == dictionary (dictionary is Python)