class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > 2:
            cols = []
            digs = []
            len_s = len(s)
            start_pos = 0
            while start_pos < len_s:
                if len_s - numRows - start_pos > 0:
                    cols.append(list(s[start_pos : start_pos + numRows]))
                    start_pos = start_pos + numRows
                    if len_s - numRows - start_pos + 2 > 0:
                        digs.append(list(s[start_pos : start_pos + numRows - 2])[::-1])
                        start_pos = start_pos + numRows - 2
                    else:
                        digs.append(list(s[start_pos:])[::-1])
                        start_pos = len_s
                else:
                    cols.append(list(s[start_pos:]))
                    start_pos = len_s
            result = ""
            len_cols = len(cols)
            len_digs = len(digs)
            for i in range(numRows):
                if i == 0 or i == numRows - 1:
                    for col in cols:
                        if i < len(col):
                            result += col[i]
                else:
                    for i_col in range(len_cols):
                        if i < len(cols[i_col]):
                            result += cols[i_col][i]
                            if i_col < len_digs:
                                if numRows - i - 2 <= len(digs[i_col]) - 1:
                                    result += digs[i_col][::-1][numRows - i - 2]
                        else:
                            break
            return result
        else:
            first_half = ""
            second_half = ""
            for i in range(len(s)):
                if i % 2 == 0:
                    first_half += s[i]
                else:
                    second_half += s[i]
            return first_half + second_half


solution = Solution()

print(solution.convert(s="PINAASRGYLHIPI", numRows=4))
print(solution.convert(s="ABCDE", numRows=4))
