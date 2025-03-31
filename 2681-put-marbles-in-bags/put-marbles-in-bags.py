# Okok so as always in all my videos I do a quick recap of I how I was able to solve the problem!
# This problem I was struggling because I was really trying to force the subarrays, and if the
# constraints said that 2 * k <= len(weights)... I would have been BING CHILLING. My idea was
# essentially grab the 2 * k largest indices, since then you could have all partitions you need
# (now I think about it, might not cover everything). I first did DP which works but is too slow obviously.
# I then thought "okay what if I grab index N-1 and then the k-1 largest indics in value besides N-1". Then
# I could sort them, i.e having indices i1,i2,...,i_{k-1},i_k where i_k == N - 1. Then I could make my
# partitions weights[0..i1], weights[i1+1..i2], ..., weighs[i_{k-1}..N-1]. But even that was incorrect.
# I read the hints, and they were not helpful AT ALL. I then (during one of the breaks in Vancouver-Seattle
# bus ride) decided to scroll through discussions to see what people were saying about this problem. I found
# an "actually helpful hints" comment, and saw a clever idea for solving this problem: USE the fact that
# since we must make k non-overlapping subarrays, we can treat this as making k-1 cuts, where each cut will
# have the elements adjacent to the cut contribute to the overall score! Since they will denote the end &
# start of their own separate partitions, respectively! Hence we grab the score from making k-1 cuts, as
# well as weights[0] and weights[N - 1] as those are baked in by default. To find max solution, we simply
# grab largest k-1 cuts. To find min solution, we simply grab smallest k-1 cuts. Then we get their
# difference and voila, we have our solution!! For "grabbing cuts" logic, I simply created a 'cut_profit'
# array where cut_profit[i] == profit from splitting into nums[..i], nums[i+1..] == nums[i] + nums[i+1].
# Then I turn cut_profit into a max_heap that I pop from k-1 times to get max solution, and similarly
# into a min_heap that I pop from k-1 times as well to get min solution. Again, grab the difference
# between these results, and BADA-BING-BADA-BOOM you got a nice and working solution!!
# But otherwise, that's pretty much it for this video, if you did find it useful or enjoyable in any
# way-shape-or-form, I'd highly appreciate it if you left a #LIKE or a #COMMENT, but otherwise... I'll
# catch you in the next one! So until then, chao chao my friend. Bye bye :)
class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        N = len(weights)

        # EDIT: 
        # Okay hey there, I am back!! While I was taking my break outside, I decided to scroll
        # through discussions for this problem on my phone to see what people were saying.
        # I saw a couple comments talking about how hints were not helpful (lol can relate...)
        # but some posts with "actually good hints". I looked at one of them that talks about
        # realizing that making k bags means making k - 1 total cuts, and wherever you make
        # these cuts will end up being where the adjacent elements of those cuts become
        # used for sum of the weights, including of course weights[0] and weights[N - 1]
        # I feel like a complete idiot... but this problem is pretty much trivial now then...

        # Step 1: Let's grab all pairs of adjacent elements, so if we make a "cut" between
        # them we know how much they contribute to overall score. weights[0] and weights[N - 1]
        # already contribute by default no matter what.
        cut_profit = [] # cut_profit[i] == profit from splitting into nums[..i], nums[i+1..]
        for i in range(N - 1):
            profit = weights[i] + weights[i + 1]
            cut_profit.append(profit)
        
        # Step 2(a): Solve for k highest-yielding cuts (maximize!)
        max_sol = weights[0] + weights[N - 1] # will cancel itself out later, but whatebbssss
        max_heap = [-profit for profit in cut_profit]
        heapq.heapify(max_heap)
        for _ in range(k - 1):
            # '-=' since simulating max-heap via min-heap w/ neg. values!
            max_sol -= heapq.heappop(max_heap)
        
        # Step 2(b): Solve for k lowest-yielding cuts (minimize!)
        min_sol = weights[0] + weights[N - 1] # cancels itself out, but eh -- might as well add it :)
        min_heap = cut_profit
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            min_sol += heapq.heappop(min_heap)
        
        # Step 3: Return difference, and voila!!!
        return max_sol - min_sol
