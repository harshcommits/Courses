from ref.ll_def import LLNode, DLLNode

if __name__ == "__main__":

    node = DLLNode('apple')
    # print(node.get_data())

    node.set_data(7)
    print(node.get_data())

    node1 = DLLNode('carrot')
    node.set_next(node1)
    # print(node.get_next())

    node2 = DLLNode('brocolli')
    node1.set_next(node2)
    # node2.set_previous(node1)
    node2.set_prev(node1)
    print(node.get_next())
    # print(node2.get_previous())
    print(node2.get_prev())
    print(node2.get_data())