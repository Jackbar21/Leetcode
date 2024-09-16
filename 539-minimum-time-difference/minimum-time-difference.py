class Solution:
    def convertToMinutes(self, timePoint):
        hour, minute = timePoint.split(":")
        return int(hour) * 60 + int(minute)
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_minutes = sorted(map(self.convertToMinutes, timePoints))
        #print(sorted_minutes)
        # res = float("inf")
        res = self.getDifference(sorted_minutes[0], sorted_minutes[-1])
        for i in range(1, len(sorted_minutes)):
            time1, time2 = sorted_minutes[i - 1], sorted_minutes[i]
            diff = self.getDifference(time1, time2)
            res = min(res, diff)
            # 0 is the best possible value we can ever get, so if we get it,
            # simply return early to save on computation :) Worst case is still O(n)
            if res == 0:
                return res
        
        return res
    
    def getDifference(self, time1, time2):
        # time1 and time2 are both given as time in minutes
        # It is possible that their difference in time is either
        # their literal (absolute-value) difference, OR when looping
        # back through midnight.
        big, small = max(time1, time2), min(time1, time2)
        #print(big, small)

        # Case 1: go FORWARD in time from big to small
        # (0 if big == 0 else 24 * 60 - big)
        case1 = (24 * 60 - big) + small

        # Case 2: go FORWARD in time from small to big
        case2 = big - small

        return min(case1, case2)


        # case1 = abs(time1 - time2)
        # case2 = abs(time1 - time2 + 24 * 60)

        # Case1: go FORWARD in time from time1 to time2
        #        <==> BACKWARD in time from time2 to time1

        # Case2: go BACKWARD in time from time1 to time2
        #       <==> FORWARD in time from time2 to time1


        # #print(case1, case2)
        return min(case1, case2)