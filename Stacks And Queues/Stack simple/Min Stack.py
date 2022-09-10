class MinStack:

    # @param x, an integer
    def __init__(self):
        self.stack = []
        self.minimum = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minimum) == 0:
            self.minimum.append(x)
        else:
            if x <= self.minimum[-1]:
                self.minimum.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            if self.stack[-1] == self.minimum[-1]:
                self.minimum.pop()
            self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1

        return self.minimum[-1]
