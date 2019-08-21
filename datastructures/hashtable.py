"""
Hashtable implementation in python
"""

class HashNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable():

    def __init__(self):
        self.size = 10
        self.table = [HashNode(None, None)] * self.size

    def get(self, key):
        key_hash = hash(key)
        index = key_hash % self.size

        node = self.table[index]
        while(node.next != None and node.key != key):
            node = node.next

        if node.key == key:
            return node.value

        if node.next == None:
            return -1

        return None

    def put(self, key, value):
        # calculate hash of key
        key_hash = hash(key)

        index = key_hash % self.size

        node = self.table[index]
        while(node.next != None and node.key != key):
            node = node.next

        if node.next == None:
            node.next = HashNode(key, value)
            return True

        if node.key == key:
            node.value = value
            return True

        return False


def main():
    hash_table = HashTable()
    hash_table.put('a', 'a')
    hash_table.put('b', 'b')
    hash_table.put('c', 'c')
    hash_table.put('a', 'aa')
    hash_table.put('bb', 'bb')

    print hash_table.get('a')
    print hash_table.get('c')

    return

if __name__ == '__main__':
    main()


