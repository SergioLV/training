# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindromeBad(head):
    length = getLength(head)
    result = []

    count = 0
    current = head
    if length % 2 == 0:
        while current != None:
            count += 1
            if count <= length/2:
                result.append(current.value)
                current = current.next
            else:
                if current.value == result[len(result)-1]:
                    del result[len(result)-1]
                current = current.next
    else:
        while current != None:
            count += 1
            if count < length//2 + 1:
                result.append(current.value)
                current = current.next
            elif count == length//2 + 1:
                current = current.next
                continue
            elif count > length//2 + 1:
                if current.value == result[len(result)-1]:
                    del result[len(result)-1]
                current = current.next
    return result == []
# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    length = getLength(head)
    if length % 2 == 0:
        result = linkedListPalindromeEven(head, length)
    else:
        result = linkedListPalindromeOdd(head, length)

    return result


def linkedListPalindromeEven(head, length):
    slow_node = head
    current = head
    count = 0
    half = length/2
    goal = 0

    while current != None:
        count += 1
        a = slow_node.value
        b = current.value
        if count > half:
            if slow_node.value == current.value:
                goal += 1
                slow_node = slow_node.next
            else:
                return False
        current = current.next
    return goal == half


def linkedListPalindromeOdd(head, length):
    slow_node = head
    current = head
    count = 0
    half = length//2 + 1
    goal = 0

    while current != None:
        count += 1
        a = slow_node.value
        b = current.value
        if count > half:
            if slow_node.value == current.value:
                goal += 1
                slow_node = slow_node.next
            else:
                return False
        current = current.next
    return [goal + 1 == half, goal + 1, half]


def getLength(linkedList):
    current = linkedList
    length = 0
    while current != None:
        length += 1
        current = current.next
    return length


a = LinkedList(0)
a.next = LinkedList(1)
a.next.next = LinkedList(2)
a.next.next.next = LinkedList(2)
a.next.next.next.next = LinkedList(1)
a.next.next.next.next.next = LinkedList(0)


print(linkedListPalindrome(a))
