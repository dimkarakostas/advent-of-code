class DListNode:
    """
    A node in a doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head.next
        start = self.head
        nodes.append(repr(start))
        while curr != start:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def add(self, data):
        """
        Insert a new element next to the node "node" and make it the list's head.
        Takes O(1) time.
        """
        if not self.head:
            newNode = DListNode(data=data)
            newNode.prev = newNode
            newNode.next = newNode
            self.head = newNode
        else:
            newNode = DListNode(data=data, prev=self.head, next=self.head.next)
            self.head.next.prev = newNode
            self.head.next = newNode
            self.head = newNode

    def removeHead(self):
        """
        Unlink the head of the list.
        Takes O(1) time.
        """
        prev_head = self.head
        self.head = prev_head.next
        prev_head.prev.next = prev_head.next
        prev_head.next.prev = prev_head.prev
        return prev_head
