# Exercise Implementation of a Binary Search Tree (BST) data structure. 

# First we create a Node class, each node will have two children. Left and right child.
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left_child = None
        self.right_child = None

# Second we create the Binary Search Tree class. The user will interact with this class. 
class BST:
    def __init__(self) -> None:
        self.root = None

    # This function will insert in the BST. 
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            # If we can't insert in root we will call a private function inside of the 
            # function insert(). This function will be called recursively 
            self._insert(data, self.root)
    def _insert(self, data, curr_node):
        # First we check is the data is less than the curr_node. It will insert the data in the left.
        if data < curr_node.data:
            if curr_node.left_child == None:
                curr_node.left_child = Node(data)
            else:
                self._insert(data, curr_node.left_child)
        elif data > curr_node.data:
            if curr_node.right_child == None:
                curr_node.right_child = Node(data)
            else:
                self._insert(data, curr_node.right_child)
        else:
            print("This data exist in BST")
    def display(self):
        if self.root is not None:
            self._display(self.root)
    def _display(self, curr_node):
        if curr_node is not None:
            self._display(curr_node.left_child)
            print(str(curr_node.data))
            self._display(curr_node.right_child)

    # This function will get the height of the BST. 
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0 

    def _height(self, curr_node, curr_height):
        if curr_node == None:
            return curr_height
        left_height = self._height(curr_node.left_child, curr_height + 1)
        right_height = self._height(curr_node.right_child, curr_height + 1)
        return max(left_height, right_height)

    # This function will search for a node that contains the data. 
    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False
    def _search(self, data, curr_node):
        if data == curr_node.data:
            return True
        elif data < curr_node.data and curr_node.left_child != None:
            return self._search(data, curr_node.left_child)
        elif data > curr_node.data and curr_node.right_child != None:
            return self._search(data, curr_node.right_child)
        else:
            return False



tree = BST()

# Inserting integers in BST.
tree.insert(8)
tree.insert(4)
tree.insert(2)
tree.insert(10)
# Print the BST.
print("Display the BST.") 
tree.display()
print()

# Testing hight of BST.
print("BST height: ", str(tree.height()))
print()

# Testing search function. 
print("Search two numbers (10 and 100) in BST:")
print(tree.search(10))
print(tree.search(100))
    

