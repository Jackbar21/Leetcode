class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Tortoise and hare meet after M steps, where M is the length of the cycle.
        # But we know there is an initial chain of length X that the tortoise must
        # go through before reaching the FIRST element of the linked list closed cycle,
        # which happens to be the duplicate number. Therefore, when the tortoise and hare
        # meet, they must be at position M - X inside the linked list cycle. Since we know
        # that position is X steps away from the beginning of the cycle, and that the element
        # at index 0 (the start of the ACTUAL linked list) is also X steps away from the
        # beginning of the cycle, we know that if we have two pointers at these positions that
        # keep advancing, after X steps, they will now both be at the position of the cycle's
        # start (i.e. that of the duplicate number). This is great, because we can easily
        # detect if the two pointers have collided, despite the fact that we have no idea what
        # this value of X is! Therefore, by having these two pointers advance at the same time,
        # we can be confident that when they interesct (not if!), it will be at the position
        # at the beginning of the linked list closed-cycle, which we know to be the duplicate
        # number :) Therefore, we can simply return the number at that position.

        # FURTHER CLARIFICATION:
        # When the tortoise enters beginning of cycle, it has taken X steps to do so.
        # This means that the hare is currently X steps ahead of the tortoise, since
        # it moves at twice the speed of the tortoise. Since we know that the gap between
        # tortoise and hare is how many steps it will take for them to reach one another,
        # and that both are now currently in the same closed cycle in the linked list, then
        # given some arbitrary M where M is the length of this linked list closed cycle, the
        # gap between the tortoise and hare must be M - X, and hence will take M - X MORE steps
        # to reach one another. Hence, they will have taken a total of X + (M - X) == M steps
        # to reach one another. This is why we KNOW that the tortoise and hare will meet each
        # other for the first time after exactly M steps, where M is the length of the linked
        # list closed cycle. This is why we were then able to make the argument that this
        # position was exactly X steps away from the beginning of the actual linked list cycle!

        tortoise, hare = 0, 0
        tortoise, hare = nums[tortoise], nums[nums[hare]]
        while tortoise != hare:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
        
        turtle = 0
        while turtle != tortoise:
            turtle, tortoise = nums[turtle], nums[tortoise]
        
        return turtle
