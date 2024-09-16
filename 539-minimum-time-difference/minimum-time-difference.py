class Solution:
    def convertToMinutes(self, timePoint):
        hour, minute = timePoint.split(":")
        return int(hour) * 60 + int(minute)
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_minutes = sorted(map(self.convertToMinutes, timePoints))

        # Possible that first and last times are actually closest.
        # (i.e. 12:00 AM and 11:59 PM are only one minute apart)
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

        # Case 1: go FORWARD in time from big to small
        # N.B. there are at most 24 hours == 1440 minutes in a day
        case1 = (1440 - big) + small

        # Case 2: go FORWARD in time from small to big
        case2 = big - small

        return min(case1, case2)