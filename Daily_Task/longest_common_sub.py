class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recure(text1, text2, text1_i, text2_i, memoir):
            if (text1_i, text2_i) in memoir:
                return memoir[(text1_i, text2_i)]
            if text1_i == len(text1) - 1:
                memior[(text1_i, text2_i)] = (
                    1 if text1[text1_i] in text2[text2_i:] else 0
                )
                return memior[(text1_i, text2_i)]
            if text2_i == len(text2) - 1:
                memior[(text1_i, text2_i)] = (
                    1 if text2[text2_i] in text1[text1_i:] else 0
                )
                return memior[(text1_i, text2_i)]
            if text1[text1_i] == text2[text2_i]:
                memoir[(text1_i, text2_i)] = (
                    recure(text1, text2, text1_i + 1, text2_i + 1, memoir) + 1
                )
            else:
                memoir[(text1_i, text2_i)] = max(
                    recure(text1, text2, text1_i + 1, text2_i, memoir),
                    recure(text1, text2, text1_i, text2_i + 1, memoir),
                )
            return memoir[(text1_i, text2_i)]

        memior = {}
        recure(text1, text2, 0, 0, memior)
        return memior[(0, 0)]


solution = Solution()
print(solution.longestCommonSubsequence(text1="a", text2="n"))
