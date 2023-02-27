from functools import reduce

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

print([x*2 for x in a])

#using filter function
print(list(filter(lambda x: x%2==0, a)))

#product of all elements in list a; using reduce
print(reduce(lambda x,y: x*y, a))