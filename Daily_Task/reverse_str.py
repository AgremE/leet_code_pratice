class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list_str = s.split(" ")
        list_str = [x for x in list_str if x != ""]
        return " ".join([list_str[i] for i in range(len(list_str) - 1, -1, -1)])


str = "a good   example"
solution = Solution()
print(solution.reverseWords(str))
