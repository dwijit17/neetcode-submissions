class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
                print(stack)
            else:
                if len(stack)>0 and stack[-1]==brackets[char]:
                    stack.pop()
                else:
                    return False         
        return True if len(stack)==0 else False

        