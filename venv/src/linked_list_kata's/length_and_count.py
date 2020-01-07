class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


def build_one_two_three():
    return push(push(Node(3), 2), 1)

#
# def length(node):
#     traverse = node
#     count = 0
#
#     while traverse is not None:
#         count += 1
#         traverse = traverse.next
#     return count
#
# def count(node, value):
#     traverse = node
#     count = 0
#
#     while traverse is not None:
#         if traverse.data == value:
#             count += 1
#         traverse = traverse.next
#     return count

def length(node):
    noOfNodes = 0
    while node:
        noOfNodes += 1
        node = node.next
    return noOfNodes

def count(node,value):
    occurrences = 0
    while node:
        if node.data == value:
            occurrences += 1
        node = node.next
    return occurrences

