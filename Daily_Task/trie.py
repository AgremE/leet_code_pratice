class TreeNode:
    def __init__(self, val="root", child_node = []):
        self.val = val
        self.child_node = child_node
class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        _f_w = word[0]
        if _f_w in self.tree:
            pass
        else:
            tree = self.tree[_f_w]
            for i in range(1,len(word)):
                _w = word[i]
                child_node = tree.child_node
                found = False
                for child in child_node:
                    if child.val == _w:
                        found = True
                        tree = child
                if not found:
                    # construst new child node
                    new_w = TreeNode(_w)
                    child_node.append(new_w)
                    for j in range(i+1,len(word)):
                        new_w.child_node = [TreeNode(word[j])]
                        new_w = new_w.child_node[0]

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        s_w = prefix[0]
        if s_w not in self.tree:
            return False
        else:
            tree = self.tree[s_w]
        for i in range(1,len(prefix)):
            child_node = tree.child_node
            _w = prefix[i]
            found = False
            for child in child_node:
                if child.val == _w:
                    found = True
                    tree = child
            if not found:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)