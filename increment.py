def increment(number):
    '''
    objective: to increment a given number.
    input parameters:
        number:number whose increment is to be calculated
    return value:incremented value is returned
    '''
    return number+1
def main():
    '''
    objective:increment value of number
    user inputs:
        num:number to be incremented
    '''
    num=int(input("Enter a number "))
    print('Incremented value of number is',(increment(num)))

if __name__=='__main__':
    main()
