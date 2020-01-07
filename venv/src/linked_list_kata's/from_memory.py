class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __int__(self, head=None):
        self.head = head

    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, data):
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
            print(traverse.value, " -> ", end="")
            traverse = traverse.next
        print("None")


listy = LinkedList()
listy.printList()
listy.insertAtEnd("3")
listy.printList()
listy.insertAtEnd("44")
listy.printList()
listy.insertAtEnd("512")
listy.printList()
