class Stack:
    def __init__(self, max_size):
        self.stack = [None] * max_size  
        self.top = -1                  
        self.max_size = max_size

    
    def push(self, data):
       
        if self.top == self.max_size - 1:
           
            print("Error: Stack Overflow. Cannot push", data)
            return False
        else:
           
            self.top += 1
          
            self.stack[self.top] = data
           
            print(f"Pushed {data} onto the stack.")
            return True

    
    def pop(self):
        
        if self.top == -1:
           
            print("Error: Stack Underflow. Cannot pop.")
            return None
        else:
           
            data = self.stack[self.top]
            self.stack[self.top] = None  
            self.top -= 1  
            print(f"Popped {data} from the stack.")
            return data

    
    def peek(self):
        
        if self.top == -1:
            
            print("Error: Stack is empty. Nothing to peek.")
            return None
        else:
            
            data = self.stack[self.top]
            print(f"Top element is {data}.")
            return data

   
    def display(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack[:self.top + 1])


stack = Stack(3)


stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)  

stack.display()


stack.peek()


stack.pop()
stack.pop()
stack.pop()
stack.pop()  

stack.display()
