# recurcive function that returns two points on the x-axis
def getLine(n):
    if n < 1:
        print("no feasible line defined in this program")
        exit()
    numString = ["first", "second"] # you can scale this if you need more lines
    try :
        _x = [int(x) for x in input('Enter the ' + numString[n-1] + ' line in this format (x1, x2): ').split(',')]
        return _x[0], _x[1]
    except:
        print("line" + str(n) + " format error please try again: ")
        return getLine(n)

def isLineOverLap():
    #... you can always get as many lines as you want using getLine(n)
    # where n is int form 1, 2, 3, ...
    x1, x2 = getLine(1)
    x3, x4 = getLine(2)
    #check for overlap
    if ((x1 < x3 and x2 > x3) or (x1 < x4 and x2 > x4)):
        print('this two lines overlap')
    else :
        print('this two lines do not overlap')

if __name__ == '__main__':
    isLineOverLap()

# USEAGE - cd via terminal to the folder where this file is placed. 
# run `python afolabi_tope_lineOverlap.py`