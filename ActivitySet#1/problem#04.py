hrs = float(input("Enter Hours:"))
h = float(hrs)
rate= float(input("Enter rate :"))
r=float(rate)
Pay=h*r
if(h>40):
    Extra_pay=(h-40)*0.5*r
    Final_pay=Pay+Extra_pay
    print(Final_pay)