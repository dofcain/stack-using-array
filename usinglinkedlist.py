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
        self.head = new_node       # Update top to new node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.head.data
        self.head = self.head.next  # Remove top node by moving top pointer
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
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
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())    # Output: 30
    print(s.peek())   # Output: 20
    print(s.size())   # Output: 2
