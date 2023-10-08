from ref.ll import LL, LLNode

if __name__ == "__main__":

    # node = DLLNode('apple')
    # # print(node.get_data())

    # node.set_data(7)
    # print(node.get_data())

    # node1 = DLLNode('carrot')
    # node.set_next(node1)
    # # print(node.get_next())

    # node2 = DLLNode('brocolli')
    # node1.set_next(node2)
    # # node2.set_previous(node1)
    # node2.set_prev(node1)
    # print(node.get_next())
    # # print(node2.get_previous())
    # print(node2.get_prev())
    # print(node2.get_data())

    # sll = LL()
    # print(sll.head)
    # sll.add_front('berry')
    # print(sll.head)

    sll = LL()
    print(sll.size())

    # adding values
    sll.add_front(1)
    sll.add_front(2)
    sll.add_front(3)

    print(sll.size())
