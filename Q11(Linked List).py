class ListNode:
    def __init__(self, pt, n=None):
        self.data = pt
        self.next = n

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def pushFront(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item, self.head)
            self.head = item
            self.size += 1
            return

    def pushBack(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item, None)
            if self.head is None:
                self.head = item
            else:
                self.tail.next = item
            self.tail = item
            self.size += 1
            return

    def remove(self, item):
        thisNode = self.head
        prevNode = None
        while thisNode:
            if thisNode.getData() == item:
                if prevNode:
                    prevNode.setNext(thisNode.getNext())
                else:
                    self.head = thisNode
                self.size -= 1
                return True
            else:
                prevNode = thisNode
                thisNode = thisNode.getNext()

    def search(self, item):
        thisNode = self.head
        while thisNode:
            if thisNode.getData() == d:
                return "Find"
            else:
                thisNode = thisNode.getNext()
        return "Nope"

    def outputList(self):
        print("[", self.head.getData(), end='')
        thisNode = self.head.getNext()
        while thisNode:
            print(", ", thisNode.getData(), end='')
            thisNode = thisNode.getNext()
        print("]")


LL = LinkedList()
LL.pushBack(1)
LL.pushBack(2)
LL.pushBack(3)
LL.remove(2)
LL.pushFront(0)
LL.pushBack(4)
LL.outputList()