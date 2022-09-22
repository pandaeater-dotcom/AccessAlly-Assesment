# f = open('j4.14.in', 'r')
# totalMins = int(f.readline())
# f_result = open('j4.14.out', 'r')
# commented code to read input and output from file

totalMins = int(input('Enter total number of minutes (as integer): '))
# command line input from user


def arithmeticSequence(hours, minutes):
    '''
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
    if hours < 10:
        if lsm - msm == msm - lsh:
            return True
    else:
        if lsm - msm == msm - lsh\
                and msm - lsh == lsh - msh:
            return True
    return False


def runTime(mins, hours=12, minutes=0, count=0):
    cycles = mins//720
    remainder = mins % 720
    if cycles > 0:
        mins = 720
    # split total mins into number of full 12hr 'cycles' and 'remainder'

    for i in range(mins):
        if arithmeticSequence(hours, minutes):
            count += 1
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
    if cycles > 0 and remainder > 0:
        return count + runTime(remainder)
    # function runs again if there is a remainder
    return count


print(runTime(totalMins))
# print(runTime(totalMins) == int(f_result.readline()))
