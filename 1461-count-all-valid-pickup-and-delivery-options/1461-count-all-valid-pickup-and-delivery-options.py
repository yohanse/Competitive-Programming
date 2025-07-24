class Solution:
    def countOrders(self, n: int) -> int:
        # Let me start with the brute force we generate all possible permutation and we can check which one is valid and count it the time complexity would be (n + n)! to find the premutation and we have to check for that it will be O(n + n) so the total will be O((n + n)*(n + n)!) but we can mimize this by pruning techinques since one of the order is invalid we don't have to continue this will lead us with great improvment but It is difficult for me  to guess the time complexity and we can keep the space complexity to under O(n + n) recusrion call

        # let me go with the optimal solution could you give me a minute to think about it

        # let think in this way how many delivery I can put now?

        # lets simulate with in example n = 2 which means for places


        #   2
        #  ___, ___, ___, ___,

        # for the first place we can't put anything rather than pickup, right?
        # right because if we put delivery certainly i will be before the pickup
        # so how many pickup we can put we can put either of them so will have to choice so we will put 2 and conitnue to the second one
        # for the second one we will have to choice either delivery either a pickup
        # which one should we add it does not matter since we are going to check for bothe no worry so we will add 1 pickup because we are remaining 1 or 1 delivery
        # You might seem amazed why would you use one delivery since we had 2, that is the question I will expect and it is brillent question
        # the answer depends on the how many pickup and delievery  we have put before 
        # what I mean is on the first row we cna choose form the two but we are going to put only one which means there has to be 1 one deliver if we choose p1 at first so the delivery has d1 and p2 -- d2

        # I think you got the idea I can coded it in few minutes

        # lets analyze the time and space complexity 
        # I am just goging to write it recursively because that is easy if I have time I will make it iterive
        # the number of branch = 2 at max becuase we wull choose either p or d
        # the number of parameters is 2 to handle the number p we are remainig and the number delivery avaliables
        # the depth of the recursion is going to be n + n because we have to choose everything that is possibel

        # based on the above information to find out the time complexity
        # number of branches power of (depth) and times with the cost of function
        # in our case 2**(n + n)*1
        # you might think that is won't pass and it won't
        # but the recusrion is going to be reptetive so me can add memorization and we can cut the time complexity
        # lets analyz the new time complexity
        # in order to find dp problems time complexity just find out how many unique problems we have and multiple it by the ocst of function
        # the problem means state how many arrangment of state we have 
        # so p might up n and d might be up to n so the unique combnination will be n*n = n**2
        # so by memorizing it we can from 2**(n + n) to n**2 with cost of adding n**2 space to mimiorizr all the problems
        # let me wirte the code, if you don't have nay quesiotn

        memo = {}
        modulo = 10**9 + 7

        def recursion(p, d):
            if p == d == 0:
                return 1

            if (p, d) in memo:
                return memo[(p, d)]
            
            memo[(p, d)] = 0

            if d != 0:
                memo[(p, d)] += d*recursion(p, d - 1)
            
            if p != 0:
                memo[(p, d)] += p*recursion(p - 1, d + 1)
            
            return memo[(p, d)] % modulo
        
        return recursion(n, 0)
            