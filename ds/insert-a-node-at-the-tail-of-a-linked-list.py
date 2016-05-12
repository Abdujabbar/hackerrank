
 
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    while True:
        print(head.data)
        if head.next == None:
            break
        else:
            head = head.next

def InsertBottom(head, data):
    if head == None:
        return Node(data)
    else:
        r = head
        while True:
            if r.next == None:
                break
            else:
                r = r.next
        r.next = Node(data)
        head = r
        return head


def InsertTop(head, data):
    if head == None:
        return Node(data)
    else:
        r = Node(data)
        r.next = head
        head = r
        return head


def InsertNth(head, data, position):
    trackedHeadNode = head
    if head == None:
        return Node(data)

    if position == 0:
        nhead = Node(data, head)
        return nhead
    else:
        nhead = Node(data)
        c = 0
        while c < position - 1 and head.next != None:
            head = head.next
            c += 1

        nodeAtPosition = head.next
        head.next = nhead
        head = head.next
        head.next = nodeAtPosition
        return trackedHeadNode


def Delete(head, position):
    if position == 0:
        head = head.next
        return head
    head.next = Delete(head.next, position-1)
    return head

head = None
head = InsertNth(head, 4, 0)
head = InsertNth(head, 3, 1)
head = InsertNth(head, 5, 0)
head = Delete(head, 2)
print_list(head)
# print(head)

# n = int(input())
# head = None
# for i in range(n):
#     head = InsertTop(head, int(input()))
#
# print_list(head)
