# f = open('s4.1.in', 'r')
# f_result = open('s4.1.out', 'r')
# bloodAvailable, bloodNeeded = f.readline().split(), f.readline().split()
# bloodAvailable = [int(x) for x in bloodAvailable]
# bloodNeeded = [int(x) for x in bloodNeeded]
# code to accept input and output from files above

bloodAvailable = [int(x) for x in input('Enter blood supply list (single space between numbers): ').strip().split(' ')]
bloodNeeded = [int(x) for x in input('Enter patient list (single space between numbers): ').strip().split(' ')]

total = 0

def minimize(blood, patients):
    '''
    Calculates how much blood can be given, returns and amount and subtracts it from both lists
    '''
    minimum = min(bloodAvailable[blood], bloodNeeded[patients])
    bloodAvailable[blood] -= minimum
    bloodNeeded[patients] -= minimum
    return minimum

x = 0
# x is the iterator
while x < len(bloodAvailable):
    total += minimize(x, x)
    x += 2
x = 1
# the Rh- blood types are given to the patients and the corresponding number subtracted from both lists
while x < len(bloodAvailable):
    total += minimize(x, x) + minimize(x-1, x)
    x += 2
# the Rh+ blood types are given to the patients and leftover Rh- of same type are given

if bloodNeeded[6] > 0:
    total += minimize(2, 6) + minimize(4, 6)
# if AB- patients are lefover, excess A- and B- blood is given

if bloodNeeded[7] > 0:
    total += minimize(3, 7) + minimize(5, 7) + minimize(2, 7) + minimize(4, 7)
# then if AB+ patients are leftover, excess A+, B+, A- and B- blood is given

x = 3
while x < len(bloodAvailable):
    total += minimize(1, x)
    x += 2
# excess O+ is given to all remaining Rh+ patients
x = 2
while x < len(bloodAvailable):
    total += minimize(0, x)
    x += 1
# excess O- is given to all remaining Rh- and Rh+ patients

print('Maximum number of patients that can receive blood is: ', total)
# print(total == int(f_result.readline()))


'''
This algorithm operates at O(n) time complexity. It takes two sets of 8 integers as input for the blood available and patients. 
First, corresponding blood types are matched and blood is donated, after which any excess Rh+ patients are given the respective Rh- blood from any surplus
Then we consider the edge cases of AB- and AB+. First any excess AB- is given blood from surplus A- and B-
Then excess AB+ is given blood from A-, B-, A+ and B+
The second to last step is donating surplus O+ blood to any remaining Rh+ patients
Finally, any surplus O- blood is donated to any remaining patients
'''
