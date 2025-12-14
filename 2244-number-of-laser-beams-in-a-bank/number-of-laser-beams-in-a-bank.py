class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        M, N = len(bank), len(bank[0])
        EMPTY, DEVICE = '0', '1'

        devices = {row: [] for row in range(M)}
        for i in range(M):
            for j in range(N):
                if bank[i][j] == DEVICE:
                    devices[i].append(j)
        
        res = 0
        for r1 in range(M):
            len_r1 = len(devices[r1])
            if len_r1 == 0:
                continue

            for r2 in range(r1 + 1, M):
                len_r2 = len(devices[r2])
                if len_r2 == 0:
                    continue
                
                if not all(len(devices[row]) == 0 for row in range(r1 + 1, r2)):
                    continue
                
                # Every device in r1 and r2 have a laser to one another
                res += len_r1 * len_r2

        return res
