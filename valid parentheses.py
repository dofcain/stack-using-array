class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node    

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.head.data
        self.head = self.head.next  
        return popped_data
        
    def peek(self):
        if self.is_empty():
           return None
        return self.head.data


    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
if __name__ == "__main__":
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    string = input("Enter expression: ")
    valid = True
    for char in string:
        if char in ['(', '{', '[']:
            s.push(char)
        elif char in [')', '}', ']']:
            if s.is_empty():
                valid = False
                break
            top = s.peek()
            if top == pairs[char]:
                s.pop()
            else:
                valid = False
                break
    if not s.is_empty():
        valid = False
    print("Valid" if valid else "Invalid")
