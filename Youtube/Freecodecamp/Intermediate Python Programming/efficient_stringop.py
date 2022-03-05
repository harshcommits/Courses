from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print("concatenate string with + : %.5f" % (end - start))

# good
start = timer()
a = "".join(my_list)
end = timer()
print("concatenate string with join(): %.5f" % (end - start))
