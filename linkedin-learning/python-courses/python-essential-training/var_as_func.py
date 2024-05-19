x = 5

def x():
    return 5

if __name__ == "__main__":
    print(x.__code__.co_code)

    # lambda functions
    myList = [{'num': 5}, {'num': 4}, {'num': 3}, {'num': 2}]
    print(sorted(myList, key=lambda x: x['num']))