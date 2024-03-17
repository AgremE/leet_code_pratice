class Solution:
    def sortedSquares(self, nums):
        pos_elem = []
        neg_elem = []
        for i in nums:
            if i < 0:
                neg_elem.append(i)
            else:
                pos_elem.append(i)
        pos_elem = [x**2 for x in pos_elem]
        neg_elem = [x**2 for x in neg_elem]
        neg_elem = neg_elem[::-1]
        f_idx = 0
        s_idx = 0
        result = []
        while True:
            if f_idx >= len(pos_elem):
                result = result + neg_elem[s_idx:]
                return result
            elif s_idx >= len(neg_elem):
                result = result + pos_elem[f_idx:]
                return result
            elif pos_elem[f_idx] <= neg_elem[s_idx]:
                result.append(pos_elem[f_idx])
                f_idx = f_idx + 1
            elif pos_elem[f_idx] > neg_elem[s_idx]:
                result.append(neg_elem[s_idx])
                s_idx = s_idx + 1


test_solution = Solution()
print(test_solution.sortedSquares([-4, -1, 0, 3, 10]))
