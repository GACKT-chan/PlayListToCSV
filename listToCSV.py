#!/usr/local/bin/python3
# coding: utf-8
print("inputFileName OutputFileName")
inName,makeName = input().split(" ")
with open(inName,'r',encoding="utf-16-le") as f:
    s = f.read()
s = s.replace(u'\ufeff','')
slines = s.split('\n')
slines = [l.replace('\n','') for l in slines]
selements = []
for l in slines:
    ll = str(l).split('\t')
    selements.append(ll)
print("使いたい項目を選択")
print("例:BPM　アーティスト　トラックタイトル")
eld = {}
for l in range(1,len(selements[0])):
    print(selements[0][l], end = '\t')
    eld.setdefault(selements[0][l], l)
print()
print(eld)
line = ""
items = input().split(" ")
for l in selements:
    line += l[0]+','
    for j in items:
        i = int(eld.get(str(j)))
        l[i] = l[i].replace(',','_')
        line += l[i]+','
    line += '\n'

print(line)

with open(makeName,'w') as f:
    f.write(line)