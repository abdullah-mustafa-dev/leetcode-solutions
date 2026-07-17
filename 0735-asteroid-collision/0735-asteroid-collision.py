class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for n in asteroids:
            con = True
            while stack and n < 0 and stack[-1] > 0:
                if abs(n) > stack[-1]:
                    stack.pop()
                else:
                    if abs(n) == stack[-1]:
                        stack.pop()
                    con = False
                    break

            if con:
                stack.append(n)
                
        return stack
        