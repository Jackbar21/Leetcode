class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        N, M = len(groups), len(elements)
        MAX = pow(10, 5)

        d = {}
        seen = set()
        for j, element in enumerate(elements):
            val = element
            if val in seen:
                continue
            seen.add(val)
            while val <= MAX:
                d[val] = d.get(val, j)
                val += element
        
        return [d.get(num, -1) for num in groups]
            

        product = functools.reduce(lambda acc, e: acc * e, elements, 1)
        product *= math.ceil(max(groups) / product) + 1
        
        for i, num in enumerate(groups):
            assert product > num
            if product % num != 0:
                continue

            # Find first valid element
            for j, el in enumerate(elements):
                if num % el == 0:
                    res[i] = j
                    break

        return res

        # element_dict = {}
        # for j, element in enumerate(elements):
        #     element_dict[element].append

        # for i, num in enumerate(groups):
        #     for div in range(1, num):
            

        d = defaultdict(list)

        sorted_groups = sorted((num, i) for i, num in enumerate(groups))
        sorted_elements = sorted((elmnt, i) for i, elmnt in enumerate(elements))

        print(sorted_groups)
        print(sorted_elements)
        
        
        d = defaultdict(list)
        for i, num in enumerate(groups):
            # O(sqrt(N))
            for factor in range(1, num // 2 + 4):
                if num == 0 or num % factor == 0:
                    d[factor].append(i)

        # print(d)
        for j, element in enumerate(elements):
            for index in d[element]:
                if res[index] == -1:
                    res[index] = j

        return res
        
        
        
        unvisited = set(range(N))

        while len(unvisited) > 0:
            index = unvisited.pop()
            num = groups[index]
            for j, element in enumerate(elements):
                if num % element == 0:
                    cur_index = res[index]
                    if cur_index == -1 or j < cur_index:
                        res[index] = j
                    break

        return res
                            
                        