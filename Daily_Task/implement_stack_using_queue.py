class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.stack.pop()

    def top(self) -> int:
        elem = self.pop()
        self.push(elem)
        return elem

    def empty(self) -> bool:
        return len(self.stack) == 0
