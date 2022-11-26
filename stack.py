# Reverse a string with Stack Data Structure.


# Define a class.
class Stack:
    def __init__(self) -> None:
        self.strings = []

    # This function will add each item to the stack. 
    def push(self, letter):
        self.strings.append(letter)

    # This function will remove the letter from the stack. 
    def pop(self):
        return self.strings.pop()
    
    # Check if stack is empty.
    def is_empty(self):
        return self.strings == []

    # Return the top letter in the stack.
    def peek(self):
        if not self.is_empty():
            return self.strings[-1]

    # Return the stack of strings.
    def get_stack(self):
        return self.strings

    
# Define a function
# This function will loop character by character onto the stack. 
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    # Define an empty string.
    reverse = ""

    # Here we pop character one by one and return thr reverse string.
    while not stack.is_empty():
        reverse += stack.pop()
    return reverse

# Create an object.
stack = Stack()
input_string = "data structure"

# Call the function reverse_string.
result = reverse_string(stack, input_string)

# Print result.
print(result)


        
    
