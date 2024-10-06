from typing import List
import math
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def _generate_leading(x,input):
            result = []
            for i in range(1,input):
                if x == i//(10**(int(math.log10(i)))):
                    result.append(i)
            return result
        result = []
        for i in range(1,10):
            result.extend(_generate_leading(i,n))
        return result