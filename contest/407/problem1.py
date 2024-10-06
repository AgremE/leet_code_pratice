class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n < k:
            return -1
        b_n = bin(n)
        b_k = bin(k)
        first_digit = len(b_n) - len(b_k)
        result = first_digit
        result -= len([x for x in b_n[2 : first_digit + 2] if x == "0"])
        for i in range(first_digit + 2, len(b_n)):
            if b_n[i] == "1" and b_n[i] != b_k[i - first_digit]:
                result += 1
            if b_n[i] == "0" and b_k[i - first_digit] == "1":
                result = -1
                break
        return result


solution = Solution()
print(solution.minChanges(31, 32))
