from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1
