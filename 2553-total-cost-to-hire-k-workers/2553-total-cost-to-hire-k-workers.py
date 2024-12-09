class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = []
        used = set()
        ans = 0

        for i in range(candidates):
            if i not in used:
                heappush(heap, (costs[i], i))
                used.add(i)

            if n - i - 1 not in used:
                heappush(heap, (costs[n - i - 1], n - i - 1))
                used.add(n - i - 1)

        front_limit = candidates
        back_limit = n - candidates - 1

        for i in range(k):
            cost, index = heappop(heap)
            if index < front_limit:
                while front_limit in used:
                    front_limit += 1
                if front_limit < n:
                    heappush(heap, (costs[front_limit], front_limit))
                    used.add(front_limit)
                    front_limit += 1
            else:
                while back_limit in used:
                    back_limit -= 1
                if back_limit > -1:
                    heappush(heap, (costs[back_limit], back_limit))
                    used.add(back_limit)
                    back_limit -= 1
            ans += cost
        return ans
