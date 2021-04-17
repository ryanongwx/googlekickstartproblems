
def findcountdown():
    counter = 0
    if K not in numberarray:
        return 0
    for l in range(N-K+1):
        if numberarray[l] == K:
            inner = 0
            for p in range(K):
                if numberarray[l + p] == marray[p]:
                    inner += 1
                if inner == K:
                    counter += 1
    return counter


testcases = int(input())
for i in range(testcases):
    N, K = map(int, input().split())
    numberarray = list(map(int,input().split()))
    marray = []
    for p in range(K):
        marray.append(K-p)
    numberofmcountdown = findcountdown()
    print("Case #" + str(i+1) + ": " + str(numberofmcountdown))