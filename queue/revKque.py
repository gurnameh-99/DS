
from sys import stdin
import queue

def reverseKElements(Queue, k) :
    if (Queue.empty() == True or
             k > Queue.qsize()):  
        return
    if (k <= 0):  
        return
  
    Stack = [] 
  
    # put the first K elements  
    # into a Stack 
    for i in range(k): 
        Stack.append(Queue.queue[0])  
        Queue.get() 
  
    # Enqueue the contents of stack  
    # at the back of the queue 
    while (len(Stack) != 0 ):  
        Queue.put(Stack[-1])  
        Stack.pop() 
  
    # Remove the remaining elements and  
    # enqueue them at the end of the Queue 
    for i in range(Queue.qsize() - k): 
        Queue.put(Queue.queue[0])  
        Queue.get()
    
    return Queue

'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
