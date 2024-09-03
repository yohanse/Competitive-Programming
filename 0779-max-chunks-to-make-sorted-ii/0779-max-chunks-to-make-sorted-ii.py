class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        length = len(arr)

        index = [i for i in range(len(arr))]
        index.sort(key=lambda x:arr[x])

        visited = {}
        paritions = pointer = 0

        for sort_pointer in range(length):
            visited[arr[index[sort_pointer]]] = visited.get(arr[index[sort_pointer]], 0) + 1
            while pointer < length and visited.get(arr[pointer], 0):
                visited[arr[pointer]] -= 1
                pointer += 1
           
            paritions += (sort_pointer + 1 == pointer)
        return paritions
        