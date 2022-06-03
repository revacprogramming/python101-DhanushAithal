file = open("mbox-short.txt")
count = 0
for l in file:
    if (l.startswith("From:")):
        adr = l.split(" ")[1]
        print(adr.rstrip())
        count += 1
print("There were", count, "lines in the file with From as the first word")