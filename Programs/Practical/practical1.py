def triangle(side1=float(input('1st side ')),side2=float(input('2nd side ')),side3=float(input('3rd side '))) :
     assert side1+side2>side3 and side2+side3>side1 and side1+side3>side2
     par = side1+side2+side3
     s = par/2
     area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
     return tuple([area,par])

print("(Area,Perimeter) : ",triangle())
    
