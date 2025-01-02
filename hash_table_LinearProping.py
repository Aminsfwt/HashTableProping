
#Hash Table Data Structure to deal with collision data using linear probing

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [ None for i in range(self.max)]

    #Function to get the Hash Table index
    def get_hash(self,key):
        h = 0
        for c in key:
            h += ord(c)
        return (h % self.max)
    
    #Function to show how *range(x,y) works. It returns a list of numbers in range(x,y)
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]#range(index, len(self.arr))] list of numbers in range((index, len(self.arr))
    
    #Function to get the empty slot to put the collision data
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
    
    #Function to get data
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
            
    #Function to put the data in the table      
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        #print(self.arr)  
              
    #Function to delete the data
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)    
