class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        mxSofar = float("-inf")
        mnSofar = float("inf")
        right = -1
        left = -1

        for i in range(len(nums)):
            mxSofar = max(mxSofar, nums[i])
            if mxSofar > nums[i]:
                right = i
        
        for i in range(len(nums) - 1, -1, -1):
            mnSofar = min(mnSofar, nums[i])
            if mnSofar < nums[i]:
                left = i

        if right == -1:
            return 0
        return right - left + 1