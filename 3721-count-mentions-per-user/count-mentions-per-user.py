class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        MESSAGE, OFFLINE = "MESSAGE", "OFFLINE"
        N = len(events)
        for i in range(N):
            events[i][1] = int(events[i][1])

        events.sort(key = lambda event: (event[1], 0 if event[0] == OFFLINE else 1)) # sort by timestamp, and then process offline requests first!
        # print(f"{events=}")
        status = defaultdict(int) # earliest time user is online!
        mentions = defaultdict(int)
        

        global_count = 0

        for event_type, timestamp, string in events:
            # print(f"{mentions=}")
            if event_type == OFFLINE:
                # user_id = int(string)
                user_id = int(string)
                status[user_id] = timestamp + 60
                continue

            assert event_type == MESSAGE
            if string == "ALL":
                # Instead of looping through dictionary, just use global var!
                global_count += 1
                continue

            if string == "HERE":
                for user_id in range(numberOfUsers):
                    # print(f"{user_id=}, {timestamp=}, {status=}")
                    if timestamp >= status[user_id]: # i.e. if NOT offline!
                        mentions[user_id] += 1
                continue

            user_ids = map(lambda id: int(id[2:]), string.split(" "))
            for user_id in user_ids:
                mentions[user_id] += 1

        # print(f"{status=}")
        # print(f"{mentions=}")
        return [
            mentions[user_id] + global_count
            for user_id in range(numberOfUsers)
        ]
            
            
            