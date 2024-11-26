class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = {node: 0 for node in range(n)}

        for _, v in edges:
            indegrees[v] += 1
        
        best_team = None
        best_val = float("inf")
        for team, val in indegrees.items():
            if val == 0 and best_val == 0:
                # Two teams are both undefeatable, hence
                # no unique champion and return -1
                return -1
    
            if best_val > val:
                best_val = val
                best_team = team
        
        return best_team if best_val == 0 else -1