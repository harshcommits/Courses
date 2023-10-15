from ref.ll import LL, LLNode

if __name__ == "__main__":

    sll = LL()
    # print(sll.size())

    # # adding values
    # sll.add_front(1)
    # sll.add_front(2)
    # sll.add_front(3)

    # print(sll.size())

    # sll.search(3)
    sll.add_front(1)
    sll.add_front(2)
    sll.add_front(3)
    sll.add_front(27)

    # print(sll.search('bird'))
    # print(sll.search(3))

    # test cases for data removal
    print(sll.remove(15))
    print(sll.head)
    print(sll.remove(27))
    # print(sll.remove(27))

    print(sll.head)
    print(sll.head.next)
