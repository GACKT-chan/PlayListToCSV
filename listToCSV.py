import re

print("inputFileName OutputFileName")
inName,makeName = input().split(" ")
inp = re.search(r'.*'+'.txt',inName)
if inp == None:
    inName += '.txt'
out = re.search(r'.*'+'.csv',makeName)
if out == None:
    makeName += '.csv'
with open(inName,'r',encoding="utf-16-le") as f:
    s = f.read()
s = s.replace(u'\ufeff','')
slines = s.split('\n')
slines = [l.replace('\n','') for l in slines]
selements = []
for l in slines:
    ll = str(l).split('\t')
    selements.append(ll)
print("使いたい項目を選択(何も選択しない場合トラックタイトル,アーティスト,コメントになります)")
print("入力例:コメント アーティスト トラックタイトル")
eld = {}
for l in range(1,len(selements[0])):
    print('[' + selements[0][l], end = ']')
    eld.setdefault(selements[0][l], l)
print()
line = ""
items = input().split(" ")

if items[0] == '':
    items = ['トラックタイトル', 'アーティスト', 'コメント']
for l in selements:
    line += l[0]+','
    print(l[0], end = '\t')
    for j in items:
        i = int(eld.get(j))
        l[i] = l[i].replace(',','_')
        line += l[i]+','
        print(l[i], end = '\t')
    print()
    line = line[::-1]
    line = line.replace(',','',1)
    line = line[::-1]
    line += '\n'
with open(makeName,'w') as f:
    f.write(line)