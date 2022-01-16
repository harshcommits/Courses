mylist = ["banana", "apple", "cherry"]
print(mylist)

print(mylist[0])

print(mylist[-1]) #prints last element

if "banana" in mylist:
     print("Banana is in the list")

print(len(mylist))

mylist.append("blueberry") #adds element at the endx
mylist.insert(1, "jackfruit")  #adds element at specified index

print(mylist)

mylist.remove("jackfruit")     #remove specific element
mylist.pop()  #removes element at the end

print(mylist)

print("list with gaps: ", mylist[0:2:1])  #order: startindex:stopindex:difference in index(default 1)
print(mylist[::-1])   #reverses the list

list1 = mylist #any changes to list1 will reflect in mylist as well, since both refer to same list in memory
list2 = mylist.copy()  #here both are separate entities

list1.append("test_fruit")

print("List 1: ", list1)
print("mylist: ", mylist)
print("list2: ", list2)

#modify list components 
test_list = [1, 2, 3, 4, 5]
new_list = [i*i for i in test_list] #squares of values in test_list
print("Test List: ", test_list)
print("New List: ", new_list)

