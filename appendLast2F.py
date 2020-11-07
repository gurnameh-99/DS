from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def cntNodes(node): 
    if (node == None): 
        return 0
          
    return (1 + cntNodes(node.next))


def appendLastNToFirst(head, n) :
    cnt = cntNodes(head) 
      
    if (cnt != n and n < cnt): 
          
        # Count of nodes to be skipped 
        # from the beginning 
        skip = cnt - n 
        prev = None
          
        curr = head 
          
        # Skip the nodes 
        while (skip > 0): 
            prev = curr 
            curr = curr.next
            skip-=1
              
        # Change the pointers 
        prev.next = None
        tempHead = head 
        head = curr 
          
        # Find the last node 
        while (curr.next != None): 
            curr = curr.next
              
        # Connect it to the head 
        # of the sub list 
        curr.next = tempHead 
    
    return head

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 