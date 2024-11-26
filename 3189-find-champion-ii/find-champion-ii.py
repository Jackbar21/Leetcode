class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        team_to_indegree = {team: 0 for team in range(n)}

        for _, v in edges:
            team_to_indegree[v] += 1
        
        best_team = n
        for team, indegree in team_to_indegree.items():
            if indegree != 0:
                continue
            
            if best_team < n:
                # Two teams are both undefeatable, hence
                # no unique champion, so return -1
                return -1
            
            best_team = team
    
        return best_team if best_team < n else -1
