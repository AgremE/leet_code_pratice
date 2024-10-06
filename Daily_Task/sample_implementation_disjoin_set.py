class DisjoinSet:
    def __init__(self, n) -> None:
        # assuming the i is always start 0
        self.component_size = n
        self.component = [1 for _ in range(n)]
        self.rep = [i for i in range(n)]

    def union(self, x, y):
        x, y = self.find_rep(x), self.find_rep(y)
        if x == y:
            return 0
        elif self.component[x] <= self.component[y]:
            self.rep[x] = y
            self.component[y] += self.component[x]
        else:
            self.rep[y] = x
            self.component[x] += self.component[y]
        self.component_size -= 1

    def find_rep(self, x):
        if self.rep[x] == x:
            return x
        return self.find_rep(self, self.rep[x])

    def is_complete(self):
        return self.component_size == 1
