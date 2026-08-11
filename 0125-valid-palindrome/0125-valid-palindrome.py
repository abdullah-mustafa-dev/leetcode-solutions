class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() == s[p2].lower():
                    p1 += 1
                    p2 -= 1
                    continue
                return False
            if not s[p1].isalnum():
                p1 += 1
            if not s[p2].isalnum():
                p2 -= 1
        return True