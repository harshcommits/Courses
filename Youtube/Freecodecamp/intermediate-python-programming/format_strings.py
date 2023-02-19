# %s=string %d=int %f=float

var = 3.1443
my_string = "The variable is %s" % var
print(my_string)

# .format method
var2 = 4.134554546
string2 = "The variable is {:.2f} and {}".format(var,var2)
print(string2)

# f-strings (new method)
var4 = 3243.234
var5 = 234

print(f"The variable is {2*var4} and {var5}")