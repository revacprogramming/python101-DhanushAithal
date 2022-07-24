import math

def distance(x,X,y,Y):
  dist= math.sqrt( ((X-x)**2) - ((Y-y)**2))
  return dist
def main():
 x1,x2,x3,y1,y2,y3=input("x1:"),input("x2:"),input("x3:"),input("y1:"),input("y2:"),input("y3:")
 x1,x2,x3=float(x1),float(x2),float(x3)
 y1,y2,y3=float(y1),float(y2),float(y3)

 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f) is " %(x1,y1,x2,y2),distance(x1,x2,y1,y2))
 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f)is "%(x2,y2,x3,y3),distance(x2,x3,y2,y3))
 print("Area of rectangle with vertices(%.2f,%.2f),(%.2f,%.2f),(%.2f,%.2f) is "%(x3,y3,x1,y1),distance(x3,x1,y3,y1))
    
main()