class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1: "I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        ans = ""
    
        n = len(str(num))
        num = str(num)
        for i in range(n):
            zero = n - i - 1
            if int(num[i]) == 4 or int(num[i]) == 9:
                value = int(num[i]) + 1
                a, b = value * 10**zero, 10**zero
                ans += dictionary[b] + dictionary[a]
            elif int(num[i]) > 5:
                a, b = 5*10**zero, 10**zero
                ans += dictionary[a]
                for j in range(5, int(num[i])):
                    ans+= dictionary[b]
            elif int(num[i]) == 5:
                a = 5*10**zero
                ans+= dictionary[a] 
            else:
                a = 10**zero
                for j in range(int(num[i])):
                    ans+= dictionary[a] 
        return ans

