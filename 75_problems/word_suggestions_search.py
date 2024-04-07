from typing import List


class TrieNode:
    def __init__(self, is_word=False) -> None:
        self.is_word = is_word
        self.childs = [None for _ in range(26)]  # represent 26 char in english


class Trie:

    def __init__(self, products) -> None:
        self.root = TrieNode()
        self.result_search = []
        self._construct_tries(products)

    def _construct_tries(self, products):
        for product in products:
            self.insert_tries(product)

    def insert_tries(self, product):
        curr = self.root
        for _c in product:
            child_ind = ord(_c) - ord("a")
            if curr.childs[child_ind]:
                curr = curr.childs[child_ind]
            else:
                curr.childs[child_ind] = TrieNode()
                curr = curr.childs[child_ind]
        curr.is_word = True

    def dfs_prefix(self, curr, word):
        if len(self.result_search) == 3:
            return self.result_search
        if curr.is_word:
            self.result_search.append(word)
        for i in range(26):
            if curr.childs[i]:
                self.dfs_prefix(curr.childs[i], word + chr(ord("a") + i))

    def start_with_prefix(self, prefix):
        self.result_search = []
        curr = self.root
        for _c in prefix:
            child_ind = ord(_c) - ord("a")
            if curr.childs[child_ind]:
                curr = curr.childs[child_ind]
            else:
                return []
        self.dfs_prefix(curr, prefix)
        return self.result_search


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        tries = Trie(products=products)
        result = []
        skip_rest = False
        for i in range(1, len(searchWord) + 1):
            if skip_rest:
                result.append([])
                continue
            prefix = searchWord[:i]
            temp_result = tries.start_with_prefix(prefix)
            if temp_result == []:
                skip_rest = True
            result.append(temp_result)
        return result


solution = Solution()
print(solution.suggestedProducts(products=["havana"], searchWord="tatiana"))
