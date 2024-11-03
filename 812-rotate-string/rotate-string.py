class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        arr_s = collections.deque([char for char in s])
        arr_goal = collections.deque([char for char in goal])

        for _ in range(len(s)):
            if arr_s == arr_goal:
                return True
            
            arr_s.append(arr_s.popleft())
        
        return False