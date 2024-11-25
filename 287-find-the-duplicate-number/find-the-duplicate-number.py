class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = 0, 0
        tortoise, hare = nums[tortoise], nums[nums[hare]]
        while tortoise != hare:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
        
        turtle = 0
        while turtle != tortoise:
            turtle, tortoise = nums[turtle], nums[tortoise]
        
        return turtle
















# class Solution:
#     def getNext(self, nums, index):
#         return nums[index]
#     def findDuplicate(self, nums: List[int]) -> int:
#         # # [4,1,2,3]

#         order = []
#         tortoise = 0
#         for _ in range(len(nums)):
#             tortoise = nums[tortoise]
#             order.append(tortoise)
        
#         print(f"{order=}")

#         # tortoise, hare = 0, 0
#         # tortoise, hare = nums[tortoise], nums[nums[hare]]
#         # while tortoise != hare:
#         #     tortoise, hare = nums[tortoise], nums[nums[hare]]
        
#         # pos = hare
        
#         # # tortoise = 0
#         # # new_count = 0
#         # # while tortoise != hare:
#         # #     tortoise, hare = nums[tortoise], nums[nums[hare]]
#         # #     new_count += 1
        
#         # # print(f"{tortoise=}")
#         # # print(f"{hare=}")
#         # # print(f"{new_count=}")
#         # # return 0
#         # # Guarantee that tortoise and hare are in CYCLE TERRITORY
#         # tortoise, hare = 0, 0
#         # for _ in range((len(nums) + 5) * 2):
#         #     tortoise = nums[tortoise]
#         #     hare = nums[nums[hare]]
        
#         # # Find how LARGE this cycle truly is!
#         # hare = nums[tortoise]
#         # len_cycle = 1
#         # while tortoise != hare:
#         #     tortoise = nums[tortoise]
#         #     hare = nums[nums[hare]]
#         #     len_cycle += 1
        
#         # tortoise, hare = 0, pos
#         # for _ in range(len_cycle):
#         #     tortoise, hare = nums[tortoise], nums[nums[hare]]

#         # new_count = 0
#         # while tortoise != hare:
#         #     tortoise, hare = nums[tortoise], nums[nums[hare]]
#         #     new_count += 1
#         # print(f"{tortoise=}")
#         # print(f"{hare=}")
#         # print(f"{new_count=}")
#         # return 0
        
#         # # Find how LONG it takes for tortoise and hare to collide
#         # tortoise, hare = 0, 0
#         # tortoise, hare = nums[tortoise], nums[nums[hare]]
#         # count = 1
#         # while tortoise != hare:
#         #     tortoise = nums[tortoise]
#         #     hare = nums[nums[hare]]
#         #     count += 1
#         # tortoise = nums[tortoise]
#         # hare = nums[nums[hare]]
#         # double_count = count + 1
#         # while tortoise != hare:
#         #     tortoise = nums[tortoise]
#         #     hare = nums[nums[hare]]
#         #     double_count += 1
        
#         # # index = count - len_cycle + 1
#         # print(f"{len_cycle=}, {count=}, {double_count=}, {len(nums)=}")
#         # tortoise = 0
#         # for _ in range(len(nums) - len_cycle - 1):
#         #     tortoise = nums[tortoise]
#         # return tortoise

#         # # Cycle encapsulates a total of (len_cycle + 1) numbers used.
#         # # There are len(nums) numbers in total. So in intial chain,
#         # # There must be len(nums) - (len_cycle + 1) numbers.
#         # # So we skip the first len(nums) - (len_cycle + 1) many numbers,
#         # # to reach the number that begins the cycle, i.e. the DUPLICATE number...
        

        
#         # print(f"{len_cycle=}, {count=}, {len(nums)=}")
#         # # print(f"{count}")
#         # return 0

#         # # Now that we know length of CYCLE to be 'count', we analyze the following:
#         # # This cycle contains the duplicate number, but only once (since its a cycle),
#         # # and all the other numbers being obviously unique (guaranteed by problem description).
#         # # Hence, there are 'count' unqiue numbers in this cycle, so beginning of linked
#         # # list chain contained (n+1) - count unique integers, including duplicate number.
#         # # Hence, duplicate number is at index ((n+1)-count) - 1.


#         # # We can calculate the length of the cycle, as well as HOW LONG
#         # # it takes for tortoise and hare to collide FROM the beginning.
#         # # Using these two values, we can detect where the cycle STARTED FROM,
#         # # i.e. the DUPLICATE NUMBER...



#         # # # print(f"{tortoise=}, {hare=}")
#         # # # hare = nums[tortoise]
#         # # tortoise = nums[tortoise]
#         # # hare = nums[tortoise]
#         # steps = 0
#         # while tortoise != hare or tortoise == 0:
#         #     tortoise = nums[tortoise]
#         #     hare = nums[nums[hare]]
#         #     # print(f"{tortoise=}, {hare=}")
#         #     steps += 1
        
#         # # print(f"{steps=}")
#         # tortoise = 0
#         # for _ in range(steps - 1):
#         #     tortoise = nums[tortoise]
        
#         # return tortoise
        
#         # # for _ in range(100):
#         # #     tortoise = nums[tortoise]
#         # #     hare = nums[nums[hare]]
#         # #     while tortoise != hare or tortoise == 0:
#         # #         tortoise = nums[tortoise]
#         # #         hare = nums[nums[hare]]
#         # #         print(f"{tortoise=}, {hare=}")

#         # return nums[hare]
        
#         # #  0 1 2 3 4
#         # # [1,3,4,2,2]

#         # # th
#         # # 1 -> 
        
#         # return tortoise



#         # START -> 1 -> 3 -> 4 -> 2 -> 2 -> START


#         # A -> B -> C -> D -> A

#         #      th                                
#         # A -> B -> C -> D -> A

#         # [3,1,3,4,2]

#         # th                
#         # 3 -> 1 -> 3 -> 4 -> 2

#         #  0 1 2 3 4
#         # [3,1,3,4,2]

#         # 3 -> 4 -> 2 -> 3 -> 4 -> 2

#         #  0 1 2 3 4
#         # [1,3,4,2,2]

#         #  0 1 2 3 4 5
#         # [1,2,3,4,5,5]

#         #  0 1 2 3 4
#         # [1,3,4,2,2]

#         #           t         h
#         # 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 -> 4 -> 2

#         #  0 1 2 3 4
#         # [3,1,3,4,2]

#         # th
#         # 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3

#         #  0   1   2   3  4   5  6   7  8  9   10 11 12  13 14  15  16  17 18 19  20
#         # [14, 17, 15, 9, 13, 6, 16, 2, 7, 10, 1, 3, 12, 4, 11, 17, 19, 20, 8, 18, 5]


#         #                                                              th  
#         # 14 -> 11 -> 3 -> 9 -> 10 -> 1 -> 17 -> 20 -> 5 -> 6 -> 16 -> 19 -> 18 -> 8

                        
#         # -> 7 -> 2 -> 15 -> 17 -> ...


#         #  0 1 2 3 4 5 6 7 8 9
#         # [2,5,9,6,9,3,8,9,7,1]

#         #      t    h
#         # 2 -> 9 -> 1 -> 5 -> 3 -> 6 -> 8 -> 7 -> 9

#         #  0 1 2 3 4
#         # [1,2,3,4,1]

#         # 1 -> 2 -> 3 -> 4 -> 1

#         # 2 <-> 4

#         # th        h    t
#         # 1 -> 3 -> 2 -> 4 -> 2 -> ...

#         # 2,4,5 -> 3rd

#         # 3,3,5 -> 1st/3rd

#         # 

#     # By the time the tortoise reaches the cycle, say it takes n steps,
#     # the hare will already be n steps DEEP into the cycle. So if the cycle is of length M,
#     # we know that the tortoise and hare are at most M - 1 steps apart (and at minimum 0).
#     # Therefore, at this point, the tortoise and hare are M - 1 - (n % (M - 1)) steps apart.
#     # So that 

#     # A -> B -> C -> D -> <cycle>

#     # when tortoise and hare meet, they will do so at step M. step M = X + Y, where X'th number
#     # is the DUPLICATE number. 



#     # C_1 -> C_2 -> ... -> C_N -> <cycle of length M>

#     # when tortoise reaches the first element of cycle, it took N steps to do so.
#     # This means, the hare is N steps ahead of the tortoise, but wraps around every
#     # M steps, so really something more of the like of N % M or N % (M - 1). Then,
#     # 

#     # When tortoise and hare meet, they are x steps away from original start of cycle.
#     # This was the same distance between tortoise and hare, when tortoise was at start of cycle.
#     # This means that tortoise/hare is M - x steps away from start of cycle, where M is length
#     # of cycle. If we were to reset the tortoise to the first position, it would not reach the
#     # cycle until at least x steps, meaning the hare would now be x + x == 2x steps ahead of it.
#     # Hence when the turtle and hare eventually meet, they will have done so in M - 2x steps.
#     # (M - x) - (M - 2x) == M - x - M + 2x == x, so by subtracting these values, we obtain
#     # that value of x that we so desperately need. After that, the problem is trivial, in that
#     # we just get the x'th number in the linked list chain. Since it could be that 2x > M or
#     # even x > M, the actual values will reflect cycle rotations, so likely we need to subtract
#     # the min from the max of these two values.
#         tortoise, hare = 0, 0
#         tortoise, hare = nums[tortoise], nums[nums[hare]]
#         m_minus_x = 0 # x + (cM - x), with smallest c such that cM - x >= 0
#         while tortoise != hare:
#             tortoise, hare = nums[tortoise], nums[nums[hare]]
#             m_minus_x += 1
#         old_tortoise = tortoise

#         hare = 0
#         m_minus_two_x = 0
#         while tortoise != hare:
#             # tortoise, hare = nums[tortoise], nums[nums[hare]]
#             tortoise, hare = nums[tortoise], nums[hare]
#             m_minus_two_x += 1
#         new_tortoise = tortoise
        
#         x = 0
#         while old_tortoise != new_tortoise:
#             old_tortoise = nums[old_tortoise]
#             x += 1
        
#         print(f"{x=}")

#         print(f"{m_minus_x=}")
#         print(f"{m_minus_two_x=}")
#         return 0
