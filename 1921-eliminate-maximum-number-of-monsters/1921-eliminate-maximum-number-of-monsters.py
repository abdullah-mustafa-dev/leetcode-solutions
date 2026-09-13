class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = [(d + s - 1) // s for d, s in zip(dist, speed)]
        arrival.sort()

        for i, t in enumerate(arrival):
            if t <= i:
                return i

        return len(arrival)