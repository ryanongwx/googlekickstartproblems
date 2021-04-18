

def checknotes(notesleft, rulebreak, repitition, pos, start):
    # Iterate over the 4 different starting positions
    if len(notesleft) == 1:
        return rulebreak
    if repitition is True:
        positions = 1e9
        for i in range(1, 5):
            if start is True:
                pos = i
                positions = min(positions, checknotes(notes, rulebreak, False, pos, False))
            if pos is False:
                pos = i
                positions = min(positions, checknotes(notesleft, rulebreak, False, pos, False))
        return positions
    if repitition is False:
        for j in range(len(notesleft)-1):
            if pos > 4 or pos < 1:
                rulebreak += 1
                return checknotes(notesleft, rulebreak, True, False, False)

            if 0 < pos < 5:
                if notesleft[j+1] > notesleft[j]:
                    # Place j+1 on the next key
                    pos += 1
                if notesleft[j+1] < notesleft[j]:
                    # Place j+1 on the previous key
                    pos -= 1
                if notesleft[j+1] == notesleft[j]:
                     # Do nothing as j+1 on the same key
                    pos = pos
                notesleft.remove(notesleft[j])
                return checknotes(notesleft, rulebreak, False, pos, False)

testcases = int(input())
for p in range(testcases):
    K = int(input())
    notes = list(map(int, input().split()))
    result = checknotes(notes, 0, True, 0, True)
    print('Case #' + str(p+1) + ': ' + str(result))
