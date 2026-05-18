class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opers = "+-*/"
        for token in tokens:
            if token not in opers:
                stack.append(token)
            elif token=="+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(a+b))
            elif token=="-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(b-a))
            elif token=="*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(a*b))
            elif token=="/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
        return int(stack[-1])
