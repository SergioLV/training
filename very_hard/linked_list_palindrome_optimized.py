class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


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


def linkedListPalindrome(linkedList):
    reversedLL = reverseLinkedList(linkedList)

    current_ordered = linkedList
    currend_reversed = reversedLL

    while current_ordered != None:
        if current_ordered.value == currend_reversed.value:
            current_ordered = current_ordered.next
            currend_reversed = currend_reversed.next
            continue
        else:
            return False

    return True


a = LinkedList(1)
# a.next = LinkedList(2)
# a.next.next = LinkedList(2)

print(linkedListPalindrome(a))
