def recursion(bus, day, bustimings, firstday, memo):
    key = str(bus) + ',' + str(day) + ',' + str(firstday)
    print(memo)
    if key in memo:
        return memo[key]
    if bus == n and day <= d:
        return firstday
    if bus > n or day > d:
        return 0
    memo[key] = 0
    for i in range(len(bustimings[bus])):
        if bustimings[bus][len(bustimings[bus])-1-i] >= day:
            if bus == 0:
                firstday = bustimings[0][len(bustimings[bus])-1-i]
            day1 = bustimings[bus][len(bustimings[bus])-1-i]
        if bustimings[bus][len(bustimings[bus]) - 1 - i] < day:
            day1 = d+1
        rc = recursion(bus + 1, day1, bustimings, firstday, memo)
        memo[key] = max(memo[key], rc)
    return memo[key]

# Mistake is that the day in the first recursion does not remain at 0 as it loops
# When the second loop for the 6 is executed, the day is 9 already

tc = int(input())
bustimings = []
for j in range(tc):
    n, d = map(int, input().split())
    timings = list(input().split())
    bus = []
    for k in timings:
        bus1 = []
        for l in range(1, d+1):
            if l*int(k) <= d:
                bus1.append(l*int(k))
        bus.append(bus1)
    memo = {}
    latestday = recursion(0, 0, bus, 0, memo)
    print("Case #" + str(j+1) + ": " + str(latestday))