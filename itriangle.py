def iTriangle(s):
    '''
    Objective : print isosceles triangle.
   
    Approach : using print commands to draw isosceles triangle
    Input Parameters : s:s is the symbol entered by user    
    '''
    print("   ",s,"   ")
    print("  ",s,s,"  ")
    print(" ",s,s,s," ")
    print("",s,s,s,s,"")
    
def main():
    '''
    Objective : To draw isosceles triangle.
    Approach : Use of iTriangle function.
    User input:sym:sym is symbol entered by user
    '''
    print("End the symbol for triangle")
    sym=input()
    iTriangle(sym)
    
if __name__=="__main__":
    main()
    print("End of program!")
