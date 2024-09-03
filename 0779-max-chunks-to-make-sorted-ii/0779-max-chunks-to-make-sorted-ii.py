class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        index = [i for i in range(len(arr))]
        index.sort(key=lambda x:arr[x])

        visited1 = {}
        visited2 = {}

        paritions = 0
        for i in range(len(arr)):
            visited1[arr[i]] = visited1.get(arr[i], 0) + 1
            visited2[arr[index[i]]] = visited2.get(arr[index[i]], 0) + 1

            if visited1 == visited2:
                paritions += 1
        return paritions
        