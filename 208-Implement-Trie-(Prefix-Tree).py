class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = {}
        self.end = False

class Trie:

    def __init__(self):
        self.tree = Node()

    def insert(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c not in curr.neighbors:
                curr.neighbors[c] = Node(c)
            curr = curr.neighbors[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for c in word:
            if c not in curr.neighbors: return False
            curr = curr.neighbors[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for c in prefix:
            if c not in curr.neighbors: return False
            curr = curr.neighbors[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)