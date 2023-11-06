class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #
        # Observeration: the flip split in growth of 2
        # Split in the middle you will have the reverse numbetr between two half
        # #
        bi_str = "01101001"  # positional flip at n = 3
        if n < 3:
            return bi_str[k]
        flip_count = 0
        for i in range(n, 2, -1):
            # reverse flip until n = 3
            if k > 2**i:
                flip_count = flip_count + 1
                k = k % 2**i
        if flip_count % 2 == 0:
            return int(bi_str[k])
        else:
            return 1 if bi_str[k] == 0 else 0


solution = Solution()
print(solution.kthGrammar(n=30, k=417219134))
