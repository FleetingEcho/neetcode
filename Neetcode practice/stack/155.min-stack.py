class MinStack:
    def __init__(self):
        self.data = []
        self.minArr = [] #降序

    def push(self, newNum):
        if not self.minArr or newNum <= self.getMin():
            self.minArr.append(newNum)
        self.data.append(newNum)

    def pop(self):
        if not self.data:
            return
        value = self.data.pop()
        if value == self.getMin():
            self.minArr.pop()

    def top(self):
        return self.data[-1] if self.data else None

    def getMin(self):
        # minArr[-1] is the smallest number
        return self.minArr[-1] if self.minArr else None
