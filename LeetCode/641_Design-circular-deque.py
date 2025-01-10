# https://leetcode.com/problems/design-circular-deque/description/

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.length = 0
        self.max = k

    def insertFront(self, value: int) -> bool:
        if self.length >= self.max:
            return False
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.length >= self.max:
            return False
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return True    

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        if self.head == self.tail: 
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length >= self.max
