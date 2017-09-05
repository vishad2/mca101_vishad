def areaTriangle(base, height):
    '''
    objective: To find the area of a Triangle
    input parameters:
    base of triangle
    height of triangle
    approach: using the formula (base*height)/2
    return value: area of triangle
    '''
    area = (base * height)/2
    return area

def main():
    base = float(input('Base of triangle: '))
    height = float(input('Height of triangle: '))
    area = areaTriangle(base, height)
    print('Base of triangle is: ', base)
    print('Height of triangle is: ', height)
    print('Area of triangle is: ', area)

if (__name__=='__main__'):
    main()
