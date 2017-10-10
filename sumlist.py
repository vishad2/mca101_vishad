def listSum(lis):
    '''
    objective: to compute sum of members of a list entered by the user
    input parameters:
    
            ls=list of elements

    return value:computed sum value from listsum function
    variables:
            sum:used to store the elements
    '''
    '''
    approach:each value of the list is accessed using loop and sum is computed
    '''
    
    
    if len(lis)==0:
        return 0
    else:
        return lis[0] + listSum(lis[1:])
    
print(listSum([2,3,4,5]))
