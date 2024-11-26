class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        team_to_indegree = {team: 0 for team in range(n)}

        for _, v in edges:
            team_to_indegree[v] += 1
        
        best_team = None
        best_indegree = float("inf")
        for team, indegree in team_to_indegree.items():
            if indegree == 0 and best_indegree == 0:
                # Two teams are both undefeatable, hence
                # no unique champion and return -1
                return -1
    
            if best_indegree > indegree:
                best_indegree = indegree
                best_team = team
        
        return best_team if best_indegree == 0 else -1
