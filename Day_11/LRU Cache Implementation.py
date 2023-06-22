from sys import stdin
from collections import OrderedDict

class Node:
    def __init__(self, k=0, val=None, p=None, n=None):
        self.val = val
        self.keynode = k
        self.prev = p
        self.next = n


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value


# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
    query = list(map(int, stdin.readline().rstrip().split()))

    if query[0] == 0:
        key = query[1]
        print(cache.get(key))
    elif query[0] == 1:
        key = query[1]
        value = query[2]
        cache.put(key, value)

    q -= 1



# from sys import stdin


# class Node:
#     def __init__(self, k=0, val=None, p=None, n=None):
#         self.val = val
#         self.keynode = k
#         self.prev = p
#         self.next = n


# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.count = 0
#         self.d = {}
#         self.head = Node(-1, -1)
#         self.tail = Node(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def insertAfterHead(self, k, val):
#         node = Node(k, val)
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next = node
#         node.next.prev = node
#         node.keynode = k
#         node.val = val
#         return node

#     def deleteBeforeTail(self):
#         temp = self.tail.prev
#         temp.prev.next = self.tail
#         self.tail.prev = temp.prev
#         return temp

#     def get(self, key):
#         if key in self.d:
#             self.d[key] = self.insertAfterHead(key, self.d[key].val)
#             self.deleteBeforeTail()
#             return self.d[key].val
#         else:

#             return -1

#     def put(self, key, value):
#         if self.count == self.capacity:
#             if key not in self.d:
#                 x = self.deleteBeforeTail()
#                 self.d[key] = self.insertAfterHead(key, value)
#                 del self.d[x.keynode]
#             else:
#                 x = self.deleteBeforeTail()
#                 self.d[key] = self.insertAfterHead(key, value)
#         else:
#             if key in self.d:
#                 x = self.deleteBeforeTail()
#                 self.d[key] = self.insertAfterHead(key, value)
#             else:
#                 self.d[key] = self.insertAfterHead(key, value)
#                 self.count+=1



# # main
# capacity, q = map(int, stdin.readline().rstrip().split(" "))

# cache = LRUCache(capacity)

# while q != 0:
#     query = list(map(int, stdin.readline().rstrip().split()))

#     if query[0] == 0:
#         key = query[1]
#         print(cache.get(key))
#     elif query[0] == 1:
#         key = query[1]
#         value = query[2]
#         cache.put(key, value)

#     q -= 1
