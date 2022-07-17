

print(" Menu List ".center(40,'*'))
print('_'*34)
print('Item'+'->'+'Rate')
class Menu(dict):
  """fill in class definition here"""
  def __init__(self):
    self=dict()
    '''  self.item=item
    self.rate=rate'''
  def add(self,item,rate):
    self[item]=rate
    
  def show(self):
    for i,j in self.items():
     print(i,'->',j)

m=Menu()
m.add("Idly",20)
m.add("Vada",10)
m.add("Dosa",25)
m.add("Poori",30)

m.show()
'''poori.show()
idly.show()
vada.show()
dosa.show()
