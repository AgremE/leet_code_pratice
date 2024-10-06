class TrieNode:
    def __init__(self, is_word=False) -> None:
        self.is_word = is_word
        self.childs = [None for _ in range(26)]


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for _c in word:
            if not curr.childs[ord(_c) - ord("a")]:
                curr.childs[ord(_c) - ord("a")] = TrieNode()
            curr = curr.childs[ord(_c) - ord("a")]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for _c in word:
            if not curr.childs[ord(_c) - ord("a")]:
                return False
        if curr.is_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for _c in prefix:
            if not curr.childs[ord(_c) - ord("a")]:
                return False
        return True
