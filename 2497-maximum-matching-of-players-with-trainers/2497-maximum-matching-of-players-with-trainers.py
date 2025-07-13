class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        players_index = 0
        ans = 0
        for i in range(len(trainers)):
            while players_index < len(players) and players[players_index] > trainers[i]:
                players_index += 1
            
            if  players_index == len(players):
                break

            ans += 1
            players_index += 1

        return ans
