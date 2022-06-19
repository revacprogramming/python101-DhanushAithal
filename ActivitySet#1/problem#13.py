# Tuples
filename=input("Enter the filename:")
fopen=open(filename)
di_ct=dict()
lst=list()
count=0
for line in fopen:
  if line.startswith("From:"):
    continue
  if line.startswith("From"):
    line=line.split()
    time= line[5]
    hr= time[:2]#[0:2]
    di_ct[hr]=di_ct.get(hr,0)+1
lst=list(di_ct.items())
lst.sort()
for i in lst:
  print(i[0],i[1])