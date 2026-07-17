class Solution(object):
    def scoreOfParentheses(self, s):
        stk = [0]
        for c in s:
            if c == '(':
                stk.append(0)
            else:
                value = max(2 * stk.pop(), 1)
                stk[-1] += value
        return stk.pop()
        