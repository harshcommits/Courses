from timeit import default_timer as timer

my_string = "Hello World" #strings are immutable
print(my_string[1:4:2])
print(my_string[::-1])  #reverses string

white = "  White spaces   "
print(white.strip())
print(white) #original string still has whitespaces

print(my_string.upper())  #similarly can use .lower() for lowercase

print(my_string.startswith("Hell")) #similarly can use endswith()

print(my_string.count('o'))
print(my_string.replace("World", "Harsh"))

#lists and strings

string_new = "How are you doing"
mylist = string_new.split(" ")

print("String in list form: ", mylist)

#convert list to string
list_string = ' '.join(mylist) #whatever is between single quotes will be in between list elements when printed
print(list_string)

#convert list to string
test_list = ['a'] * 6

#bad method
test_str = ''

for i in test_list:
     test_str += i
print(test_str)

#good method; much faster and efficient
list_2 = ['b'] * 6

list_str = ''.join(list_2)
print(list_str)
