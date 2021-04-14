# array of N positive integers
#  i-th integer of the array is Ai
# [3, 2, 1] is a 3-countdown
# Number of K-countdowns in her array

def findcountdown(m, numberarray1):
    counter = 0
    if m not in numberarray1:
        return 0
    for i in range(N):
        if numberarray1[i] == m and i != N-1:
            for j in range(1, m):
                if numberarray1[i+j] == 1:
                    counter += 1
                    m = K
                if numberarray1[i+j] == m-1:
                    m -= 1

    return counter


testcases = int(input())
for i in range(testcases):
    N, K = map(int, input().split())
    numberarray = list(map(int,input().split()))
    numberofmcountdown = findcountdown(K, numberarray)
    print("Case #" + str(i+1) + ": " + str(numberofmcountdown))