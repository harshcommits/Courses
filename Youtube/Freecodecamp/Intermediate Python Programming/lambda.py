#lambdas are single line functions as below:

"""
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x*y
print(mult(2, 5))
"""

points2d = [(1, 2), (14, -1), (5, -1), (10, 4)]
sorted_list = sorted(points2d, key=lambda x: x[0] + x[1]) #points2d is sorted by the sum of x and y value in this case

print(points2d)
print(sorted(points2d))
print(sorted_list)
