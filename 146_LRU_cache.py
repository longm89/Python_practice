class Node:
    def __init__(self,key,val,prev_node = None,next_node = None):
        self.val = val
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node
class Double_linked_list:
    def __init__(self):

        self.head = None
        self.tail = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # we keep a dictionary a, where a[key] points to a node in a Double linked list with val = value
        # head is the first element of the queue that will be taken out first
        # when an element is used, it will be moved to the tail of the Double linked list
        self.a = dict()
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.num_of_keys = 0

    def move_to_tail(self, node):
        # move a node to the tail of the Double linked list
        if node.prev_node:
            before = node.prev_node
            if self.head is node:
                self.head = before
            after = node.next_node
            node.prev_node = None
            node.next_node = self.tail
            self.tail.prev_node = node
            before.next_node = after
            if after:
                after.prev_node = before
            self.tail = node
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.a:
            self.move_to_tail(self.a[key])
            return self.a[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.a:
            self.a[key].val = value
            self.move_to_tail(self.a[key])
        else:
            if self.num_of_keys==self.capacity:
                self.num_of_keys -= 1
                self.a.pop(self.head.key)
                if not self.head.prev_node:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.prev_node
                    self.head.next_node = None
            self.a[key] = Node(key,value)
            self.num_of_keys += 1
            if (not self.tail) and (not self.head):
                self.tail = self.a[key]
                self.head = self.a[key]
            else:
                self.a[key].next_node = self.tail
                self.tail.prev_node = self.a[key]
                self.tail = self.a[key]




our_cache = LRUCache(5)

our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5)
our_cache.put(6, 6)

print(our_cache.get(3))   
