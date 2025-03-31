# Okay, I will not see if I am able to troubleshoot the wifi...
# Will cut the video here, and resume as soon as I have wifi and was able to hit run & submit!!
# See you in just one second :)
# OKAY I'M BACK - my phone is at low battery, but I'm using my hotspot and I think it's BARELY enough...
# LET'S RUN ITTTTTTTT OMGGGG
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
