from collections import deque

def stack(values):
    pass

def search_array(value, list):
    pass

# uses queues
def print_binary_numbers(n):
    if n <= 0:
        return
    
    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)


if __name__ == "__main__":
    two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    the above 2d array should be seen as follows:
    1 2 3
    4 5 6
    7 8 9
    """

    print(two_d_list[1][2])

    # example for printing binary functions; foll. prints values up to 10
    print_binary_numbers(10)