class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Idea: If a row or column has 0 or 1 total servers, there are exactly 0 communicating
        # servers on that row or column. However, if there are n >= 2 servers on a row/column,
        # then each server communicates with the other n-1 servers, for a total of "n communicating
        # servers" on that row/column. Hence, for each row and each column, we want to increment the
        # total number of communicating servers by:
        #   (a) 0, if number of servers is N, where N <= 1
        #   (b) N, if number of servers is N, where N >= 2
        SERVER, EMPTY = 1, 0
        M, N = len(grid), len(grid[0])
        rows = [set() for _ in range(M)]
        cols = [set() for _ in range(N)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == SERVER:
                    rows[i].add((i, j))
                    cols[j].add((i, j))
        
        communicating_servers = set()
        for servers in rows:
            if len(servers) >= 2:
                for server in servers:
                    communicating_servers.add(server)

        for servers in cols:
            if len(servers) >= 2:
                for server in servers:
                    communicating_servers.add(server)

        return len(communicating_servers)
