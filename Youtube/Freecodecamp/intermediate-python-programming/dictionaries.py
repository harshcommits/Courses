mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)
print(mydict["name"])
print(mydict.values())

#reading keys; similarly can assign to values
for key in mydict.keys():
     print(key)

#adding values
mydict["email"] = "testemail.google.com"
print(mydict)

#delete values
del mydict["name"]
print(mydict)

#copy dictionary

sample_test_dict = mydict #both reference same dictionary in memory
copy_dict = mydict.copy() #here 2 different entities are created
sample_test_dict["name"] = "Max"
print(sample_test_dict)
print(copy_dict)


#another way to declare dictionary
mydict2 = dict(name="Mark", age=27, city="Boston")
print("Second Dictionary: ", mydict2)

mydict2.pop("age")
mydict2.popitem()  #removes last item from dictionary
print("Second dictionary values after pop:", mydict2.values())

#using tuples as dicitionaries
tup = (1, 2, 3)
tup_dict = {tup: 6}
print("Tuple dictionary: ", tup_dict)
