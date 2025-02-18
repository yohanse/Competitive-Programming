class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        
        ans = 0
        for i in range(n):
            freq = {}
            for j in range(n):
                dis = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                freq[dis] = freq.get(dis, 0) + 1
            
            for key in freq:
                ans += freq[key]*(freq[key] - 1)
        return ans