class Solution:
    def decodeString(self, s: str) -> str:
        # I do believe this is useing stack but somehow I got stuck, let see what happens next
        # the algorithm go as followed
        num_stack = []
        string_stack = []
        result = []
        i = 0
        s = s[::-1]
        while i <= len(s) - 1:
            if s[i] == "[":
                # try to pop most of the number
                i += 1
                while s[i].isnumeric():
                    num_stack.append(s[i])
                    i += 1
                    if i == len(s):
                        break
                _mul = int("".join(num_stack[::-1]))
                num_stack = []
                cur_string = ""
                while string_stack:
                    temp_str = string_stack.pop(-1)
                    if temp_str == "]":
                        break
                    cur_string += temp_str
                cur_string = _mul * cur_string
                string_stack.append(cur_string)
            else:
                string_stack.append(s[i])
                i += 1
        return "".join(string_stack[::-1])


solution = Solution()
print(solution.decodeString(s="sd2[f2[e]g]i"))
