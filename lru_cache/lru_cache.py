from dll_queue import Queue
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.storage = Queue()
        self.cache = {}


    def __init__(self, limit=10):
        self.size = 0
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Update value
        value = self.cache[key]
        dll_entry = {key: value}
        node = self.storage.find_node(dll_entry)
        self.storage.move_to_front(node_to_move)
        return node.value


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # DLL
    def set(self, key, value):
        if self.size < self.limit:
            # add length
            self.size += 1
            # add to cache and storage
            self.cache[key] = value
            self.storage.add_to_head({key: value})
            self.storage.move_to_front({key: value})

        elif key in self.cache:
            # update value
            self.cache[key] = value

            # Move to front of DLL
            dll_entry = {key: value}
            node_to_move = self.storage.find_node(dll_entry)
            self.storage.move_to_front(node_to_move)


        else:
            # Remove last one
            self.cache.pop(key)
            self.storage.remove_from_tail()

            # add to cache and storage
            self.cache[key] = value
            self.storage.add_to_head({key: value})