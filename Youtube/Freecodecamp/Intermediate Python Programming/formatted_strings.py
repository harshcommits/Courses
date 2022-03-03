#Method 1: using %d, %s, %f(floating value) etc. (very old)

var = "Tom"
var2 = 20
my_string = "The variable is %s" %var
print(my_string)
my_string = "The variable is %d" %var2
print(my_string)
var_float = 3.1234343
float_string = "The variable is %.2f" %var_float
print(float_string) #print to 2 decimal places

#Method2: using .format

varf = 2.122234
out_str = "The variable is {:.3f}".format(varf)
print(out_str)

#using f-strings (since python3.6+)
varfs = 3.2312
varfs2 = 7

print(f"The variable is {varfs} and {varfs2}")