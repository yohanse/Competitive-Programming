class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        

        friend_zone = set()
        
        for friend1, friend2 in friendships:
            common = [0 for i in range(n)]

            can_communicate = False
            for language in languages[friend1 - 1]:
                common[language - 1] = 1
            
            for language in languages[friend2 - 1]:
                if common[language - 1]:
                    can_communicate = True
            
            if not can_communicate:
                friend_zone.add(friend1 - 1)
                friend_zone.add(friend2 - 1)

        common = [0 for i in range(n)]
        for friend in friend_zone:
            for language in languages[friend]:
                common[language - 1] += 1
        
        return len(friend_zone) - max(common)
            
        
        