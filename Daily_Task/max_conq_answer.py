class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ###
        # This is done by using recursion of exhusted search space
        # #
        memoir = {}

        def get_reverse(_s):
            if _s == "T":
                return "F"
            else:
                return "T"

        def recur_solution(tracker, curr_index, curr_max, memoir, answer_key, k):
            if k == 0:
                return curr_max
            if curr_index in memoir:
                return memoir[curr_index]
            curr_char = answer_key[curr_index]
            if curr_char == tracker:
                memoir[curr_index] = max(
                    recur_solution(
                        tracker, curr_index + 1, curr_max + 1, memoir, answer_key, k
                    ),
                    recur_solution(
                        get_reverse(tracker),
                        curr_index + 1,
                        0,
                        memoir,
                        answer_key,
                        k - 1,
                    ),
                )
            else:
                memoir[curr_index] = max(
                    recur_solution(
                        tracker, curr_index + 1, curr_max + 1, memoir, answer_key, k - 1
                    ),
                    recur_solution(
                        get_reverse(tracker),
                        curr_index + 1,
                        0,
                        memoir,
                        answer_key,
                        k,
                    ),
                )
