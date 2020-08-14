class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
        self.contents = [None] * capacity
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
        return len(self.contents)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # // = whole number  / = decimals
        return self.size / self.capacity
        

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
                                                                                                                                    
        hash = 5381
        # byte_array = key.encode('utf-8')


        for byte in key:
            # the modulus keeps it 32-bit, python ints don't overflow
            hash = (hash * 33) + ord(byte)

        return hash


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
        index = self.hash_index(key)
        # check if the index is not in the table create a new one
        if not self.contents[index]:
            self.contents[index] = HashTableEntry(key,value)
            # speeding up the process instead of checking length.
            self.size =+ 1
        else:
            current = self.contents[index]
            while current.next is not None and current.key is not key:
                current = current.next
            if current.key is key:
                current.value = value
            else:
                current.next = HashTableEntry(key,value)
                # speeding up the process instead of checking length.
                self.size =+ 1








        """For a given key, store a value in the hash table"""
        # find the index of the key
        # entry_index = self.hash_index(key)
        
        # # check to see if there is already an entry at that key
        # if self.contents[entry_index] is None:
        #     # creating the new entry
        #     new_entry = HashTableEntry(key,value)
        #     # assigning the new entry to the contents of that index
        #     self.contents[entry_index] = new_entry
        # current_entry = self.contents[entry_index]
        # # while there is a current entry there.
        # while current_entry:
        #     # if the current entry's key is equal to the key
        #     if current_entry.key == key:
        #         # then we need to overwrite the current entry's value with the new value.
        #         current_entry.value = value
        #     # we are pointing the new head to the new value
        #     current_entry = current_entry.next
        #     # the old head is now current entry
        #     old_head = current_entry 
        #     new_head = HashTableEntry(key, value) 
        #     new_entry = self.contents[entry_index] 
        #     new_head.next = old_head
        # self.size += 1



        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        if self.get(key) is None:
            return None
        self.put(key, None) 
 



        # hash the key and find the index
        # index = self.hash_index(key)
        # # search the linked list for the hashtable entry
        # # set a variable called 'current' to be show contents of the index
        # current = self.contents[index]
        # while current is not None:
        #     if current.key == key:
        #         current.value = None
        #     else:
        #         # looking to the next value in the linked list
        #         current = current.next
        
        



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # find the index for the given key
        entry_index = self.hash_index(key)
        # set a variable called 'current' to be show contents of the index
        current = self.contents[entry_index]
        # while current is not none 
        while current is not None:
            # check if current's key is == to the key we searched
            if current.key == key:
                # if it is then return the value
                return current.value
            # else look to the next value in linked list and compare again.
            else:
                # looking to the next value in the linked list
                current = current.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_contents = self.contents
        self.contents = [None] * new_capacity
        self.capacity = new_capacity
        for i in old_contents:
            current = i
            # if we reach the end of the list
            if current.next is None:
                self.put(current.key, current.value)
            while current.next is not None:
                self.put(current.key, current.value)
                current = current.next
            self.put(current.key, current.value)


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

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
