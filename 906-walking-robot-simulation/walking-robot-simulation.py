class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.dir = None # direction, i.e. "north", "east", "south", or "west"
        self.max_dist = 0
        self.obstacles = None
        self.dir_map = { 
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }
    def getDistance(self, origin, dest):
        x1, y1 = origin
        x2, y2 = dest
        return pow((x1 - x2), 2) + pow((y1 - y2), 2)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.x, self.y = 0, 0 # current position (initially origin)
        self.dir = "north" # can be "north", "east", "south", or "west"
        self.obstacles = set(tuple(obstacle) for obstacle in obstacles)

        for command in commands:
            # Turn left
            if command == -2:
                self.dir = self.changeDirection("left")
                continue

            # Turn right
            if command == -1:
                self.dir = self.changeDirection("right")
                continue
            
            # Move k steps forward
            k = command
            # print(k, command, commands)
            assert 1 <= k <= 9
            # Idea: want to move up to k steps forward. We can do this
            # with a for loop that iterates up to k times, moving 1 step
            # for each for-loop iteration, and in each iteration checking
            # if stepping would cause us to hit an obstacle. If so then we
            # break, otherwise we update the current robot's position, as
            # well as updating the maximum squared Euclidian distance
            # found so far (if the current position happens to be the largest).
            for _ in range(k):
                assert self.dir in self.dir_map
                dx, dy = self.dir_map[self.dir]
                origin = (0, 0)
                new_pos = (self.x + dx, self.y + dy)
                # print(f"{new_pos}")
                if self.isObstacle(new_pos):
                    break

                new_dist = self.getDistance(origin, new_pos)
                self.max_dist = max(self.max_dist, new_dist)
                self.x, self.y = new_pos

        return self.max_dist
    
    def changeDirection(self, turn_direction):
        assert turn_direction in ["left", "right"]
        return self.turnLeft() if turn_direction == "left" else self.turnRight()
    
    def turnLeft(self):
        d = {
            "north": "west",
            "west": "south",
            "south": "east",
            "east": "north"
        }
        assert self.dir in d
        return d[self.dir]
    
    def turnRight(self):
        d = {
            "north": "east",
            "east": "south",
            "south": "west",
            "west": "north"
        }
        assert self.dir in d
        return d[self.dir]

    def isObstacle(self, pos):
        x, y = pos
        return (x, y) in self.obstacles