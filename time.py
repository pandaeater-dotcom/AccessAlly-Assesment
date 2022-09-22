# f = open('j4.'+x+'.in', 'r')
# totalMins = int(f.readline())
# f_result = open('j4.'+x+'.out', 'r')
# commented code to read input and output from file

totalMins = int(input('Enter total number of minutes (as integer): '))
# command line input from user


def arithmeticSequence(hours, minutes):
    '''
    this function determines if a particular time is an arithmetic sequence

    12:34
    1: most significant hour (msh)
    2: least significant hour
    3: most significant minute
    4: least significant minute
    '''
    msm = minutes//10
    lsm = minutes % 10
    msh = hours//10
    lsh = hours % 10
    if hours < 10 and lsm - msm == msm - lsh:
        return True
    elif hours >= 10 and lsm - msm == msm - lsh and msm - lsh == lsh - msh:
        return True
    return False


def runTime(mins, hours=12, minutes=0, count=0):
    cycles = mins//720
    remainder = mins % 720
    remainderCount = 0
    if cycles > 0:
        mins = 720
    # split total mins into number of full 12hr 'cycles' and 'remainder'

    for i in range(mins+1):
        if arithmeticSequence(hours, minutes):
            count += 1
            if i <= remainder and cycles > 0:
                remainderCount += 1
            # we are counting for the full cycle and the remainder simultaneously
        if minutes == 59:
            minutes = 0
            if hours != 12:
                hours += 1
            else:
                hours = 1
        else:
            minutes += 1

    if cycles > 0:
        count *= cycles
    count += remainderCount
    return count

print('Total number of arithmetic sequences in given time: ', runTime(totalMins))
# print(runTime(totalMins) == int(f_result.readline()))
