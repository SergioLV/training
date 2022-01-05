# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    total_list_one = getTotalLinkedList(linkedListOne)
    total_list_two = getTotalLinkedList(linkedListTwo)

    return total_list_one + total_list_two


def getTotalLinkedList(linkedList):
    current = linkedList
    total = 0
    i = 0

    while current != None:
        total += current.value * 10**i
        i += 1
        current = current.next

    return total


a = LinkedList(0)
a.next = LinkedList(2)
b = LinkedList(0)
b.next = LinkedList(1)

print(sumOfLinkedLists(a, b))
