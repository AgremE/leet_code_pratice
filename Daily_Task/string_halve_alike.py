class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        track_char = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        dict_first = {}
        dict_second = {}
        len_split = len(s) // 2
        total_first = 0
        total_second = 0
        for _i in range(len_split):
            first_char = s[_i]
            second_char = s[_i + len_split]
            if first_char in track_char:
                total_first = total_first + 1
            if second_char in track_char:
                total_second = total_second + 1
        if total_second == total_first:
            return True
        return False


solution = Solution()
print(solution.halvesAreAlike("AbCdEfGh"))
print(solution.halvesAreAlike("textbook"))
