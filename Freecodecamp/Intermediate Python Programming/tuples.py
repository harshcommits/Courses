import sys

example = ("Max", 28, "Boston")  #can declare tuples without parentheses
print(type(example))

print(example[2])
print(len(example))

example2 = 'a', 'p', 'p', 'l', 'e'

print(example2.count('p'))
print(example2.index('p')) #returns first occurence in tuple

list_ex = list(example2)

#slicing

a = 1, 2, 3, 4, 5, 6, 7, 8

print(a[1:5:2])
print(a[::-1])  #can use this to reverse tuple

#using variables for tuple elements

name, age, city = example
print(f"{age} years old {name} lives in {city}")

#grouping multiple items via variables

i1, *i2, i3, i4 = a
print(i1)
print(i3)
print(i4)
print(i2) #printed as a list

#size comparison between tuple and list
b = list(a)

print(sys.getsizeof(a), bytes) #tuple size: 104 bytes; more efficient for memory consumption
print(sys.getsizeof(b), bytes) #list size: 120 bytes
