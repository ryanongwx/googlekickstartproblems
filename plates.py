def recursion(ithstack, platestaken, memo):
    key = str(ithstack) + ',' + str(platestaken)
    if key in memo:
        return memo[key]
    if platestaken == p:
        memo[key] = 0
        return memo[key]
    if ithstack > n:
        if platestaken == p:
            memo[key] = 0
            return memo[key]
        else:
            memo[key] = -1e9
            return memo[key]
    if platestaken > p:
        memo[key] = -1e9
        return memo[key]

    for i in range(k+1):
        if i == 0:
            memo[key] = max(-1e9, recursion(ithstack + 1, platestaken + i, memo))
        if i > 0:
            memo[key] = max(memo[key], (plates[ithstack - 1][i-1] + recursion(ithstack + 1, platestaken + i, memo)))
    return memo[key]


casenumber = int(input())

for l in range(casenumber):
    n, k, p = map(int, input().split())
    plates = []
    for j in range(n):
        beautyvalues = list(map(int, input().split()))
        current = 0
        pile = []
        for t in beautyvalues:
            current += int(t)
            pile.append(current)
        plates.append(pile)
    memo = {}
    fans = recursion(1, 0, memo)
    print("Case #" + str(l+1) + ": " + str(fans))

