from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(postOrder, inOrder, n) :
    if(len(postOrder)==0):
        return None
    root = BinaryTreeNode(postOrder[n-1])
    rootIndex = -1
    for i in range(n):
        if inOrder[i] == postOrder[n-1]:
            rootIndex = i
            break
    if rootIndex == -1:
        return None
    leftInOrder = inOrder[0:rootIndex]
    rightInOrder = inOrder[rootIndex+1:]
    leftPostOrder = postOrder[0:len(leftInOrder)]
    rightPostOrder = postOrder[len(leftInOrder):n-1]

    leftTree = buildTree(leftPostOrder, leftInOrder, len(leftInOrder))
    rightTree = buildTree(rightPostOrder, rightInOrder, len(rightInOrder))
    
    root.left = leftTree
    root.right = rightTree

    return root

'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)