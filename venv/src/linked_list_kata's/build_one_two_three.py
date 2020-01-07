class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head,data):
    newNode = Node(data)
    newNode.next = head
    return newNode

def build_one_two_three():
    return push(push(Node(3), 2), 1)
