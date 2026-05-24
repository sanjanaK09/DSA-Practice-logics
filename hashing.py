#hashing is a technique used to convert data into a fixed-size value called a has value or hash code 
#this hash value heps store and search data very fast 
#
#hash function:---a hash function converts input--fixed index \ex- hash("apple")
#suppose table size=10
#formula--index = key % 10
#ex-- 25 %10=5
# 25 is stored at index 5
#
#Collision --
# 15--15%10---5
# 25--25%10---5
# 35--35$10---5

class HashTable:
    def __init__(self,size):
        self.size =size
        self.table=[[]for _ in range(size)]
    def hash_function(self,key):
        return key % self.size
    def insert(self,key):
        index = self.hash_function(key)
        self.table[index].append(key)
    def display(self):
        print(self.table)
h= HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()