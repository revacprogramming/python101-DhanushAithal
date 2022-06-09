# Dictionaries

filename = "dataset/mbox-short.txt"

d=dict()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for i in handle:
    if i.startswith("From "):
        emails=i.split()
        email=emails[1]
        d[email]=d.get(email,0)+1
    else:
        continue
print(email,d[email])
