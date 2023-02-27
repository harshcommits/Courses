from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

#not a lot of use cases for count, cycle, repeat; can read for more

a = [1, 2, 4, 1]
b = [3]

#product
prod = product(a,b, repeat=2)
print(list(prod))

#permutations
perm = permutations(a, 2)
print(list(perm))
comb = combinations(a, 2)
print(list(comb))

#combinations with iterations
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

#accumulate: generates cumulative sums for lists
acc = accumulate(a)
print(list(acc))

#cumulative product(multiplied) list
acc_mul = accumulate(a, func=operator.mul)
print(list(acc_mul))

#with max func
acc_max = accumulate(a, func=max)
print(list(acc_max))

#groupby
def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

print("break")

persons = [{'Name': 'Tim', 'Age': 34}, {'Name': 'Tom', 'Age': 14}, {'Name': 'Ram', 'Age': 14}, {'Name': 'Shyam', 'Age': 12}]

group_obj2 = groupby(persons, key=lambda x: x['Age'])
for key, value in group_obj2:
    print(key, list(value))