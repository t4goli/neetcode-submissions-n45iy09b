class MinStack:

    def __init__(self):
        self.stack = []
        self.minis = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minis) == 0:
            self.minis.append(val)
        else:
            self.minis.append(min(self.minis[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minis.pop()



    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minis[-1]

