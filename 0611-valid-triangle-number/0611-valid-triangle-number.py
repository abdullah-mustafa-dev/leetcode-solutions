class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        ans = 0

        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                target = nums[i] + nums[j]
                idx = len(nums)
                left, right = j + 1, len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2

                    if nums[mid] >= target:
                        right = mid - 1
                        idx = mid
                    else:
                        left = mid + 1
                ans += (idx - j - 1)
        return ans