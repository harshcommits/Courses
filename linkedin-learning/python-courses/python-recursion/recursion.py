import turtle

MAX_LENGTH = 250
INCREMENT = 10

def draw_spiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    draw_spiral(a_turtle, line_length + INCREMENT)

def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_recursive(left) + middle + quicksort_recursive(right)

if __name__ == "__main__":

    # charlie = turtle.Turtle(shape="turtle")
    # charlie.pensize(5)
    # charlie.color("red")
    # draw_spiral(charlie, 10)
    # turtle.done()

    assert factorial_recursive(4) == 24

    array = [10, 7, 8, 9, 1, 5]
    print(quicksort_recursive(array))