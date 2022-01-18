from timeit import default_timer as timer

my_list = ['a'] * 100000

#bad method
start = timer()
my_string = ''

for i in my_list:
     my_string += i
stop = timer()

print(stop-start)  #time taken: 0.01115140000001702

#good method; faster and cleaner

start2 = timer()
my_string = ''.join(my_list)
stop2 = timer()

print(stop2-start2) #time taken: 0.00038829999994050013