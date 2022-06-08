name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
    word_split = line.split()
if "From" in word_split:
    email = word_split[1]
dic[email] = dic.get(email,0) + 1
holder =0
key_result =None
value_result =None
for key,value in dic.items():
    if value > holder:
        holder =value
key_result =key
value_result =value
print(key_result , value_result)