class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = sorted(zip(dist, speed), key=lambda x: x[0]/ x[1])
    
        count = 1
        for i in range(1, len(monsters)):
            time = monsters[i][0] / monsters[i][1]
            if time <= count:
                return count
            count += 1
        return count