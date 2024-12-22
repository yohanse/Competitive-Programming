class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        index = [i for i in range(len(queries))]
        index.sort(key=lambda x: max(queries[x]))
        
        def binarysearch(stack, target):
            if heights[stack[0]] <= target:
                return -1
                
            l, r = 0, len(stack) - 1
            while l < r:
                m = (l + r + 1) // 2
                if heights[stack[m]] > target:
                    l = m
                else:
                    r = m - 1
            return stack[l]

        heights_index, queries_index = len(heights) - 1, len(queries) - 1
        answer = [-1 for i in range(len(queries))]
        stack = []
        for heights_index in range(len(heights) - 1, -1, -1):
            
            while stack and heights[heights_index] >= heights[stack[-1]]:
                stack.pop()
            stack.append(heights_index)

            while queries_index > -1 and heights_index == max(queries[index[queries_index]]):
                if queries[index[queries_index]][0] == queries[index[queries_index]][1] or heights[max(queries[index[queries_index]])] > heights[min(queries[index[queries_index]])]:
                    answer[index[queries_index]] = heights_index
                else:
                    answer[index[queries_index]] = binarysearch(stack, max(heights[queries[index[queries_index]][0]], heights[queries[index[queries_index]][1]]))
                queries_index -= 1
        
        return answer        