class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Algorithm wide, find the larget ascill sum as longest common subsequence.
        So instead of the score of the sequence is not based on the total len
        but based on the ascill sum
        min = total - max
        that the logic
        """
