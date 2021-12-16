class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList

    while current != None:
        if current.next != None and current.value == current.next.value:
            if current.next.next != None:
                current.next = current.next.next
            else:
                current.next = None
        else:
            current = current.next

    return linkedList


def printLinkedList(linkedList):
    current = linkedList
    while current != None:
        print(current.value)
        current = current.next
    return


a = LinkedList(3)
a.next = LinkedList(4)
a.next.next = LinkedList(4)
a.next.next.next = LinkedList(4)
a.next.next.next.next = LinkedList(5)

printLinkedList(a)
b = removeDuplicatesFromLinkedList(a)
print("==============")
printLinkedList(b)
