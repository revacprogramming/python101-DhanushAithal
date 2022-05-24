# Functions


def computepay(h, r):
    pay=hrs*rte
    if(hrs>40):
        Extra_pay=(hrs-40)*0.5*rte
        Final_pay= pay+Extra_pay
        return Final_pay



hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
