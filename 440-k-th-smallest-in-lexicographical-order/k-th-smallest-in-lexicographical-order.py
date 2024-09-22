# BRILLIANT IDEA: Look at number of digits that n occupies. So for n = 123, you know theres 3 digits, so all numbers starting with 1 that are 1-2 digits in length are valid, and for 3 digits,
# then only those from 100-123 are valid. For n = 921 same thing, but now for 3 digits, everything, from 100-199 is valid for the 1-starting-digit integers. this is how you can get
# a FAST O(1) calculation for number of integers

# 2 [20-29]
# 20-29 [200-299]
# 200-299 [2000-2999]


class Solution:
    def __init__(self):
        self.n = None
        # self.count = 0
        self.k = None
        self.res = []
        self.memo = {}
        self.cache = {}
        self.d = {}
    
    # getKthSmallest from starting_digit originally (as num)
    def getKthSmallest(self, num, k):
        assert k >= 1
        if k == 1:
            return num
        print(f"{num=}, {k=}")
        k -= 1
        num *= 10
        i = 0
        # if k == 2:
        #     return num
        # while True:
        #     assert i < 10
        #     self.numChildrenFromNum(num + i)

        #     # Loop Invariant
        #     i += 1
        child = num
        max_ofs = min(10, max(0, self.n - num + 1))
        for i in range(max_ofs):
            child = num + i
            num_subchildren = self.numChildrenFromNum(child)
            print(f"{child=}, {num_subchildren=}, {k=}")
            if k > num_subchildren:
                k -= num_subchildren
                # print(k)
                # continue
            # k <= num_subchildren
            else:
                return self.getKthSmallest(child, k)
                # if k <= 0:
                #     assert k == 0
                #     return num + i + 1 # TODO: assert correct return
        # return -9999999
        # assert False
        # return child
        return self.getKthSmallest(num//10 + 1, k)
        

        # children = [num + i for i in range(10)]

    # broken / doesn't work
    # @cache
    def numChildrenFromNum(self, num):
        str_n = str(self.n)
        str_num = str(num)
        default_count = 0

        # 23
        # 230,231,...,239
        # 2300........2399
        # 23000.......23999
        # 11000
        if num > self.n:
            return 0
        count = 0
        for power in range(max(0, ((len(str(self.n)) - 1) - len(str(num)))) + 1):
            count += 10 ** power
        # count = max(1, 10 ** ((len(str(self.n)) - 1) - len(str(num))))
        # count += max(0, 11*((len(str(self.n)) - 1) - len(str(num))))
        # print(f"1: {count=}")
        # count = 10 ** ((len(str(self.n)) - len(str(num))+2 - 1) - 1)
        while len(str(num)) < len(str(self.n)):
            # count += 10
            num *= 10
        if num > self.n:
            print(f"3: {count=}, {num=}, {self.n=}")
            return count
            num //= 10
        max_ofs = (10 ** (len(str(num)) - 1 - 1)) - 1
        max_ofs = min(num + max_ofs, self.n + 1)
        for num in range(num, max_ofs):
            count += 1
        # print(f"2: {count=}")
        return count

        
        if num > self.n:
            return 0
        count = 1
        num *= 10
        for i in range(10):
            count += self.numChildrenFromNum(num)
        return count

        # T(n) = 10 * T(n/10)
        

        # num = 23 -> 230, self.n = 1421
        # num = 11 -> 110, self.n = 1234
        # num = 91, self.n = 10000
        # [910..919]
        # [9100..9109] ... [9190..9199]

        # under 910, there's 9100..9109
        # under 911, there's 9110..9119

        
        base = 10 ** (len(str_num)-1)
        # singles = int(str_num[-1]) * 10
        singles = int(str_num[-1])
        default_count += 1 # include num itself as part of children
        num *= 10
        flag = False
        #print(f"{base=}, {singles=}")
        for _ in range(len(str_n) - len(str_num) - 1):
            default_count += min(10, max(0, self.n - num + 1))
            if num * 10 > self.n:
                flag = True
                break
            # default_count += base - singles
            # default_count += 10 - singles
            # default_count += min(10, max(0, self.n - num + 1))
            base *= 10      # 10 --> 100
            singles *= 10   # 3 ---> 30
            num *= 10
            # default_count += base - singles
        
        print("DAS")
        print(default_count, base, singles, num)
        
        
        # num is now 2300
        # base = 10 ** (len(str(num)) - 1)
        max_offset = 10 ** ((len(str(num)) - 1) - 1) - 1
        # max_offset = (10 ** (len(str_n) - 1 - 1)) - 1
        
        default_count += max(0, min(num + max_offset, self.n) - num + 1)
        print(default_count, base, singles, num)
        return default_count


        # base = starting_digit * (10 ** (len(str_n)-1))
        # d[starting_digit] += max(0, min(base + 99, self.n) - base + 1)


        # singles = int(str_num[-1])
        # default_count += (10 - singles)
        # for _ in range(len(str_n) - len(str_num) - 1):
        #     num *= 10
        #     singles *= 10



        

        # base = len(str(num))
        # for _ in range(len(str_n) - 1):
        #     default_count += base
        #     base *= 10


    # O(logn)
    def numChildrenPerStartingPosition(self):
        # d = {}
        # for i in range(1, 9 + 1):
        #     d[i] = 1
        #     for j in range(10):
        #         d[i] += self.numChildrenFromNum(i * 10 + j)
        # return d
        str_n = str(self.n)
        default_count = 0
        base = 1
        for _ in range(len(str_n) - 1):
            default_count += base
            base *= 10
        d = {i: default_count for i in range(1, 9 + 1)}
        for starting_digit in d:
            # n = 721
            base = starting_digit * (10 ** (len(str_n)-1))
            max_ofs = 10**(len(str_n)-1)
            # print(f"{max_ofs=}")
            d[starting_digit] += max(0, min(base + max_ofs, self.n + 1) - base)
        
        self.d = d
        return d




    def getSortedIndex(self, num):
        # This is not accurate. You will need to OFFSET
        # by number of children inside each smaller starting digit
        # i.e. for number like 213, you will get sortedIndex starting
        # from index of position 2, not from position of index 0.
        if num in range(1, 9 + 1):
            return 0
        if num in self.cache:
            return self.cache[num]
        num_divisible_by_ten = ((num % 10) == 0)
        if num % 10 != 0:
            res = 1 + self.getSortedIndex(num - 1)
            # res = self.getSortedIndex(num - 1) + self.getNumChildren(num - 1)
            self.cache[num] = res
            return res
        
        num_divisions = 0
        while num % 10 == 0:
            num //= 10
            num_divisions += 1
        res = num_divisions + self.getSortedIndex(num)
        self.cache[num] = res
        return res
    # getKthSmallest from starting_digit originally (as num)
    def getKthSmallestOld(self, num, k):
        assert k >= 1
        if k == 1:
            return num
        
        # num *= 10
        # if num > self.n:
        #     return -1
        smallest_child = num * 10
        biggest_child = min((num * 10) + 9, self.n)
        # if smallest_child > biggest_child:
        #     return -1

        # assert smallest_child <= biggest_child <= self.n
        # ###print(smallest_child, biggest_child, self.n)

        count = 1
        child = smallest_child
        while True:
            assert smallest_child <= child <= biggest_child
            prev_count = count
            count += self.getNumChildren(child)
            # child += 1
            # TODO: confirm this is >= k and not > k!
            if count >= k:
                # child possesses k'th smallest as one of its children (or itself)
                # so search recursively in there
                return self.getKthSmallest(child, k - prev_count)
            else:
                child += 1
        
        return None
        
    def getNumChildren(self, num):
        # Must set self.count back to 0 first time call this function every time!
        # For now, assume num == 1
        if num > self.n:
            return 0
        if num in self.memo:
            return self.memo[num]
        count = 1
        # self.res.append(num)
        # TODO: should be == k or == k - 1 here?
        # if count == k: 
        #     self.res = num
        #     return -1

        smallest_child = num * 10
        biggest_child = min((num * 10) + 9, self.n)
        # if smallest_child > self.n:
        #     return 1
        
        for child in range(smallest_child, biggest_child + 1):
            count += self.getNumChildren(child) # (+1) for the child itself
            # TODO: can end termination here!
            # if count >= k:
            #     break
        
        self.memo[num] = count
        return count
        
        
        # smallest_child <= self.n < biggest_child
        # smallest_child <= self.n >= biggest_child
        
        # if biggest_child > self.n:
            
        # [num, (num + 9)]

    def findKthNumber(self, n: int, k: int) -> int:
        self.n = n
        self.k = k
        # print(f"{self.numChildrenFromNum(1)=}") # should be 111
        #print(sorted(range(1,n+1), key=lambda x: str(x)))
        # ##print(self.getSortedIndex(112))
        # d = self.numChildrenPerStartingPosition()
        # d = {i: self.numChildrenFromNum(i) for i in range(1, 9 + 1)}
        
        # print(f"{d=}")
        # assert sum(d.values()) == self.n
        # return 1

        if k == 1:
            return 1
        
        num = 1
        k -= 1

        while k > 0:
            count = self.countBetween(num, num + 1)
            if k < count:
                # k'th smallest must be within num's children
                num *= 10
                k -= 1
                continue
            
            assert k >= count
            num += 1
            k -= count
        
        return num
            
        
        #print(k)
        starting_digit = 1
        while k > d[starting_digit]:
            k -= d[starting_digit]
            starting_digit += 1
        print(f"{k=}, {starting_digit=}")
        # return self.getKthSmallest(starting_digit, k - 1)
        return self.getKthSmallest(starting_digit, k)

        starting_digit = 0
        num_children = [] # at most 10 elements, so sum(num_children) is O(1) time
        while k > sum(num_children):
            starting_digit += 1
            num_children.append(self.getNumChildren(starting_digit))
        
        # Step 1: figure out how many children are under 1. 
        # starting_digit = 1
        # count = 1
        # self.count = 0

        # starting_digit = 1
        # num_children = self.getNumChildren(starting_digit)
        starting_digit = 0
        num_children = [] # at most 10 elements, so sum(num_children) is O(1) time
        while k > sum(num_children):
            starting_digit += 1
            num_children.append(self.getNumChildren(starting_digit))
        ###print(f"{starting_digit=}, {num_children=}")

        # Update k such that want to find k'th smallest FROM starting digit
        #print(k)
        k -= sum(num_children)
        k += num_children[-1]
        #print(k, starting_digit)
        return self.getKthSmallest(starting_digit, k)

        return 1

        # ###print(res)
        ###print(self.res)
        return res




        # Given integer i, 1 <= i <= n, where i is X'th lexicographically smallest integer,
        # need to find the value of X in O(P) <= O(logn) time.
        # 9 * O(P), 9 * O(P), 9 * O(P), ... until get >= n, and keep moving by 10x each time
        # 10^x >= n
        # T(n) = 1 * T(n / 9) + 9*(n^d)
        # a = 1, b = 9, c = 9, d = ?
        # if d = 0.5, then final solution would be O(n^0.5) == O(sqrt(n)) time, which is good!

        # MERGESORT:
        # T(n) = 2T(n/2) + cn --> O(nlogn)

        # BINARY SEARCH:
        # T(n) = 1*T(n/2) + c --> O(logn)

        # GENERIC D&C RECURRENCE:
        # T(n) = a * T(n / b) + cn^d

        # MASTER THEOREM:
        # T(n)
        # == a * T(n / b) + cn^d
        # ==
        #       O(n^d),         if a < b^d
        #       O(n^dlogn),     if a = b^d
        #       O(n^log_b(a)),  if a > b^d

        # O(logn)
        # l, r = 1, n
        # mid = (l + r) // 2
        ###print(sorted(range(1, n + 1), key=lambda num: str(num)))
        return 1

        # i --> children == [10 * i, ..., 10 * i + 9]

        # i = 100
        # min(i + 9, n) - i



        # Want: 1 <= i <= n, and i is X'th smallest, what is value of X?


        # O(n)
        # res = self.lexicalOrder(n)
        # return self.res[k - 1]

        # O(n + klogn)
        # arr = [str(i) for i in range(1, n + 1)]
        # heapq.heapify(arr)
        # for _ in range(k - 1):
        #     heapq.heappop(arr)
        # return int(arr[0])


        # 121 // 10 --> 12.1
        # 110 // 10 --> 11 // 10
        # 100 // 10 --> 10 // 10 --> 1
    
    # at this point I am ~half-a-dozen hours into the problem, and now finally
    # looking at the editorial for assistance. I did not think of the count steps
    # between two prefixes idea, I was fixated on calculating the number of children
    # that exist beneath a certain node/number, and using that information to efficiently
    # find k'th smallest integer (but could not write an effienct and/or correct algorithm.)
    def countBetween(self, num1, num2):
        count = 0
        while num1 <= self.n:
            count += min(num2, self.n + 1) - num1
            num1 *= 10
            num2 *= 10
        return count

# 11, 18
