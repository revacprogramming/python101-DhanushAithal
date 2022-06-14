import re
sum=0
file_name=input("Enter the file name to open:")
file_open=open(file_name)
for line in file_open:
  line=line.strip()
  find_num=re.findall('[0-9]+',line)
  #find_num=re.findall('\d+',line)
  for num in find_num:
    y=float(num)
    sum+=y
print(sum)
