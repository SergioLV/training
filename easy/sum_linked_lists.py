# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum_1 = getSumLinkedList(linkedListOne)
    sum_2 = getSumLinkedList(linkedListTwo)

    return sum_1 + sum_2


def getSumLinkedList(linkedList):
    current = linkedList
    sum = 0

    while current != None:
        sum += current.value
        current = current.next

    return sum


a = LinkedList(1)
a.next = LinkedList(2)
b = LinkedList(3)
b.next = LinkedList(4)

print(sumOfLinkedLists(a, b))
