fname = input("Enter file name: ")
fn = open(fname)
lst = []
for l in fn:
    #l = l.rstrip()
    l = l.split()
    for word in l:
    	if word not in lst:
        	lst.append(word)
print(sorted(lst))