# rectangular wall containing R rows and C columns
# A wall is stable if it can be created by adding polyominos one at a time to the wall so that each polyomino is always supported.
# A polyomino is supported if each of its squares is either on the ground, or has another square below it.

# Recursion has to constantly check whether below is the same alphabet and whether below is the ground
# Take note that after one alphabet is initialized, it can be taken as the ground
# I think can approach by elimination method



def recursion(possiblestablearray, rownumber, resultarray, allalphabet, repititions):
    # Return values when edge conditions are met (When the target row to inspect exceeds the number of rows in the grid)
    if rownumber > R:
        for letter in possiblestablearray:
            if letter not in resultarray:
                resultarray.append(letter)
        if repititions > len(allalphabet):
            return -1

        if len(resultarray) == len(allalphabet):
            result = ""
            for thing in resultarray:
                result += thing
            return result

        return recursion([], 1, resultarray, allalphabet, repititions + 1)



    # Check those on the ground first and put them into a possible array
    if rownumber == 1:
        for alphabet in gridarray[R-rownumber]:
            if alphabet not in allalphabet:
                allalphabet.append(alphabet)
            # For the second round must leave out those in result array (2nd iteration)
            if alphabet not in resultarray:
                if alphabet not in possiblestablearray:
                  possiblestablearray.append(alphabet)
        return recursion(possiblestablearray, rownumber+1, resultarray, allalphabet, repititions)

    # Use Row number to check row by row whether the elements connected by same alphabet below
    if rownumber > 1:
        for i in range(C):
            # First iteration wheen resultarray is empty
            if len(resultarray) == 0:
                # Add all alphabets to the allalphabet array
                if gridarray[R-rownumber][i] not in allalphabet:
                    allalphabet.append(gridarray[R-rownumber][i])
                # If the block is supported from the ground (below if statement)
                if gridarray[R-rownumber][i] in possiblestablearray:
                    if gridarray[R-rownumber][i] != gridarray[R-rownumber+1][i]:
                        # This means that the block is not supported by block below it, hence remove from possible array
                        possiblestablearray.remove(gridarray[R-rownumber][i])
                        # If not supported, just go next, do not need to do anything
            # Second iteration when resultarray is not empty
            if len(resultarray) > 0:
                # Alphabetes may not start from the ground hence add along the way
                for item in gridarray[R-rownumber]:
                    if item not in gridarray[R-rownumber+1]:
                        possiblestablearray.append(item)
                # Checking whether the block is stable
                if gridarray[R - rownumber][i] in possiblestablearray:
                    # Treat the alphabets in resultarray as stable so exclude the ones that do not have itself or the walled letters underneath
                    if gridarray[R-rownumber][i] in possiblestablearray:
                        # If alphabet not the same as the one below it
                        if gridarray[R-rownumber][i] != gridarray[R-rownumber+1][i]:
                            # If alphabet below it is already formed and can treat as wall
                            if gridarray[R-rownumber+1][i] not in resultarray:
                                possiblestablearray.remove(gridarray[R - rownumber][i])

        return recursion(possiblestablearray, rownumber+1, resultarray, allalphabet, repititions)


testcases = int(input())
for l in range(testcases):
    gridarray = []
    R, C = map(int, input().split())
    for j in range(R):
        row = input()
        gridarray.append(list(row))
    answer = recursion([], 1, [], [], 0)
    print("Case #" + str(l+1) + ": " + str(answer))

