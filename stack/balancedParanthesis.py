
from sys import stdin

def isBalanced(expression) :
    stack = []
    for i in range(0, len(expression)):
        if expression[i] == "(":
            stack.append(expression[i])
        else:
            if len(stack) == 0:
                return False
            elif stack[len(stack)-1] == "(":
                stack.pop()
            
    if len(stack) <= 0:
        return True
    return False



#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
