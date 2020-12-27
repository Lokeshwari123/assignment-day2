# insert element at any position in linkedlist

class Node_data:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
        # self.tail=None


def insert_pos(head, data, position):
    pos = 0
    current_head = head
    previous_head = head
    while pos <= position:
        if pos == position:
            new_head = Node_data(data)
            new_head.next = None
            return head
        elif head != None:
            temp = Node_data(data)
            for i in range(0, position-1):
                cur = current_head.next
                if cur.next == None:
                    break
            temp.next = current_head.next
            current_head.next = temp


def printlist(self):
    temp = self.head
    while temp:
        print(temp.data, end="")
        temp = temp.next


l = linkedlist()
