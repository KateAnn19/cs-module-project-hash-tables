class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f"{self.key} {self.value}".format(self.key, self.value)


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.size = 0
        
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.hash_table)
        
    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        # load factor is defined as the number of items in the table divided by capacity
        # total = 0
        # for x in range(len(self.hash_table)):
        #     if (self.hash_table[x] != None): 
        #         total += 1
        # load = total/self.capacity
        # return load
        return self.size / self.capacity
            
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here
        # cryptography 
        FNV_Prime = 1099511628211
        FNV_offset_basis = 14695981039346656037
        hash = FNV_offset_basis
        for char in key:
            hash = hash * FNV_Prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        # look onto bitwise operators
        hash = 5381
        for x in key:
            #hash = ((hash * 33) + hash) + ord(x)
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        # call the load factor to see what the load factor is and resize if necessary
        load = self.get_load_factor()
        # doubles the storage capacity if necessary
        if(load > 0.7):
            self.capacity = self.capacity * 2
            self.resize(self.capacity)
        # find the index in the hash table that we want
        index = self.hash_index(key)
        # if this does not have a new entry create one
        if self.hash_table[index] is None:
            self.hash_table[index] = HashTableEntry(key, value)
            self.size += 1
            if(load < 0.2):
                self.capacity/2
                self.downsize(self.capacity)
            return
        # if the key exists then ovverride it 
        elif self.hash_table[index].key == key:
            self.hash_table[index].value = value
            if(load < 0.2):
                self.capacity/2
                self.downsize(self.capacity)
                return 
        # if the first entry is not the key and and entry exists this means it is a linked list and we need to iterate
        else:
            # it is a linked list and we need to iterate
            current = self.hash_table[index]
            while current.next is not None:
                # looked through everything and didn't find the key so add a new hash entry 
                if current.key == key:
                    self.hash_table[index].value = current.value
                    if(load < 0.2):
                        self.capacity/2
                        self.downsize(self.capacity)
                        return
                current = current.next
            # we didn't find it so we need to create a brand new entry 
            current.next = HashTableEntry(key, value)
            self.size += 1
            if(load < 0.2):
                self.capacity/2
                self.downsize(self.capacity)
            return


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        load = self.get_load_factor()
        # Your code here
        # get the index value
        index = self.hash_index(key)
        # if there is nothing in the index return not found
        if(self.hash_table[index] is None):
            return print('Key is not found')
        # if there is a value and the key is equal set the node to None
        if(self.hash_table[index].key == key):
            self.hash_table[index] = None
            self.size -= 1
            if(load < 0.2):
                self.capacity/2
                self.downsize(self.capacity)
            return 
        # else this means the first value is not the key and there are multiple nodes so iterate
        else:
            # set current to the value 
            current = self.hash_table[index]
            # while the current value has more nodes attached iterate and check to see if keys are equal
            while current.next is not None or current.key is not key:
                # when the key is found then set the node to None
                if current.key == key:
                    value = current.value
                    self.hash_table[index] = None
                    self.size -= 1
                    # return the deleted value 
                    if(load < 0.2):
                        self.capacity/2
                        self.downsize(self.capacity)
                    return value
                # if the key wasn't found then set current to the next node and check that
                current = current.next
            # else it was never found 
            return "Not found"

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # get the index that we want
        index = self.hash_index(key)
        # if there is no value there return None
        if(self.hash_table[index] is None):
            return None
        if self.hash_table[index].key == key:
            return self.hash_table[index].value
        else:
            # iterate through it
            current = self.hash_table[index]
            while current.next is not None:
                if current.key == key:
                    return current.value
                current = current.next
            return None 

        # another way to do this
        # if key isn't found
        # if self.get(key) is None:
        #     return None
        # else find the key and remove it and the valye by setting it to None
        # self.put(key, None)
    
    def downsize(self, new_capacity):
        new_hash = [None] * new_capacity
        old_hash = self.hash_table
        # Your code here
        #loop through the old storage array
        for x in range(len(old_hash)):
            # check to see if there is an entry in the index 
            # placed in variable for ease of understanding
            current = self.hash_table[x]
            # if there is something in the index let's rehash it and place it in a new index 
            if current != None:
                # now let's check to see if it is a linked list or not
                # if it is only one value then rehash it
                if current.next is None:
                    index = self.hash_index(current.key)
                    new_hash_entry = HashTableEntry(current.key, current.value)
                    new_hash[index] = new_hash_entry
                    self.size += 1
                # if it has mutiple values then loop and find the right one
                else: 
                    while current.next is not None:
                        # move forward in the linked list and rehash every  entry 
                        index = self.hash_index(current.key)
                        new_hash_entry = HashTableEntry(current.key, current.value)
                        new_hash[index] = new_hash_entry
                        self.size += 1
                        current = current.next
        self.hash_table = new_hash



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        print(f"It has resized to: {new_capacity}")
        new_hash = [None] * new_capacity
        old_hash = self.hash_table
        # Your code here
        #loop through the old storage array
        for x in range(len(old_hash)):
            # check to see if there is an entry in the index 
            # placed in variable for ease of understanding
            current = self.hash_table[x]
            # if there is something in the index let's rehash it and place it in a new index 
            if current != None:
                # now let's check to see if it is a linked list or not
                # if it is only one value then rehash it
                if current.next is None:
                    index = self.hash_index(current.key)
                    new_hash_entry = HashTableEntry(current.key, current.value)
                    new_hash[index] = new_hash_entry
                    self.size += 1
                # if it has mutiple values then loop and find the right one
                else: 
                    while current.next is not None:
                        # move forward in the linked list and rehash every  entry 
                        index = self.hash_index(current.key)
                        new_hash_entry = HashTableEntry(current.key, current.value)
                        new_hash[index] = new_hash_entry
                        self.size += 1
                        current = current.next
        self.hash_table = new_hash
        
    def __str__(self):
        for x in self.hash_table: 
            if(x is None):
                print("value is none") 
            else:
                if x.next is not None:
                    while x.next is not None:
                        print(f"Key: {x.key}, Value: {x.value}")
                        x = x.next
                else:
                    print(f"KEY {x.key}, {x.value}")

    # Artem gave this function as an example. I may want to refactor to use these built-in methods 
    # def insert_or_overwrite_value(self, value):
    #     node = self.find(value)
    #     if node is None:
    #         # Make a new node
    #         self.insert_at_neadh(Node(value))
    #     else:
    #         # overwrite old value
    #         node.value = value
        


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("This is ht", ht.__str__())

    print("")


    # # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


    print("This is line 1", ht.get("line_1"))
    print("This is line 2", ht.get("line_2"))
    print("This is line 3", ht.get("line_3"))
    print("This is line 4", ht.get("line_4"))
    print("This is line 5", ht.get("line_5"))
    print("This is line 6", ht.get("line_6"))
    print("This is line 7", ht.get("line_7"))
    print("This is line 8", ht.get("line_8"))
    print("This is line 9", ht.get("line_9"))
    print("This is line 10", ht.get("line_10"))
    print("This is line 11", ht.get("line_11"))
    print("This is line 12", ht.get("line_12"))



    # a hashtable is a dictionary under the hood:
    # the hashtable is made up of these parts:
        # hash function + index + array + linked list (basically a node class)

    


    
