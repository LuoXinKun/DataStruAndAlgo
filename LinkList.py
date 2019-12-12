"""
链表基本操作
"""
class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self,data):
        item = Node(data)

        if self.head == None:
            self.head = item
            self.length += 1
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = item
            self.length += 1

    def print(self):
        p = self.head
        while p:
            print(p.data)
            p = p.next

    def printlength(self):
        print(self.length)

linklist = LinkList()
for i in range(10):
    if i%2 !=0:
        linklist.append(i)
linklist.print()
linklist.printlength()