class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def good_functions(mid):
            count = 0
            for rank in ranks:
                count += int((mid / rank)**0.5)
            return count >= cars

        left, right = 0, cars*cars*min(ranks)
        while left < right:
            mid = (left + right) // 2
            if good_functions(mid):
                right = mid
            else:
                left = mid + 1
        return left