class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # depth = n
        # number branch = 2
        # 2**n + c(n, k) * k
        # def back(index, choosen):
        #     if index == len(nums1):
        #         if len(choosen) == k:
        #             mini = float('inf')
        #             sumi = 0
        #             for i in choosen:
        #                 sumi += nums1[i]
        #                 mini = min(mini, nums2[i])
        #             return sumi*mini

        #         return -float('inf')
            
        #     ans1 = back(index + 1, choosen)
        #     choosen.append(index)
        #     ans2 = back(index + 1, choosen)
        #     choosen.pop()
        #     return max(ans1, ans2)
        # return back(0, [])

        # O(n**2 + n*log(k))
        # #SEcond approach
        # result = 0
        # for mini in nums2: #o(n)
        #     heap = []
        #     for i in range(len(nums1)): O(n), 
        #         if nums2[i] >= mini:
        #             heappush(heap, nums1[i])
        #             if len(heap) > k:
        #                 heappop(heap)
            
        #     if len(heap) == k:
        #         result = max(result, mini*sum(heap))
        n = len(nums1)
        index = [[nums2[i], nums1[i]] for i in range(n)]
        index.sort(reverse=True)

        result, heap = 0, []
        sumi = 0
        for a, b in index:
            heappush(heap, b)
            sumi += b
            if len(heap) > k:
                sumi -= heappop(heap)
            if len(heap) == k:
                result = max(result, a*sumi)
        return result

                
        #

        