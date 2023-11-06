class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        reverse = False
        if n < 0:
            reverse = True
            n = -n

        while n > 0:
            last_bit = n & 1

            # Check if current LSB
            # is set
            if last_bit:
                ans = ans * x
            x = x * x

            # Right shift
            n = n >> 1
        if reverse:
            return float(1 / ans)
        return ans
