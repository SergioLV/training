class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def printLinkedList(linkedList):
    current = linkedList

    while current != None:
        print(current.value)
        current = current.next
    return


def reverseLinkedList(linkedList):
    stack = []
    current = linkedList

    while current != None:
        stack.append(current.value)
        current = current.next
    newLinkedList = LinkedList(stack.pop())

    current = newLinkedList
    while stack != []:
        current.next = LinkedList(stack.pop())
        current = current.next

    return newLinkedList


a = LinkedList(1)
a.next = LinkedList(2)
a.next.next = LinkedList(3)
a.next.next.next = LinkedList(4)

b = reverseLinkedList(a)
printLinkedList(b)
