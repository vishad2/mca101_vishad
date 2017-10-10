def increment(number):
    '''
    objective: to increment a given number.
    input parameters:
        number:number whose increment is to be calculated
    return value:incremented value is returned
    '''
    return number+1
def addnos(n1,n2):
    '''
    objective:compute sum of two numbers
    user inputs:
        num1:first number
        num2:second number
        return value:sum of two numbers
    '''
    '''
    approach:recursively call increment function
    '''
    if n2==0:
        return n1
    else:
        return (addnos(increment(n1),n2-1))
