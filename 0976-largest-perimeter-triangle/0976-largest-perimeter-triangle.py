class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxArea = 0

        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a + b > c and a + b + c > maxArea:
                maxArea = a + b + c

        return maxArea