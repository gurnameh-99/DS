
from sys import stdin
from queue import Queue

class Stack :
    def __init__(self):

        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0
        
    def getSize(self) :
        return self.curr_size
        
    def isEmpty(self) :
        if self.curr_size == 0:
            return True
        return False
        
    def push(self, data) :
        self.curr_size += 1
    
        self.q2.put(data)  
  
        # Push all the remaining  
        # elements in q1 to q2.  
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        # swap the names of two queues  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q
        
    def pop(self) :
        if (self.q1.empty()):
            return -1
        res = self.top()
        self.q1.get()
        self.curr_size -= 1
        return res
        
    def top(self) :
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]
		




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1