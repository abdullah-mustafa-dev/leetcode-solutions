class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        return answer