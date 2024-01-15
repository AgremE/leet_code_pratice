class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 1:
            if target <= k:
                return 1
            else:
                return 0
        total = sum(
            [self.numRollsToTarget(n - 1, k, target - pos) for pos in range(1, k + 1)]
        )
        return total
