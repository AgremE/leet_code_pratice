from collections import deque


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_ch_count = deque()
        init_char = s[0]
        count = 1
        for i in range(1, len(s)):
            if init_char == s[i]:
                count += 1
            else:
                list_ch_count.append((init_char, count))
                init_char = s[i]
                count = 1
        while len(list_ch_count) > 1:
            left_count = list_ch_count.popleft()
            right_count = list_ch_count.pop()
            if left_count[0] != right_count[0]:
                list_ch_count.append(left_count)
                list_ch_count.append(right_count)
                continue
        total_len = 0
        if list_ch_count:
            for char, count in list_ch_count:
                total_len += count
        return total_len
