class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


node1 = Node("one")
node2 = Node("two")
node3 = Node("three")

node1.next = node2
node2.next = node3

printingNode = node1
while True:
    print(printingNode.data, "-> ")
    printingNode = printingNode.next
    if printingNode is None:
        break