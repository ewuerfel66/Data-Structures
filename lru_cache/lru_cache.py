from doubly_linked_list import DoublyLinkedList, ListNode

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
        # Check if key is in cache
        if key in self.cache.keys():
            cur = self.storage.head

            # Find the node
            while cur is not None:
                if list(cur.value.keys())[0] == key:
                    break
                else:
                    cur = cur.next

            # Move
            self.storage.move_to_front(cur)

            return cur.value

        else:
            return None


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
        if key in self.cache:
            # update value
            self.cache[key] = value

            # Move to front of DLL
            cur = self.storage.head
            while cur is not None:
                if cur.value == {key, value}:
                    break
                else:
                    cur = cur.next
            
            self.storage.move_to_front(cur)

        elif self.size < self.limit:
            # add length
            self.size += 1
            # add to cache and storage
            self.cache[key] = value
            self.storage.add_to_head({key: value})

        else:
            key_to_remove = self.storage.tail.key

            # Remove last one
            self.cache.pop(key_to_remove)
            self.storage.remove_from_tail()

            # add to cache and storage
            self.cache[key] = value
            self.storage.add_to_head({key: value})