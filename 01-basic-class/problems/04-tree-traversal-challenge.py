# In this practice, you will use classes to implement a binary search tree and
# perform pre-order, in-order, and post-order traversal of the tree.

# Implement a class Node with a constructor method that defines the following
# instance properties:
# - The lefthand child of the node, initialized to None
# - The righthand child of the node, initialized to None
# - The value of the node, initialized to the value passed into the constructor

# Implement another class Tree with the following instance methods:
# - insert() that takes in the root node and a new node and places the new node
#   in the correct location in the binary search tree
# - preorder_traversal() that traverses the tree and prints the value of each
#   node in pre-order succession
# - inorder_traversal() that traverses the tree and prints the value of each
#   node in in-order succession
# - postorder_traversal() that traverses the tree and prints the value of each
#   node in post-order succession

# Write your class here.
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def insert(self, curr, new_node):
        if not curr:
            return new_node
        
        if curr.value == new_node.value:
            return
        
        else:
            if curr.value < new_node.value:
                curr.right = self.insert(curr.right, new_node)
            
            else:
                curr.left = self.insert(curr.left, new_node)

            return curr

    def preorder_traversal(self, node):
        if node:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)


tree = Tree()

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))

print("** PRE ORDER: **")
tree.preorder_traversal(root) # 4, 1, 2, 3

print("** IN ORDER: **")
tree.inorder_traversal(root) # 1, 2, 3, 4

print("** POST ORDER: **")
tree.postorder_traversal(root) # 3, 2, 1, 4