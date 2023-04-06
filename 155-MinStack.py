class MinStack:

    def __init__(self):
        self.stack = []
        self.topStack = -1
        self.minStack = []
        self.minTop = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topStack += 1
        if self.minTop == -1 or val <= self.minStack[-1]:
            self.minStack.append(val)
            self.minTop += 1

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop(-1)
            self.minTop -= 1
        self.stack.pop(self.topStack)
        self.topStack -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
