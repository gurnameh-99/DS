
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False

def reverseStack(inputStack, extraStack) :
    if len(inputStack) <= 1:
        return
    while(len(inputStack) != 1):
        extraStack.append(inputStack.pop())
    lastElement = inputStack.pop()
    while(len(extraStack) != 0):
        inputStack.append(extraStack.pop())
       
    reverseStack(inputStack, extraStack)
    
    inputStack.append(lastElement)
    
    return inputStack


'''-------------- Utility Functions --------------'''

#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


#main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
