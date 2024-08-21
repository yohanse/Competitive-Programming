class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        N = len(s)
        end = 0

        def convert(char):
            return ord(char) - 96
        
        def append(Hash, char):
            return (Hash*power + convert(char)) % modulo
        
        def popleft(Hash, char):
            return (Hash - (convert(char) * (pow(power, k, modulo)))) % modulo
        
        window_hash = 0
        for i in range(k):
            window_hash = append(window_hash, s[i])
            
        if window_hash == hashValue:
            end = 0
            
        for i in range(k, N):
            window_hash = append(window_hash, s[i])
            window_hash = popleft(window_hash, s[i - k])
            
            if window_hash == hashValue:
                end = i - k + 1
        
        return s[end:end+k][::-1]