import re

print("inputFile  ", end = ':')
inName= input()
print("outputFile ", end = ':')
makeName= input()
inp = re.search(r'.*'+'.txt',inName)
if inp == None:
    inName += '.txt'
out = re.search(r'.*'+'.csv',makeName)
if out == None:
    makeName += '.csv'
with open(inName,'r',encoding="utf-16-le") as f:
    s = f.read()
s = s.replace(u'\ufeff','').replace(',','_')
slines = s.split('\n')
slines = [l.replace('\n','') for l in slines]
selements = []
for l in slines[:-1]:
    ll = str(l).split('\t')
    selements.append(ll)
print("使いたい項目を選択(何も選択しない場合トラックタイトル,アーティスト,コメントになります)")
print("入力例:コメント アーティスト トラックタイトル")
eld = {}
for l in range(1,len(selements[0])):
    print('|'+selements[0][l], end = '|')
    eld.setdefault(selements[0][l], l)
print()
line = ""
items = input().split(" ")
if items[0] == '':
    items = ['トラックタイトル', 'アーティスト', 'コメント']
with open(makeName,'w') as f:
    for l in selements:
        output = ''
        for it in items:
            output += l[int(eld.get(it))]+','
        output += '\n'
        f.writelines(output)
