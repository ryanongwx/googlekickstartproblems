def longestarray(array):
    maximum = 0
    for j in range(N-1):
        counter = 0
        difference = array[j] - array[j+1]
        initial = j
        while True:
            if j >= N-1:
                break
            if array[j] - array[j+1] == difference:
                if j == initial:
                    counter += 1
                counter += 1
            else:
                break
            j += 1
        maximum = max(maximum, counter)
    return maximum

testcases = int(input())
for i in range(testcases):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = longestarray(numbers)
    print('Case #' + str(i+1) + ': ' + str(result))