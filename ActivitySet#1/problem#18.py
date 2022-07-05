import re
count = 0
hand = open("regex_sum_1548641.txt.opdownload")
lines = hand.read()
match =  re.findall('[0-9]+',lines)
for i in match:
	number = int(i)
	count = count + number
print(count)