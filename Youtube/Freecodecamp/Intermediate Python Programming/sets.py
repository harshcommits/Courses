myset = {1, 2, 3, 1, 2}   #unordered, mutable
print(myset)  #doesn't print duplicates
myset.add(4)
myset.remove(1)  #can also use myset.discard(1); doesn't throw error even if value not present
print("myset after operations", myset)

#print list as set
list_set = set(["Harsh", "Shyam", "Sundar"])
print(list_set)

#pop operations
print("Value popped out of set: ", list_set.pop()) #pop prints out random value which gets popped out of set
print("Remaining values: ", list_set)

#union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

print("union of odds and evens: ", odds.union(evens))
print("Intersection of odds and evens: ", odds.intersection(evens))

#print difference of odds and primes
print(odds.difference(primes))