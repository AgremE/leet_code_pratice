from typing import List
import copy 
import heapq
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        dict_char_heap = {}
        for i, c in enumerate(word1):
            _ord = ord(c)-ord('a')
            if _ord not in dict_char_heap:
                dict_char_heap[_ord] = []
                heapq.heapify(dict_char_heap[_ord])
            heapq.heappush(dict_char_heap[_ord],i)
        for i in range(len(word1)-len(word2)):
            change = 1
            result = []
            temp_heap =copy.deepcopy(dict_char_heap)
            for j,c_word2 in enumerate(word2):
                if word1[i+j] == c_word2:
                    if not result:
                        result.append(i+j)
                        continue
                    if result and (i+j)>result[-1]:
                        result.append(i+j)
                        continue
                if change == 1:
                    result.append(i+j)
                    change = 0
                    continue
                c = ord(c_word2) - ord('a')
                if c not in temp_heap:
                    break
                else:
                    found = False
                    while temp_heap[c]:
                        val = heapq.heappop(temp_heap[c])
                        if  val <= result[-1]:
                            continue
                        result.append(val)
                        found = True
                        break
                    if not found:
                        break
            if len(result) == len(word2):
                return result
        return []

solution = Solution()
print(solution.validSequence(word1="bbeigiibhjafjig",word2="abc"))