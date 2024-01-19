from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def can_pass(gas, cost, i):
            result = gas[i]
            for _i in range(i + 1, len(gas)):
                result = result - cost[_i - 1] + gas[_i]
                if result <= 0:
                    return False
            for _i in range(i + 1):
                result = result - cost[_i - 1] + gas[_i]
                if result <= 0:
                    return False
            return True

        last_cost = cost[-1]
        del cost[-1]
        cost.insert(0, last_cost)
        benefit = []
        for i in range(len(gas)):
            benefit.append(gas[i] - cost[i])
        i = 0
        while i <= len(gas) - 1:
            if benefit[i] < 0:
                i += 1
                continue
            else:
                if can_pass(benefit[:], cost, i):
                    return i
                _next = i + 1
                next_positive = False
                while _next < len(gas) - 1:
                    if benefit[_next] > 0:
                        if next_positive:
                            break
                        _next += 1
                    else:
                        _next += 1
                        next_positive = True
                i = _next
        return -1


solution = Solution()
print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(solution.canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]))
print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
