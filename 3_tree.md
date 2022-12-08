# **Binary Search Tree**

## **Definition of Binary Search Tree**

A binary search tree like a linked list is a set of nodes and allow us to maintain a sorted list of numbers. Each node stores an item, for example for every node (N), all items in its left subtree are smaller than N and all the items in its right subtree are larger than N. It is called binary tree because each node has a maximum of two children. It is called a search tree because it can be used to search a number in O(log n) time. 

![Binary Search Tree](images/bst_2.png)

## **Example of Binary Search Tree**

A Binary Search Tree is constracted in the following way: 

![Binary Search Tree Example](images/bst_1.png)

As look in the image we inserted 7 elements in the Binary Tree, 70, 31, 93, 94, 14, 23, 73. The element 70 was the first item inserted into the tree, this is called the **root**. Next, 31 is less than 70, so it becomes to be inserted to left of 70, this is **left child** of 70. Next, 93 is greater than 70, so it becomes the right **right child** of 70. Here we have completed two levels of the three filled. Next item will be inserted to the left of to the right child of either 31 or 93. Here in our example, 94 is greater than 93 so it becomes the right of 93, we complete the binary tree with this pattern to create a balance binary tree. 

## **Common Operations i a BST**

| Operation in BST | Description | Performance |
| --- | --- | --- |
insert(value) | Insert a value into the tree | O(log n) Recursively search the subtrees to find the next available spot.
remove | Remove a value from the tree | O(log n) Recursively search the subtrees to fin the value and then remove it. This will require some cheanup of the adjacent nodes. 
search(value) | Determine if a value is in the tree. | O(log n) Recursively search the subrees to find the value. 
traverse_reverse | Visit all objects from smallest to largest. | O(n) Recursively traverse the left subtree and then the right subtree.
traverse_reverse | Visit all objects from largest to smallest. | O(n) Recursively traverse the right subtree and then the left subtree.
height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided. | O(n) Recursively find the height of the left and right subtrees and then return the maximum height (plus one to account for the root).
size() | Return the size of the BST | O(1) The size is amintained within the BST class. 
empty() | Return true if the root node is empty. This can also be done by checking the size for O. | O(1) The comparison of the root node or the size. 

## **Implementing of a BST in Python**

To implement a Binary Search Tree we will use the properties or operations of BST above. 
First we can implement a binary tree node in python as follows. 

```.py
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
```

A BST class that will be use by the user. 

```.py
class BST:
    def __init__(self):
        self.root = None
```

## **Problem to solve**

The problem to resolve will be pretty simple. We will performance an insertion, then we will find the height of the BST and lastly we will search an element in the tree. For all the operation we will start from the root. 

## **Solution**

[Solution](bst.py)