def whichIsGreater():
    num1 = input("Please provide the first number: ")
    num2 = input("Please provide the the second number: ")

    if num1 > num2 :
        print(num1, " is greater than ", num2)
    elif num1 == num2 :
        print(num1, " is equal to ", num2)
    else : 
        print(num1, " is lesser than ", num2)

if __name__ == '__main__':
    whichIsGreater()

# USEAGE - cd via terminal to the folder where this file is placed. 
# run `python afolabi_tope_greater.py`