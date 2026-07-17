class Solution(object):
    def isValid(self, s):
        dct = {')': '(', ']': '[', '}': '{'}
        stk = []
        
        for char in s:
            if char not in dct:     # open
                stk.append(char)
            # empty or NO match
            elif not stk or dct[char] != stk.pop():
                return False

        return not stk  # MUST be empty

        