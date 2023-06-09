#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    ######## After Init ##########
    #
    # ←←←←←←                ←←←←←←
    # ↓→→→→Tail→NotUsed←Head→→→→↓↑
    # ↓↑                        ↓↑
    # ↓↑←←←←←←←←←←←←←←←←←←←←←←←←↓↑
    # ↓→→→→→→→→→→→→→→→→→→→→→→→→→→↑
    #
    ##############################
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}  # (key, Node)
        self.head = Node(-1, None)
        self.tail = Node(-1, None)

        ### Tail point to the latest Node & Head to the oldest
        # self.head.prev # Not Used
        self.head.next = self.tail  # Dummy Head
        self.tail.prev = self.head  # Dummy Tail
        # self.tail.next # Not Used

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        node = self.hash[key]
        self._removeNode(node)
        self._addTailNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self._removeNode(self.hash[key])

        node = Node(key, value)
        self._addTailNode(node)
        self.hash[key] = node
        if len(self.hash) > self.capacity:
            self._evict()

    ### Self-Defined
    def _removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _addTailNode(self, node):
        lastValidNode = self.tail.prev
        lastValidNode.next = node
        node.prev = lastValidNode
        self.tail.prev = node  # lastValidNode = node
        node.next = self.tail

    def _evict(self):
        node = self.head.next  # the least recently used node
        self._removeNode(node)
        self.hash.pop(node.key)  # update hash (Remove)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
