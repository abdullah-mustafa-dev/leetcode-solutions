class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        # find the Minimum Absolute Difference
        minDif = None
        for i in range(1, len(arr)):
            dif = arr[i] - arr[i - 1]
            if not minDif or dif < minDif:
                minDif = dif

        ans = []
        for i in range(1, len(arr)):
            dif = arr[i] - arr[i - 1]
            if dif == minDif:
                ans.append([arr[i-1], arr[i]])

        return ans