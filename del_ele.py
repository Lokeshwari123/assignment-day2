# delete an element at begining in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, value):
        temp = self.head
        if (temp != None):
            print("you can't delete ,the list is empty")
            if (temp.data == value):
                self.head = temp.next
                temp = None
                return

    def printlist(self):
        temp = self.head
        while(temp):
            print("%d" % (temp.data)),
            temp = temp.next


list1 = LinkedList()
list1.push(1)
list1.push(3)
list1.push(6)
list1.push(8)

print("created linked list is")
list1.printlist()
list1.deleteNode(8)
print("linked list after deletion of 1")
list1.printlist()
