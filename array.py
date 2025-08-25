class Stack:
  def __init__(self):
        self.stack=[]
  def push(self, item):
      self.stack.append(item) 

  def pop(self):
        return self.stack.pop() 
  def peek(self):
        return self.stack[-1] 
if __name__ == "__main__":
    s = Stack()
    l= list(map(int,input().split()))
    for element in l:
         s.push(element)
    print(f"{s.pop()} \n{s.peek()}")
         
