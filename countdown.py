# array of N positive integers
#  i-th integer of the array is Ai
# [3, 2, 1] is a 3-countdown
# Number of K-countdowns in her array

def findcountdown(m, numberarray1):
    counter = 0
    if m not in numberarray1:
        return 0
    for l in range(N-K+1):
        if numberarray1[l] == m:
            repitition = 0
            for j in range(1, K):
                if numberarray1[l+j] == 1 and repitition == K-2:
                    counter += 1
                if numberarray1[l+j] == K-j:
                    repitition += 1

    return counter


testcases = int(input())
for i in range(testcases):
    N, K = map(int, input().split())
    numberarray = list(map(int,input().split()))
    numberofmcountdown = findcountdown(K, numberarray)
    print("Case #" + str(i+1) + ": " + str(numberofmcountdown))