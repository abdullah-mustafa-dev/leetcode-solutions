class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = list(range(len(position)))
        indices.sort(key=lambda i: position[i], reverse=True)

        fleets = 0
        last_time = 0
        for i in indices:
            fleet = (target - position[i]) / speed[i]

            if fleet <= last_time:
                continue

            last_time = fleet
            fleets += 1
            
        return fleets