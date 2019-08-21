"""
Implementation of linkedlist
"""
class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList(object):
    
    def __init__(self, key, value):
        self.head = Node(key, value)

    def add_at_end(self, key, value):
        n = self.head
        while n.next != None:
            n = n.next

        n.next = Node(key, value, prev=n)
        return self.head

    def get(self, key):
        if self.head.key == key:
            return self.head
        n = self.head
        while n.next != None or n.key == key:
            n = n.next
        
        if n.key == key:
            return n

        return None

    def remove(self, key):
        if self.head.key == key and self.head.next != None:
            self.head = self.head.next
            return self.head
        elif self.head.key == key and self.head.next == None:
            return None
        
        n = self.head
        while n.next != None:
            if n.key == key:
                n.prev.next = n.next
                n.next.prev = n.prev
                return self.head
            n = n.next

        if n.key == key:
            n.prev.next = None
        return self.head

    
def main():
    ll = LinkedList('1', 1)
    for i in range(2,12):
        ll.add_at_end(str(i), i)

    n = ll.head
    while n.next != None:
        print n.key
        n = n.next

    ll.remove('6')

    print '\n###########'
    n = ll.head
    while n.next != None:
        print n.key
        n = n.next


if __name__ == '__main__':
    main()       
    