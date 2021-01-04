from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    def __init__(self):
        self.count = 0
        self.head = None
        
    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        return self.count


    def isEmpty(self) :
        if self.count == 0:
            return True
        return False

    def push(self, data) :
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
        self.count += 1

    def pop(self) :
        if self.isEmpty():
            return -1
        popped = self.head.data
        self.head = self.head.next
        self.count -= 1
        return popped


    def top(self) :
        if self.isEmpty():
            return -1
        return self.head.data

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