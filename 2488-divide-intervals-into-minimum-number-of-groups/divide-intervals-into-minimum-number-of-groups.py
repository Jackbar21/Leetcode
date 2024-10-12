class TreeNode:
    def __init__(self, interval):
        self.left = None
        self.right = None
        self.interval = tuple(interval)

class Solution:
    def __init__(self):
        self.bst = None
    
    def getSmallestIntervalWithMinStart(self, root, min_start):
        if not root:
            print("COND1")
            return None

        if self.getLargestInterval(root)[0] < min_start:
            print("COND2")
            print(self.getSmallestInterval(root), min_start)
            return None
        
        return self.getSmallestIntervalWithMinStartHelper(root, min_start)
    
    def getSmallestIntervalWithMinStartHelper(self, root, min_start):
        # if not root:
        #     return None # used for termination case!
        assert root is not None

        if root.interval[0] < min_start:
            return self.getSmallestIntervalWithMinStart(root.right, min_start)
        
        return self.getDirectSmallestIntervalWithMinStart(root, min_start)
    
    def getDirectSmallestIntervalWithMinStart(self, root, min_start):
        assert root is not None
        if root.left and root.left.interval[0] >= min_start:
            return self.getDirectSmallestIntervalWithMinStart(root.left, min_start)
        
        # while root.right and root.right.interval[0] == root.interval[0]:
        #     root = root.right

        return root.interval

    def getSmallestInterval(self, root):
        assert root is not None
        if root.left:
            return self.getSmallestInterval(root.left)
        
        return root.interval
    
    def getLargestInterval(self, root):
        assert root is not None
        if root.right:
            return self.getLargestInterval(root.right)
        
        return root.interval

    # def insert(self, root, interval):
    #     if not root:
    #         return TreeNode(interval)
        
    #     if interval < root.interval:
    #         root.left = self.insert(root.left, interval)
    #     else:
    #         root.right = self.insert(root.right, interval)
        
    #     return root
    
    def delete(self, root, interval):
        assert root is not None

        print("DASA", root.interval, interval)
        if interval < root.interval:
            root.left = self.delete(root.left, interval)
            return root
        
        if interval > root.interval:
            root.right = self.delete(root.right, interval)
            return root
        
        assert interval == root.interval
        if not root.left and not root.right:
            assert root.interval == interval
            return None
        
        if not root.left:
            return root.right
        
        if not root.right:
            return root.left
        
        assert root.left is not None and root.right is not None
        smallest_interval = self.getSmallestInterval(root.right)
        root.interval = smallest_interval
        root.right = self.delete(root.right, smallest_interval)
        return root
    
    def initTree(self, intervals, l, r):
        if l >= r:
            # return root if l > r else self.insert(root, intervals[l])
            return None if l > r else TreeNode(intervals[l])
        
        mid = (l + r) // 2
        root = TreeNode(intervals[mid])
        root.left = self.initTree(intervals, l, mid - 1)
        root.right = self.initTree(intervals, mid + 1, r)
        return root

        

    # Want to find interval with smallest start time, such that
    # the start time >= min_start
    # We can do this via leftmost binary search with condition being
    # interval[START] >= min_start, which will be sorted array of
    # booleans since intervals already sorted by increasing start times!
    # def leftmostBinarySearch(self, intervals, min_start):
    #     # intervals = self.sorted_intervals
    #     l, r = 0, len(intervals) - 1

    #     while l < r:
    #         mid = (l + r) // 2
    #         if intervals[mid][0] < min_start:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
        
    #     return l

    def preorder(self, root):
        if not root:
            return
        
        left = root.left.interval if root.left else "L"
        right = root.right.interval if root.right else "R"
        print(root.interval, left, right)
        self.preorder(root.left)
        self.preorder(root.right)
        return
    
    def minGroupsOld(self, intervals: List[List[int]]) -> int:
        LEFT, RIGHT = 0, 1
        START, END = 0, 1
        # intervals.sort(key = lambda interval: (interval[RIGHT]))
        # intervals.sort(key = lambda interval: (interval[LEFT], interval[RIGHT]))
        intervals.sort()
        print(intervals)

        self.bst = self.initTree(intervals, 0, len(intervals) - 1)
        # self.preorder(self.bst)
        # return 0
        # return 0

        # groups = {
        #     intervals[0]: [intervals[0]]
        # }
        groups = []
        while self.bst != None:
            # Last Node to remove
            if not self.bst.left and not self.bst.right:
                print(groups, self.bst.interval)
                print("RES 1", groups, self.bst.interval)
                return len(groups) + 1

            smallest_interval = self.getSmallestInterval(self.bst)
            self.bst = self.delete(self.bst, smallest_interval)
            min_start = smallest_interval[RIGHT] + 1
            new_group = [smallest_interval]

            next_interval = self.getSmallestIntervalWithMinStart(self.bst, min_start)
            print(f"{smallest_interval=}, {next_interval=}")
            while next_interval != None: # if None, implies none valid left!
                print(next_interval, min_start)
                self.preorder(self.bst)
                assert next_interval[START] >= min_start
                new_group.append(next_interval)
                min_start = max(min_start, next_interval[END] + 1)
                self.bst = self.delete(self.bst, next_interval)

                # Loop Invariant
                next_interval = self.getSmallestIntervalWithMinStart(self.bst, min_start)

            groups.append(new_group)
            continue    



            # # Overlaps with all intervals, so add to group alone and carry on
            # biggest_interval = self.getLargestInterval(self.bst)
            # if biggest_interval[START] < min_start:
            #     groups.append(new_group)
            #     continue
            
            # # Want to find next interval with smallest start time, such that
            # # the start time >= min_start (i.e. smallest_interval's right time + 1).
            # assert self.bst
            # while self.bst.right:
            #     next_interval = self.getSmallestInterval(self.bst.right)
            #     if next_interval[START] >= min_start:
            #         new_group.append(next_interval)
            #         min_start = max(min_start, next_interval[END] + 1)
            #         self.bst.right = self.delete(self.bst.right, next_interval)
            #     else:
            #         break

            # groups.append(new_group)
            # continue      

            # # while self.bst.right and 

            # index = self.leftmostBinarySearch(intervals, min_start)
            # print(index, len(intervals), intervals)
            # while index < len(intervals):
            #     if intervals[index][START] >= min_start:
            #         start, end = intervals.pop(index)
            #         min_start = max(min_start, end + 1)
            #         new_group.append((start, end))
            
            # groups.append(new_group)
            # continue

        print("RES 2")
        return len(groups)    


        # while len(intervals) > 0:
        #     # continue
        #     left, right = intervals.popleft()
        #     # left, right = intervals.pop(0)
        #     new_group = [(left, right)]
        #     min_start = right + 1
        #     # Want to find interval with smallest start time, such that
        #     # the start time >= min_start
        #     # We can do this via leftmost binary search with condition being
        #     # interval[START] >= min_start, which will be sorted array of
        #     # booleans since intervals already sorted by increasing start times!

        #     # overlaps with all intervals, so add to group alone and carry on
        #     if intervals[-1][START] < min_start:
        #         groups.append(new_group)
        #         continue
            
        #     index = self.leftmostBinarySearch(intervals, min_start)
        #     print(index, len(intervals), intervals)
        #     while index < len(intervals):
        #         if intervals[index][START] >= min_start:
        #             start, end = intervals.pop(index)
        #             min_start = max(min_start, end + 1)
        #             new_group.append((start, end))
            
        #     groups.append(new_group)
        #     continue
                

        #     while len(intervals) > 0 and intervals[index][START] >= min_start:
        #         start, end = intervals.pop()
        #         min_start = max(min_start, end)
        #         new_group.append((start, end))

        #     # Idea: go from end of intervals, and keep
        #     # adding valid intervals starting from one
        #     # with earliest 
            
        #     # TODO: change to groups += 1
        #     groups.append(new_group)

        # print(groups)
        # return len(groups)

        # s1, e1
        # s2, e2

        # s1 <= s2

        # conflict if and only if e1 >= s2
    
    def intervalsOverlap(self, interval1, interval2):
        # if big_interval < small_interval:
        #     small_interval, big_interval = big_interval, small_interval
        small_interval, big_interval = sorted([interval1, interval2])
        
        return small_interval[1] >= big_interval[0]

    def rightmostBinarySearch(self, intervals, start):
        # Find rightmost index i such that intervals[i][END] >= start
        START, END = 0, 1
        l, r = 0, len(intervals) - 1
        rightmost_index = -1
        while l < r:
            mid = (l + r) // 2
            if intervals[mid][END] >= start:
                # rightmost_index = max(rightmost_index, mid)
                # l = mid + 1
                r = mid - 1
            else:
                # r = mid - 1
                l = mid + 1
                rightmost_index = max(rightmost_index, mid)


        assert rightmost_index != -1
        # assert r == rightmost_index
        return rightmost_index
    def minGroups(self, intervals: List[List[int]]) -> int:
        START, END = 0, 1
        # freqs = [0] * (max(map(lambda interval: interval[END], intervals)) + 2)
        freqs = {}
        for start, end in intervals:
            freqs[start] = freqs.get(start, 0) + 1
            freqs[end + 1] = freqs.get(end + 1, 0) - 1
        
        res = 0
        cur = 0
        for key in sorted(freqs):
            cur += freqs[key]
            res = max(res, cur)
        return res


        START, END = 0, 1
        intervals = sorted(map(lambda interval: tuple(interval), intervals))
        freqs = {interval: 0 for interval in intervals} 

        for interval in intervals:
            r = self.rightmostBinarySearch(intervals, interval[START])
            freqs[intervals[r]] += 1
        
        print(freqs)
        return 0


        # Idea: For each interval, we're gonna find the 

        # Find rightmost index i such that intervals[i][END] >= start
        # (i.e. actually overlaps)

        for interval in intervals:
            interval = tuple(interval)
            was_added = False
            for intersect in freqs:
                if self.intervalsOverlap(interval, intersect):
                    new_freq = freqs[intersect] + 1
                    del freqs[intersect]
                    new_intersect = (
                        max(intersect[START], interval[START]),
                        min(intersect[END], interval[END])
                    )
                    assert new_intersect not in freqs
                    freqs[new_intersect] = max(freqs.get(new_intersect, 0), new_freq)
                    was_added = True
                    # break
            
            if not was_added:
                freqs[interval] = 1
        
        print(freqs)
        return max(freqs.values(), default=0)




        START, END = 0, 1
        intervals = sorted(map(lambda interval: tuple(interval), intervals))
        interval_to_intersect = {intervals[0]: intervals[0]}
        intersect_to_freq = {intervals[0]: 1}
        print(f"{intervals}")
        # print(interval_to_intersect, intersect_to_freq)

        for i in range(1, len(intervals)):
            prev_interval = intervals[i - 1]
            cur_interval = intervals[i]

            # Sorted by increasing start time (then inc. end time),
            # so overlap if and only if prev_interval[END] >= cur_interval[START]
            if prev_interval[END] >= cur_interval[START]:
                print(f"{i=}, COND1")
                # Overlap, so take current "intersection" that
                # previous interval maps to, and intersect it with
                # new interval. Increase frequency by one, since
                # current interval is added to set of intervals
                # conflicting with it
                cur_intersect = interval_to_intersect[prev_interval]
                new_start = max(cur_intersect[START], cur_interval[START])
                new_end = min(cur_intersect[END], cur_interval[END])
                new_intersect = (new_start, new_end)
                # del interval_to_intersect[prev_interval]

                print(cur_interval, new_intersect, cur_intersect) 
                print(interval_to_intersect, intersect_to_freq)
                interval_to_intersect[cur_interval] = new_intersect
                intersect_to_freq[new_intersect] = intersect_to_freq[cur_intersect] + 1
                print(interval_to_intersect, intersect_to_freq)

            else:
                print(f"{i=}, COND2")
                # since this has largest start time so far, it cannot
                # yet conflict with any seen interval. So add it to its
                # own group.
                interval_to_intersect = {cur_interval: cur_interval}
                intersect_to_freq = {cur_interval: 1}

        print(interval_to_intersect)
        print(intersect_to_freq)
        return max(intersect_to_freq.values())

        for (start, end) in intervals:
            # for i in range(start, end + 1):
            #     freqs[i] = freqs.get(i, 0) + 1
            freqs[start] = freqs.get(start, 0) + 1
            freqs[end + 1] = freqs.get(end + 1, 0) - 1
            # freqs[start] = freqs.get(start, 0) + 1
            # freqs[end] = freqs.get(end, 0) + 1
            # max_freq = max(max_freq, freqs[start], freqs[end])
        
        # print(freqs.values())
        # return max_freq
        return max(freqs.values())
