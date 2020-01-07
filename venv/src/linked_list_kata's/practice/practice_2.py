class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        traverse = self.head
        while True:
            if traverse.next is None:
                traverse.next = newNode
                break
            traverse = traverse.next

    def printList(self):
        traverse = self.head

        while traverse is not None:
            print(traverse.data, " -> ", end="")
            traverse = traverse.next
        print("none")


listy = LinkedList()
listy.appendAtEnd(1)
listy.appendAtEnd(2)
listy.appendAtEnd(3)
listy.printList()

