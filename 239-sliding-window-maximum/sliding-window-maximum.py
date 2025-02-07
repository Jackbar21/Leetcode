class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = {}
        max_heap = [] # use negative numbers to simulate max heap via min heap!
        for i in range(k):
            num = nums[i]
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                max_heap.append(-num)

        heapq.heapify(max_heap)
        res = [-max_heap[0]]

        l = 0
        for r in range(k, len(nums)):
            # Add num at index r, and remove num at index l!
            l_num, r_num = nums[l], nums[r]
            if l_num == r_num:
                l += 1
                res.append(-max_heap[0])
                continue

            # Add nums[r]
            if r_num in d:
                d[r_num] += 1
            else:
                d[r_num] = 1
                heapq.heappush(max_heap, -r_num)
            
            # Delete nums[l]
            # assert l_num in d
            d[l_num] -= 1
            if d[l_num] == 0:
                del d[l_num]
            l += 1

            # Append new window max into res
            while -max_heap[0] not in d:
                heapq.heappop(max_heap)
            res.append(-max_heap[0])
        
        return res
