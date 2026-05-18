class MinStack:

    def __init__(self):
        self.stack = []
        self.currmin = float('inf')
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currmin = min(self.currmin,val)
        self.minstack.append(self.currmin)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
            self.currmin = self.minstack[-1] if self.minstack else float('inf')
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]


