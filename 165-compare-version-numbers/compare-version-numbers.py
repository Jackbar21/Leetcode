class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        N, M = len(v1_list), len(v2_list)

        for i in range(min(N, M)):
            v1 = int(v1_list[i])
            v2 = int(v2_list[i])

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        if N > M:
            for i in range(M, N):
                if int(v1_list[i]) > 0:
                    return 1
        elif N < M:
            for i in range(N, M):
                if int(v2_list[i]) > 0:
                    return -1
        
        return 0

