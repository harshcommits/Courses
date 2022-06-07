
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #searching the nodes
    def search(self, target):
        if self.data == target:
            print(f"Found {self.data}")
            return None

        #check if data is on the left nodes; if yes, search recursively through all left nodes
        if self.left and self.data > target:
            return self.left.search(target)

        #check if data is on the right nodes; if yes, search recursively through all right nodes
        if self.right and self.data < target:
            return self.right.search(target)

        print("Data not in tree")

    #traversal methods
    def traversePreOrder(self):
        print(self.data)
        if self.left:
            self.left.traversePreOrder()

        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()

        print(self.data)
        
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()

        if self.right:
            self.right.traversePostOrder()
        
        print(self.data)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    #add another wrapper for search function
    def search(self, target):
        return self.root.search(target)

    #wrappers for traversal functions
    def traversePreOrder(self):
        self.root.traversePreOrder()

    def traverseInOrder(self):
        self.root.traverseInOrder()

    def traversePostOrder(self):
        self.root.traversePostOrder()

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(23)

myTree = Tree(node, "My tree")

# #print node data
# print(node.right.data)
# print(node.right.right.data)

#prints data from myTree instance
print(myTree.name)
print(myTree.root.right.data)

#search for a value in tree
#found = myTree.root.search(23)

#using the search function in the Tree class, instead of the parent Node class
found = myTree.search(23)

#traverse the tree
print("Traversing Pre-Order\n")
myTree.traversePreOrder()

print("Traversing In-Order\n")
myTree.traverseInOrder()

print("Traversing Post-Order\n")
myTree.traversePostOrder()