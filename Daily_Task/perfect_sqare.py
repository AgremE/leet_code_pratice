from heapq import heapify, heappush, heappop


class Solution:
    def numSquares(self, n: int) -> int:
        heap = []
        heapify(heap)
        ### Generate all possible divider
        divider = [x**2 for x in range(1, 101)]
        for i in divider:
            score = n // i
            if score == 0:
                score = 10**5
            heappush(heap, [score, n % i])
        while heap:
            ## Pop min score associated node (score, reminder from previoud divided number)
            mid_score, reminder = heappop(heap)
            if reminder == 0:
                ### If found return, this condition will always meet as we have 1 as perfect squre
                return mid_score
            for i in divider:
                if i > reminder:
                    continue
                divided_score = reminder // i
                total_score = mid_score + divided_score
                heappush(heap, [total_score, reminder % i])


solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))
print(solution.numSquares(16))
