class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        searchNums = set(nums)
        longest = 0

        for n in searchNums:
            if n - 1 not in searchNums:
                length = 0
                while n + length in searchNums:
                    length += 1
                longest = max(longest, length)

        return longest