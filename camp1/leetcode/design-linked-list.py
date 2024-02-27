class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        ans = [self.val]
        temp = self.next

        while temp:
            ans.append(temp.val)
            temp = temp.next

        return '->'.join(map(str, ans))

class MyLinkedList:

    def __init__(self):
        self.dummy = Node(0)

    def get(self, index: int) -> int:
        curr = self.dummy

        for i in range(index + 1):
            curr = curr.next
            if curr == None:
                return -1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        print(self.dummy)
        newNode = Node(val)

        newNode.next = self.dummy.next
        self.dummy.next = newNode

    def addAtTail(self, val: int) -> None:
        print(self.dummy)
        newNode = Node(val)

        curr = self.dummy
        while curr.next != None:
            curr = curr.next
            if curr == None:
                return
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        i = 0
        curr = self.dummy
        while i < index:
            i += 1
            curr = curr.next
            if curr == None:
                return
        newNode.next = curr.next
        curr.next = newNode 

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.dummy
        while i < index:
            i += 1
            curr = curr.next
            if curr == None:
                return
        if curr.next:
            curr.next = curr.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)