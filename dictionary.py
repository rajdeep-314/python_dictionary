initial_size = 8 # Initial size of the hash table of the dictionary
mult_factor = 2 # Factor by which size changes during resizing
loading_factor = 0.6 # Loading percentage must be less than this at all times
probing_step = 5 # In case of collisions, new location = (last tried location + probing_step) % table_size


# For now, this is just Python's in-built hash function
def hash_function(input_string):
    return hash(input_string)


class dictionary:
    # You can force the size by passing it as an argument
    def __init__(self, *args, size = initial_size):
        self._dict = [["-"]*3 for _ in range(size)] # Initializes an "empty" hash table
        self._size = size # Total number of buckets
        self._length = 0 # Number of filled buckets
        
        if args: # If the constructing argument has been passed
            # The constructing argument must be an iterable with each entry as an iterable that produces at least 2 elements
            # The first two produced elements for each entry are treated as the key and value
            for entry in args[0]:
                entry_iterator = iter(entry)
                key = next(entry_iterator)
                value = next(entry_iterator)
                self.add_item(key, value)

    # Adds the key-value pair to the hash table, makes necessary length and size changes
    def add_item(self, key, value):
        # Checks for resizing
        if self.key_membership(key) == False and self._length + 1 >= loading_factor*self._size: # Needs resizing
            self.resize()
        
        bit_masked_hash = hash_function(key)%self._size
        k = 0
        
        # Collision handling, value overwritng, etc
        while True:
            pos_to_check = (bit_masked_hash + k)%self._size
            if self._dict[pos_to_check][0] == "-": # empty slot found
                self._dict[pos_to_check] = [bit_masked_hash, key, value]
                self._length += 1
                break
            else:
                if self._dict[pos_to_check][1] == key:
                    self._dict[pos_to_check][2] = value
                    break
                else:
                    k += probing_step

    # Resizing works by re-evaluating hashes for all key-value pairs by considering current_size*mult_factor buckets
    def resize(self):
        self._size *= mult_factor
        self._dict = dictionary(self.get_key_value_list(), size = self._size).get_hash_table()
    
    # Returns the two-dimensional list with each entry of the format [ID, key, value], treated as the hash table
    def get_hash_table(self):
        return self._dict

    # Prints the corresponding hash table with all of it's buckets
    def show_hash_table(self):
        print("ID\t\tKey\t\tValue")
        print("-"*40)
        print()
        for entry in self._dict:
            print("\t\t".join(str(element) for element in entry))
        print()

    # Returns the number of filled buckets
    def get_length(self):
        return self._length

    # Returns the total number of buckets
    def get_size(self):
        return self._size

    # Returns a 2 dimensional list with each entry of the format [key, value]
    def get_key_value_list(self):
        return [[entry[1], entry[2]] for entry in self.get_hash_table() if entry[0] != "-"]

    # Checks for the membership of a key in the dictionary - is fast
    def key_membership(self, key):
        bit_masked_hash = hash_function(key)%self._size
        k = 0

        while True:
            pos_to_check = (bit_masked_hash + k)%self._size
            if self._dict[pos_to_check][0] == "-":
                return False
            elif self._dict[pos_to_check][1] == key:
                return True
            
            k += probing_step

    def delete_key(self, key):
        # A very primitive approach that makes another dictionary without the current entry - very time consuming
        # A consequence of this, though, is that on deleting an element, the hash table might resize
        if self.key_membership(key) == False:
            print(f"KeyError. The key {key} does not exist")
        else:
            new_dict = dictionary(entry for entry in self.get_key_value_list() if entry[0] != key)
            self._dict = new_dict.get_hash_table()
            self._size = new_dict.get_size()
            self._length = new_dict.get_length()
    
    # prints the dictionary in the traditional way
    def print(self):
        print("{" + ", ".join(": ".join(str(k) for k in entry) for entry in self.get_key_value_list()) + "}")
