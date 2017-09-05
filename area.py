def areaRectangle(length,breadth):
    '''
    objective: to calculate area of a rectangle
    approach: multiplying user input length and breadth
    parameters: -> length: length of the rectangle
                -> breadth: breadth of the rectangle
    return value: area of the rectangle
    '''
    area = length * breadth
    return area

def areaSquare(side):
    '''
    objective: to calculate area of a square
    approach: invoke function areaRectangle with both arguments as side 
    parameters: -> side: side of square
    '''
    areaRectangle(side,side)

def main():
    '''
    objective: to calculate area of a rectangle
    approach: taking length and breadth of rectangle from user and passing as arguments to the 	function areaRectangle
    '''
    
    length = float(input('Enter length of the Rectangle: '))
    breadth = float(input('Enter breadth of the Rectangle: '))
    area = areaRectangle(length, breadth)
    if (length==breadth):
        side=length
        print('Side of Square is: ', side)
        
        print('Area of Square: ', area)
        area = areaSquare(side)
    else:
        print('Length of Rectangle: ', length)
        print('Breadth of Rectangle: ', breadth)
        area = areaRectangle(length, breadth)
        print('Area of Rectangle: ', area)
    
    print('End of main.')
    
if (__name__=='__main__'):
    main()
