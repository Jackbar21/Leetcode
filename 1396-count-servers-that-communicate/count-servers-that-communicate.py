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
                    rows[i].add(j)
                    cols[j].add(i)
        
        communicating_servers = set()
        for i in range(M):
            server_col_indices = rows[i]
            if len(server_col_indices) >= 2:
                for server_col_index in server_col_indices:
                    communicating_servers.add((i, server_col_index))

        for j in range(N):
            server_row_indices = cols[j]
            if len(server_row_indices) >= 2:
                for server_row_index in server_row_indices:
                    communicating_servers.add((server_row_index, j))

        return len(communicating_servers)
