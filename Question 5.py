#I Have tried but not able to solve

import re
data = """
INDIA
Runs: 231, Wickets: 5, Overs: 50
ENGLAND
Runs: 187, Wickets: 10, Overs: 47
BANGLADESH
Runs: 220, Wickets: 8, Overs: 50
AUSTRALIA
Runs: 250, Wickets: 9, Overs: 50
"""
result={}
step1=step2=step3=''
lines=data.split('\n')

for line in lines:
    if re.search(r'^(\w+):$',line,re.M):
        out=re.search(r'^(\w+):$',line,re.M)
        step1=out.group(1)
        result[step1]={}
    if re.search(r'^\s{4}(\w+):$',line,re.M):
        out=re.search(r'^\s{4}(\w+):$',line,re.M)
        step2=out.group(1)
        result[step1][step2]={}
    if re.search(r'^\s{8}(\w+)$',line,re.M):
        out=re.search(r'^\s{8}(\w+)$',line,re.M)
        item1=out.group(1)
        if not result[step1][step2]:
            result[step1][step2]=[item1]
        else:
            result[step1][step2].append(item1)

print(result)
