class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def get_num_partition(s, k):
            f_i = 0
            count_diff = {s[f_i]: 1}
            num_partion = 1
            while f_i != len(s):
                if s[f_i] not in count_diff:
                    if len(count_diff) == k:
                        count_diff = {}
                        num_partion += 1
                    else:
                        count_diff[s[f_i]] = 1
                f_i += 1
