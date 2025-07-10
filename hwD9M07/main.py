class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def check_values(self):
        current = self.head
        while current:
            print(f"{current.value}", end=" <-> ")
            current = current.next
        print("None")

    def count(self):
        cnt = 0
        current = self.head

        while current:
            cnt += 1
            current = current.next
        return cnt

dll = DoublyLinkedList()

dll.append(14)
dll.append(13)
dll.append(12)

print(dll.count())

dll.check_values()