def longestarray(array):
    maximum = 0
    counter = 0
    difference = []
    for j in range(N-1):
        difference.append(array[j] - array[j+1])
    difference.append(-1e9)
    for k in range(len(difference)-1):
        if difference[k] == difference[k+1]:
            counter += 1
        else:
            maximum = max(maximum, counter)
            counter = 0
    return maximum+2




testcases = int(input())
for i in range(testcases):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = longestarray(numbers)
    print('Case #' + str(i+1) + ': ' + str(result))