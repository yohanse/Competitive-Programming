class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        num = str(num)[::-1]
        number = {"1" : "One", "2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five", "6": "Six", "7": "Seven", "8":"Eight", "9":"Nine" }
        count = {0:"", 1:"Thousand", 2:"Million", 3:"Billion"}
        one = { "10": "Ten", "11" : "Eleven", "12" : "Twelve", "13" : "Thirteen", "14" : "Fourteen", "15" : "Fifteen", "16" : "Sixteen", "17" : "Seventeen", "18" : "Eighteen", "19" : "Nineteen"}
        two = {"1" : "", "2": "Twenty", "3":"Thirty", "4":"Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9": "Ninety" }
        c = 0
        ans = ""
        for i in range(0, len(num), 3):
            temp = ""
            for j in range(i, min(i + 3, len(num))):
                
                if j - c * 3 == 0 and num[j] != "0":
                    temp += number[num[j]]
                elif j - c * 3 == 1 and num[j] != "0":
                    temp = two[num[j]] + " " + temp
                    if num[j] == "1":
                        key = num[j] + num[j - 1]
                        temp = one[key]
                elif j - c * 3 == 2 and num[j] != "0":
                    temp = number[num[j]] + " Hundred " + temp

            if temp != "":
                temp += " " + count[c]
            c += 1
            ans = " " + temp + ans

        ans = ans.strip()
        ans = ans.split()
        return " ".join(ans)
        

                    
                    

                


        