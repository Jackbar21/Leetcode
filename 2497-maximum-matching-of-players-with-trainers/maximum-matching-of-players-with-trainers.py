class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        N, M = len(players), len(trainers)
        players.sort()
        trainers.sort()

        res = index = 0
        for player in players:
            while index < M and trainers[index] < player:
                index += 1
            
            # No more trainers left!
            if index >= M:
                assert index == M
                break 
            
            # trainers[index] can train next weakest player, and is weakest remaining
            # trainer. Hence, assign these as such, and continue the problem!
            res += 1
            index += 1

        return res
