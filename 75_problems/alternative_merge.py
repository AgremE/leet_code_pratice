class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(len(word1)):
            if i >= len(word1) or i >= len(word2):
                break
            result += f"{word1[i]}{word2[i]}"
        if len(word1) == len(word2):
            return result
        if len(word1) > len(word2):
            result = result + f"{word1[i:]}"
        else:
            result = result + f"{word2[i+1:]}"
        return result


solution = Solution()
print(solution.mergeAlternately("abcd", "pq"))
