class Node:
    def __init__(self, value):
        self.value = value
        self.children = {} # dict so you can search for the char as key and the Node for that char as the value.
        self.end = False #You set to false as it means its not a complete word seen, when you have seen a complete word you set this to True

class Trie:

    def __init__(self):
        self.tree = Node('*')

    def insert(self, word: str) -> None:
        curr = self.tree
        # print(word)
        for c in word:
            # print(c)
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for c in word:
            if c not in curr.children: return False
            curr = curr.children[c]
        return curr.end  # If the last node has its end set to true the word exists and not just a prefix. 

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for c in prefix:
            if c not in curr.children: return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)