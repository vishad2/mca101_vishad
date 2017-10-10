def calcperc(total,marksob):
    '''
    objective: to compute the percentage of marks
    input parameters:
        totmarks:total marks
        obtmarks:marks obtained by student
    approach: divide obtmarks by total marks and multiply by 100
    return value: percentage
    '''
    perc = (marksob/total)*100
    return perc
    
def main():
    '''
    objective: to compute the percentage of student
    user inputs:
       totmarks:total marks
        obtmarks:marks obtained by student
    approach: use function calcperc
    '''
    
    tot = int(input('enter total marks: '))
    marks = int(input('enter marks obtained by student: '))
    print('total marks: ', tot)
    print('marks obtained: ', marks)
    print('percentage computed is: ',calcperc(tot,marks),"%")
    print('End of output')
    
if __name__ == '__main__':
    main()
print('End of program')
