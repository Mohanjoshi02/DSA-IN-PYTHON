class queue:
    def __init__(self):
        self.rear = -1     #  represents an empty queue
        self.data = [0]*100 #used to store data in list with 0 to 99 index
        self.front=0
        
    def push(self,X):
        if self.rear==99:
            print("queue is overflow")
            return
        
        self.rear += 1
        self.data[self.rear]=X
        return X
    
    def pop(self):
        if self.front > self.rear:
            print("queue is underflow")
            return
        y=self.data[self.front]
        self.front +=1
        return y
    
s=queue()
print(s.push(10))
print(s.push(20))
print(s.push(30))

print(s.pop())
print(s.pop())
print(s.pop())
