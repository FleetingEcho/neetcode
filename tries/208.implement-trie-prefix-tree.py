class Trie:

    def __init__(self):
        self.root={}

    def traverse(self,word):
        node=self.root
        for c in word:
            if c not in node:
                return None
            node=node[c]
        return node

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node["isWord"]=True

    def search(self, word: str) -> bool:
        node=self.traverse(word)
        if node==None:
            return False
        return node.get("isWord",False) if "isWord" in node else False

    def startsWith(self, prefix: str) -> bool:
        node=self.traverse(prefix)
        return node is not None



#优化后

class Trie:

    def __init__(self):
        self.root = {}

    def traverse(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return None
            node = node[c]
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c]={}
            node=node[c]
        node["isWord"] = True

    def search(self, word: str) -> bool:
        node = self.traverse(word)
        return node is not None and node.get("isWord", False)

    def startsWith(self, prefix: str) -> bool:
        return self.traverse(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)