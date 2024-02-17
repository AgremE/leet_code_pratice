from typing import List
import math


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen_num(c_d, n_l, high):
            result = 0
            if c_d * (10**n_l) > high:
                return None
            for i in range(n_l + 1):
                if c_d > 9:
                    return None
                result += c_d * (10 ** (n_l - i))
                c_d += 1
            return result

        def generate_all_num(low, high):
            len_low = int(math.log10(low))
            len_high = int(math.log10(high))
            result = []
            for _len in range(len_low, len_high + 1):
                for i in range(1, 10):
                    temp = gen_num(i, _len, high)
                    if temp:
                        result.append(temp)
                    else:
                        break
            return result

        result = generate_all_num(low, high)
        return [x for x in result if x > low and x < high]


solution = Solution()
print(solution.sequentialDigits(low=100, high=300))
