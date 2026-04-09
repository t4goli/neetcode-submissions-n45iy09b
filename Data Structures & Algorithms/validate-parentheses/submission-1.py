class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0:
            return True
        for i, val in enumerate(s):
            if val == '[' or val == '{' or val == '(':
                stack.append(val)
                continue
            if not stack:
                return False
            if val == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if val == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if val == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False