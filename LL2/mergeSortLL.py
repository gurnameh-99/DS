from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def midPoint(head) :
    if head == None:
        return None

    temp = head
    res = head
    while(temp.next != None and temp.next.next != None):
       res = res.next
       temp= temp.next.next

    return res

def mergeTwoSortedLinkedLists(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    elif head1 == None and head2 == None:
        return None
    final_head = None
    final_tail = None
    if head1.data < head2.data :
        final_head = head1
        final_tail = head1
        head1 = head1.next

    else:
        final_head = head2
        final_tail = head2
        head2 = head2.next

    while (head1 != None and head2 != None):
        if head1.data < head2.data :
            final_tail.next = head1
            head1 = head1.next
        else:
            final_tail.next = head2
            head2 = head2.next
        final_tail = final_tail.next

    if head1 == None:
        final_tail.next = head2
    else:
        final_tail.next = head1

    return final_head


def mergeSort(head) :
    if head is None or head.next is None:
        return head 
    mid = midPoint(head)
    head1 = head
    head2 = mid.next
    mid.next = None
    head1 = mergeSort(head1)
    head2 = mergeSort(head2)

    final_head = mergeTwoSortedLinkedLists(head1, head2)
    return final_head

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


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
