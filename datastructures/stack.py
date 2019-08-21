"""
Stack implementation in python
"""
class EmptyStack(Exception):
    pass

class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None

    def add(self, data):
        if not self.top:
            # its emtpy, add at top
            self.top = StackNode(data)
            return

        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
        return

    def pop(self):
        if self.top == None:
            raise EmptyStack

        result = self.top.data
        self.top = self.top.next

        return result

    def is_empty(self):
        return self.top == None
    
    
def main():
    stack = Stack()
    for i in range(0,10):
        stack.add(i)

    print stack.is_empty()

    while stack.top != None:
        print stack.pop()

    print stack.is_empty()

    return

if __name__ == '__main__':
    main()