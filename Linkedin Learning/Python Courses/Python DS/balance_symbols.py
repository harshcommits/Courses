class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def match_symbols(str_example):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()
    mystack = Stack()

    index = 0
    while index < len(str_example):
        symbol = str_example[index]

        if symbol in openers:
            mystack.push(symbol)
        else:

            if mystack.is_empty():
                return False
 
            else:
                top_item = mystack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
                    
            print(mystack.printvalues())

        index += 1

    if mystack.is_empty():
        return True

    return False

print(match_symbols('({[]})'))
#print(match_symbols('({[]})}'))