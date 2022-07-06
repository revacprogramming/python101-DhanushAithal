# Object Oriented Programming
# https://www.py4e.com/lessons/Objects
print('\033[1m _Oops_ \033[0m')
class student():
  def __init__(self,name,id,address):
   self.name=name
   self.id=id
   self.address=address
   print("\033[1m Student Information as Fallows \033[0m")
  def show(self):
  
   print("Name :",self.name,sep='')
   print("Id :",self.id,sep='')
   print('Address :',self.address)
  def __del__(self):
    print("Objects doesn't Exists!!")

a=student('Abhi','R21EF301','Banglore')
a.address="Delhi"
b=student('Balu','R21EF302','Chennai')
c=student('Chandan','R21EF303','Mumbai')

a.show()
b.show()
c.show()