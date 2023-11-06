from heapq import heapify, heapreplace, heappop, heappush


class LFUCache:
    def __init__(self, capacity: int):
        self.heap = []
        self.count_dict = {}
        heapify(self.heap)
        self.input_dict = {}
        self.cache_count = 0
        self.capacity = capacity

    def updated_count(self, key, _old_count):
        new_count = self.get_id_heap(key, _old_count + 1)
        heappush(self.heap, (new_count, key))

    def get_id_heap(self, _key, _count):
        id = (10**6 + _count) * (10**5) + _key
        return id

    def get(self, key: int) -> int:
        if key in self.input_dict:
            self.count_dict[key] = self.count_dict[key] + 1
            self.updated_count(key, self.count_dict[key])
            return self.input_dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.input_dict:
            self.input_dict[key] = value
            self.updated_count(key, self.count_dict[key])
            self.cache_count = self.cache_count + 1
        else:
            ### checking the capacity of cache
            if self.cache_count >= self.capacity:
                ## Remove the cache until the key is hit in the list of input_dictionary
                while self.heap:
                    _id, key = heappop(self.heap)
                    if key in self.input_dict:
                        del self.input_dict[key]
                        del self.count_dict[key]
                        break
                _id = self.get_id_heap(key, 1)
                heappush(self.heap, (_id, key))
            else:
                self.input_dict[key] = value
                self.count_dict[key] = 1
                self.cache_count = self.cache_count + 1
                _id = self.get_id_heap(key, 1)
                heappush(self.heap, (_id, key))


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
_instruction = [
    "LFUCache",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "get",
    "get",
    "get",
]
_input = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
bj = None
for i in range(len(_instruction)):
    instruc = _instruction[i]
    _in = _input[i]
    if instruc == "LFUCache":
        bj = LFUCache(_in[0])
    elif instruc == "put":
        key, value = _in
        bj.put(key, value)
    elif instruc == "get":
        print(bj.get(_in[0]))

    if instruc != "get":
        print("None")
