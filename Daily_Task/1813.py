class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        insert_1 = False
        if len(sentence1) < len(sentence2):
            insert_1 = True
        insert_str = sentence1 if insert_1 else sentence2
        compare_str = sentence2 if insert_1 else sentence1

        split_insert_str = insert_str.split(" ")
        split_compare_str = compare_str.split(" ")
        # case 1 insert at start
        insert_start = split_insert_str==split_compare_str[-len(split_insert_str):]
        insert_begin = split_insert_str==split_compare_str[:len(split_insert_str)]
        # check if we  can insert in the middle 
        _count = 0
        if len(split_insert_str) == 1:
            return insert_start or insert_begin
        for i, _str in enumerate(split_insert_str):
            if i >= len(split_insert_str):
                break
            if split_compare_str[i] == _str:
                _count+=1
            else:
                break
        split_compare_str = split_compare_str[::-1]
        split_insert_str = split_insert_str[::-1]
        for i,_str in enumerate(split_compare_str):
            if i >= len(split_insert_str):
                break
            if split_insert_str[i] == _str:
                _count+=1
            else:
                break
        insert_middle = _count>=len(split_insert_str)
        return insert_start or insert_begin or insert_middle


solution = Solution()
print(solution.areSentencesSimilar(sentence1 = "B", sentence2 = "ByI BMyQIqce b bARkkMaABi vlR RLHhqjNzCN oXvyK zRXR q ff B yHS OD KkvJA P JdWksnH"))