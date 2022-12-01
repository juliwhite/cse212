# Linked List.

# Implement a node class. Constructor

class Node:
    def __init__(self, data=None):
        # Store the data 
        self.data = data

        # Store the next pointer. Initialize to None. It will be the 
        # last element of the linked List. Always the next pointer will be set to None. 
        self.next = None

# Next class will be the Linked List class. The user will work with this class. 
class Linked_list:
    def __init__(self):
        # Here we have the head. There is not data in the head, but the user is
        # going to access this node. This is going to be a placeholder that point 
        # to the first element in the list. 
        self.head = Node()

    # One important function is the append function. This is going to add a new node to 
    # the end of the current linked list. The append function will be used to create the 
    # first element in this linked list. 
    def append(self, data):
        # Create a new node of the class node.
        new_node = Node(data)

        # Create a variable to store the node that we are currently looking at. 
        # The cur variable is set the self.head because we are going to star at the leftmost
        # point in the linked list. 
        cur = self.head

        # The while loop will iterate through each node in the linked list. 
        # Once it gets to the next node that is None, we'll know that it is 
        # the last node. Once we find this we can insert a new node. 
        while cur.next is not None:
            cur = cur.next
        # Once we are at the last element of the linked list we can set cur.next to new_node. 
        cur.next = new_node

    # This lenght function we'll be helpful to implement if you want to manage the nodes in 
    # the linked list, or you want to know how large is the linked list. 
    def length(self):
        # Create a variable to point to the current node. In this case we set it to he head. 
        cur = self.head
        # Create a variable to count the total of nodes. 
        total = 0
        while cur.next is not None:
            # Increment total by one. 
            total += 1
            #Traverse through the next node.
            cur = cur.next
        return total
    
    # This function is to help you to see how the rest of the function are implemented. 
    def display(self):
        # Create a list to display the nodes of the linked list. 
        items = []

        # Set a variable for the current node we are looking at. 
        cur_node = self.head

        # Use while loop to traverse over the nodes in the linked list. 
        while cur_node.next is not None:
            cur_node = cur_node.next
            items.append(cur_node.data)
        print(items)

    # This function will get data from a linked list. 
    def get(self, index):
        # First, we check that index is not out of range of the linked List. 
        if index >= self.length():
            print("Out of range.")
            return None
        # We Create two variables to iterate later through the linked list. 
        cur_index = 0
        cur_node = self.head     # Star from the head.
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    # This function will delete a data from a provided index.
    def delete(self, index):
        # Check if we are out of range. if not we'll continue through a while loop.
        if index >= self.length():
            print("Out of range.")
            return None

        cur_index = 0
        cur_node = self.head
        while True:
            # When we delete a node we will have to append the last node to next node of 
            # the node that is being delete.
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:     # Check with the index that the user provide. 
                # We don't neccesary delete the node but we only point node before the node
                # that we want to "delete" and connected to the next node of the node that we 
                # want to delete. 
                last_node.next = cur_node.next
                return None
            cur_index += 1



# Create an instant of a linked list. 
my_list = Linked_list()

# Add numbers to our linked list. 
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

# Display the linked list
my_list.display()

# Get an element at second index. It would be the data "3"
print(my_list.get(2))

# Delete at index 2. It would be data "3"
my_list.delete(2)
my_list.display()


