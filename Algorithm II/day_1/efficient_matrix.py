from typing import List


class Solution:
    def find_range(self, matrix, target):
        first_col = [row[0] for row in matrix]
        for i in range(len(first_col)):
            if first_col[i] > target:
                break
        return 0, i

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_i, end_i = self.find_range(matrix, target)
        for i in range(start_i, end_i + 1):
            row_info = matrix[i]
            left_i = 0
            right_i = len(matrix[0]) - 1
            while left_i <= right_i:
                mid_i = (left_i + right_i) // 2
                num = row_info[mid_i]
                if num < target:
                    left_i = mid_i + 1
                elif num > target:
                    right_i = mid_i - 1
                else:
                    return True
        return False


test_solution = Solution()
test_case = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
test_case_2 = [[1]]
print(test_solution.searchMatrix(test_case, 3))
