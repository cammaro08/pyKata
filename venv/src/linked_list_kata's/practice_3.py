class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#
# node1 = Node("3")
# node2 = Node("7")
# node3 = Node("10")
#
# node1.next = node2
# node2.next = node3
#
# traverse = node1
# while True:
#     print(traverse.value + " -> ", end="")
#     if traverse.next is None:
#         print("None")
#         break
#     traverse = traverse.next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        newNode = Node(value)
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
        print("none")


listy = LinkedList()
listy.printList()
listy.insert("3")
listy.printList()
listy.insert("44")
listy.printList()
listy.insert("512")
listy.printList()
