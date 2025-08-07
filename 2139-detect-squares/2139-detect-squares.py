class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] = 1 + self.points.get((x, y), 0)

    def count(self, point: List[int]) -> int:
        x, y = point
        number_of_square = 0
        for x1, y1 in self.points.keys():
            if x1 != x and abs(x1 - x) == abs(y1 - y):
                
                point1 = (x1, y)
                point2 = (x, y1)
                point3 = (x1, y1)

                number_of_square += self.points.get(point1, 0)*self.points.get(point2, 0)*self.points.get(point3, 0)
        
        return number_of_square