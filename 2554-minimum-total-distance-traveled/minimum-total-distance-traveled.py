class Solution:
    def __init__(self):
        self.robot = None
        self.factory = None
        self.memo = {}
    
    def minDistDp(self, robot_index, factory_index, factory_limit):
        POS, LIMIT = 0, 1
        # if (robot_index, factory_index)
        # if robot_index >= len(self.robot) or factory_index >= len(self.factory):
        #     return 0
        if robot_index >= len(self.robot):
            return 0
        
        # If still robots left but no factories left to choose from, impossible
        # problem, hence return inf to "discourage" this invalid solution
        if factory_index >= len(self.factory):
            return float("inf")
        
        if factory_limit == None:
            factory_limit = self.factory[factory_index][LIMIT]
        
        if (robot_index, factory_index, factory_limit) in self.memo:
            return self.memo[(robot_index, factory_index, factory_limit)]

        # Case 1: Add robot_index to factory_index (IF ENOUGH SPACE)
        case1 = float("inf")
        if factory_limit > 0:
            case1 = self.minDistDp(robot_index + 1, factory_index, factory_limit - 1)
            robot_pos = self.robot[robot_index]
            factory_pos = self.factory[factory_index][POS]
            case1 += abs(robot_pos - factory_pos)

        # Case 2: Don't add robot to factory_index (IF ENOUGH FACTORIES?)
        case2 = self.minDistDp(robot_index, factory_index + 1, None)

        res = min(case1, case2)
        self.memo[(robot_index, factory_index, factory_limit)] = res
        return res

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        self.robot = robot
        self.factory = factory

        POS, LIMIT = 0, 1

        robot.sort()
        factory.sort(key = lambda x: x[POS])

        return self.minDistDp(0, 0, factory[0][LIMIT])

        factory_dict = {pos: limit for pos, limit in factory}
        # return self.minTotalDistanceDp(0, tuple((pos, limit) for pos, limit in factory))
        return self.minTotalDistanceDp(0, factory_dict)
    
    def factoryDictToTuple(self, factoryDict):
        return tuple((pos, limit) for pos, limit in factoryDict.items())
    
    def factoryDictToBoolTuple(self, factoryDict):
        return tuple((pos, limit > 0) for pos, limit in factoryDict.items())

    def minTotalDistanceDp(self, i, _factory_dict):
        # i have n elements, each of which with n possible values
        # so worst case is n * n^n space for dp, == n^(n+1)
        factory_dict = _factory_dict.copy()
        # Add i'th robot to best factory
        if i >= len(self.robot):
            return 0
        
        tuple_factory = self.factoryDictToTuple(factory_dict)
        # tuple_factory = self.factoryDictToBoolTuple(factory_dict)
        if (i, tuple_factory) in self.memo:
            return self.memo[(i, tuple_factory)]
        
        robot_pos = self.robot[i]
        res = float("inf")
        for factory_pos in factory_dict:
            limit = factory_dict[factory_pos]
            if limit > 0:
                dist = abs(factory_pos - robot_pos)
                factory_dict[factory_pos] -= 1
                case = dist + self.minTotalDistanceDp(i + 1, factory_dict)
                factory_dict[factory_pos] += 1

                res = min(res, case)
        
        self.memo[(i, tuple_factory)] = res
        return res


# Case 1: O(n^3) direct sol.

# Case 2: 1D dp, with O(n^2) body loop

# Case 3: 2D dp, with O(n) body loop

# Case 4: 3D dp, with O(1) body loop

# where n = max(robot.length, factory.length)
