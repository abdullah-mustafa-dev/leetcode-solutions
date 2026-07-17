class Solution(object):
    def permute(self, nums):
        ans = []
        def helper(path=[], seen=set()):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for n in nums:
                if n not in seen:
                    path.append(n)
                    seen.add(n)
                    helper(path, seen)
                    path.pop()
                    seen.remove(n)
        helper()
        return ans
        