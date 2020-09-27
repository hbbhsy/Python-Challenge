import re

file=open('regex.txt')
sum=0
count=0
for line in file:
    line=re.findall('[0-9]+',line)
    if len(line)>0:
        count+=len(line)
        for num in line:
            sum+=int(num)
print(sum)
