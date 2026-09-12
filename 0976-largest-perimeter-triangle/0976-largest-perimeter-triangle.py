class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxArea = 0

        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2] and nums[i] + nums[i + 1] + nums[i + 2] > maxArea:
                maxArea = nums[i] + nums[i + 1] + nums[i + 2]

        return maxArea