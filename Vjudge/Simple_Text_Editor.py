import sys

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):

    def __init__(self, string):
        self.root = Node(string)
    
    def append(self, W):
        self.root.next = Node(self.root.data + W)
        self.root.next.prev = self.root
        self.root = self.root.next
    
    def delete(self, k):
        self.root.next = Node(self.root.data[:-k])
        self.root.next.prev = self.root
        self.root = self.root.next
    
    def print(self, k):
        print(self.root.data[k - 1])
    
    def undo(self):
        self.root = self.root.prev


Q = int(sys.stdin.readline())
string = DoubleLinkedList('')
for _ in range(Q):
    args = sys.stdin.readline().split()
    t = int(args[0])
    if t == 1:
        string.append(args[1])
    elif t == 2:
        string.delete(int(args[1]))
    elif t == 3:
        string.print(int(args[1]))
    elif t == 4:
        string.undo()
