class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        count, answer = [], []

        for key in counter:
            count.append((-counter[key], key))
        heapify(count)
        while len(count) > 1:
            count1, key1 = heappop(count)
            count2, key2 = heappop(count)

            if answer == [] or answer[-1] != key1:
                answer.append(key1)
                answer.append(key2)
            else:
                answer.append(key2)
                answer.append(key1)
            
            if count1 != -1:
                heappush(count, (count1 + 1, key1))
            
            if count2 != -1:
                heappush(count, (count2 + 1, key2))
        
        if count:
            count1, key = heappop(count)
            answer.append(key)

        return answer




        