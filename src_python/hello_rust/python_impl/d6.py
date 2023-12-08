sample_input1 = sample_input2 = """Time:      7  15   30
Distance:  9  40  200""".splitlines()


def solve1(input: list[str]) -> str:
    times, dists = input
    times = list(map(int, times.split()[1:]))
    dists = list(map(int, dists.split()[1:]))

    ways_to_beat = 1
    for target_time, target_dist in zip(times, dists):
        speeds = []
        for charged_speed in range(1, target_time):
            dist = (target_time - charged_speed) * charged_speed
            if dist > target_dist:
                speeds.append(charged_speed)
        ways_to_beat *= len(speeds)

    return str(ways_to_beat)


def solve2(input: list[str]) -> str:
    target_time, target_dist = input
    target_time = int(target_time.replace("Time: ", "").replace(" ", ""))
    target_dist = int(target_dist.replace("Distance: ", "").replace(" ", ""))

    # Could to binary/ternary search but this is fast enough
    ways_to_beat = 0
    for charged_speed in range(1, target_time):
        dist = (target_time - charged_speed) * charged_speed
        if dist > target_dist:
            ways_to_beat += 1

    return str(ways_to_beat)


full_input1 = full_input2 = """Time:        38     67     76     73
Distance:   234   1027   1157   1236""".splitlines()
