class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freqArr = [0] * 100001
        for j in range(len(nums)):
            freqArr[nums[j]+50000] += 1

        idx = 0
        for i in range(100001):
            for _ in range(freqArr[i]):
                nums[idx] = i - 50000
                idx += 1
        return nums