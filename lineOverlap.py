def isLineOverLap():
    x1, x2 = [int(x) for x in input('Enter the first line in this format (x1, x2): ').split(',')]
    x3, x4 = [int(x) for x in input('Enter the first line in this format (x1, x2): ').split(',')]
    if ((x1 < x3 and x2 > x3) or (x1 < x4 and x2 > x4)):
        print('this two lines overlap')
    else :
        print('this two lines do not overlap')

isLineOverLap()