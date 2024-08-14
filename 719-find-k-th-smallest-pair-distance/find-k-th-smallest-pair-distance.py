# HINT: Binary search for the answer. 
#       How can you check how many pairs have distance <= X?
class Solution:
    def _count_pairs_with_max_distance(self, nums, max_distance):
        return self.countNumPairsGreaterThanX(max_distance)
    def __init__(self):
        self.num_pairs = -1
        self.nums = None # sorted
    def countNumPairsGreaterThanX(self, X):
        nums = self.nums
        n = len(nums)
        # l, r = 0, len(self.nums) - 1
        count = 0
        l = 0
        # mid = n - 1
        # while nums[mid] - nums[0] != X:
        #     mid -= 1
        
        # assert 0 <= mid < n

        # [6, 15, 35, 36, 38, 39, 52, 62, 70, 78, 87, 89, 99, 100, 99999]
        for r in range(n):
            count += l
            while nums[r] - nums[l] > X:
                count += 1
                l += 1

        return count

        r = n - 1
        l = r - 1

        while l > 0 and nums[r] - nums[l] > X:
            l -= 1
        
        # 62 - 6 == 56
        # [6, 15, 35, 36, 38, 39, 52, 62, 70, 78, 87, 89, 99, 100, 99999]

        while r > 0 and nums[r] - nums[l] > X:
            assert l == 0
            r -= 1
        

        
        

        # for r in range(len):
        # while l < r:

        #     if nums[r] - nums[l] > X:
        #         return count
            

    def countNumPairsLessThanOrEqualToX(self, X):
        return self.num_pairs - self.countNumPairsGreaterThanX(X)
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        self.nums = nums
        self.num_pairs = n * (n - 1) // 2
        # pairs = [nums[j] - nums[i] for i in range(n) for j in range(i + 1, n)]
        # print(pairs)
        # return pairs[k - 1]

        # nums = [6, 89, 39, 36, 35, 99, 70, 15, 62, 38, 100, 78, 87, 52]
        # sorted_nums = [6, 15, 35, 36, 38, 39, 52, 62, 70, 78, 87, 89, 99, 100, 99999]

        l, r = 0, nums[-1] - nums[0]

        while l < r:
            mid = (l + r) // 2

            # COUNT nums[r] - nums[mid] <= k
            # OR    nums[mid] - nums[l]

            count = self.countNumPairsLessThanOrEqualToX(mid)

            # if count == k:
            #     return mid
            if count >= k:
                r = mid
            else:
                # assert count > k
                l = mid + 1
        
        return l

        # <= 62 - 6 == k, 62 - 6 is result
        # elif #(<= 62 - 6) < k, then search 6..62
        # else #(<= 62 - 6) > k, search 62..99999

        biggest = []

        l, r = 0, n - 1
        # biggest.append(nums[r] - nums[l])

        while l < r and len(biggest) < num_pairs - k + 1:
            assert nums[r] - nums[l] >= 0
            biggest.append(nums[r] - nums[l])
            # if len(biggest) >= num_pairs - k + 1:
            #     assert len(biggest) == num_pairs - k + 1
            #     return biggest[-1]

            # Update l or r depending on which one retains largest difference
            case1 = nums[r - 1] - nums[l]
            case2 = nums[l + 1] - nums[r]

            if case1 > case2:
                # Decrement right by 1, but left now restarts from beginning!
                r -= 1
                l = 0
            else:
                l += 1
        
        print(biggest)
        return biggest[-1]



        # biggest diff = 99999 - 6
        # 2nd biggest diff = 99999 - 15, 100 - 6

        # k'th smallest, so pop O(n^2 - k) = O(n^2) elements
















        # n = len(nums)
        # pairs = [] # O(n^2) space

        # # O(n^2)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         pairs.append(abs(nums[i] - nums[j]))
        
        # heapq.heapify(pairs) # O(n^2)

        # for i in range(k - 1):
        #     heapq.heappop(pairs)
        
        # return pairs[0]
