class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        final = 2**4 - 1
        
        def backtrack(bit_mask, permutation):
            if bit_mask == final:
                permutation.append(permutation[0])

                slope = [0 for i in range(4)]
                distance = [0 for i in range(4)]

                for i in range(4):
                    x1, y1 = permutation[i]
                    x2, y2 = permutation[i + 1]

                    distance[i] = (x1 - x2) ** 2 + (y1 - y2) ** 2

                    if x1 - x2 == 0 and y1 - y2 == 0:
                        slope[i] = "E"
                    elif x1 - x2 == 0:
                        slope[i] = "V"
                    elif y1 - y2 == 0:
                        slope[i] = "H"
                    else:
                        slope[i] = ((y1 - y2), (x1 - x2))
                
                if len((set(distance))) != 1:
                    return False
                
                for i in "EVH":
                    if i in slope:
                        if (slope[0], slope[1]) == ("H", "V") or (slope[1], slope[0]) == ("H", "V"):
                            return True
                        else:
                            return False
                
                if slope[0][0] * slope[1][0] == -slope[1][1] * slope[0][1]:
                    return True
                
                return False
            res = False
            for i in range(4):
                num = 1 << i
                if num & bit_mask == 0:
                    res = res or backtrack(bit_mask | num, permutation + [points[i]])
            return res
        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
        if len(set(points)) != 4:
            return False
        return backtrack(0, [])
        

                
                    
                
        