# Input is as follows:
# Number of Houses on sale(N)  Budget(B)
# Prices of N Houses

# Output is as follows:
# Case Number: Maximum number of houses that can be bought
casenumber = int(input())

# Generating an output
for i in range(casenumber):
    n, budget = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    ans = []
    s = 0
    for j in prices:
        s = s + j
        if s <= budget:
            ans.append(s)
    print("Case #{}: {}".format(i + 1, len(ans)))

