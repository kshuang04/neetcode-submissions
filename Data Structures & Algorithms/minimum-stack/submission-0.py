class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = float("inf")
        for item in self.stack:
            if item < min:
                min = item
        return min
