class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


# Creating a Stack object
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Pop elements
print(s.pop())  # 30
print(s.pop())  # 20
print(s.pop())  # 10
print(s.pop())  # Stack Underflow

class Stack:
    def __init__(self):
        self.Index = -1     #  represents an empty stack
        self.data = [0]*100 #used to store data in list with 0 to 99 index
    
    def push(self,X):
        if self.Index==99:
            print("stack is overflow")
            return
        
        self.Index += 1
        self.data[self.Index]=X
        return X
    
    def pop(self):
        if self.Index==-1:
            print("stack is underflow")
            return
       
        y=self.data[self.Index]
        self.Index -=1
        return y
    
s=Stack()
print(s.push(10))
print(s.push(20))
print(s.push(30))

print(s.pop())
print(s.pop())
print(s.pop())
        
