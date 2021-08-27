with open('midTermScore_grp01.csv') as file:
    rawDatas = file.read().strip().split('\n')

datas = [dict(zip(rawDatas[0].split(','),rawData.split(','))) for rawData in rawDatas[1:]]
cleanDatas = [data for data in datas if data['Test name'] == '01204111 Midterm Examination 2564-1']

student = len(cleanDatas)
maxScore = int(max(cleanDatas,key=lambda r:int(r['Score']))['Score'])
avgScore = sum([int(data['Score']) for data in cleanDatas])/student
minScore = int(min(cleanDatas,key=lambda r:int(r['Score']))['Score'])

stdScore = (sum([(int(data['Score'])-avgScore)**2 for data in cleanDatas])/student)**0.5

print(student)
print(f'{maxScore} {avgScore:.2f} {stdScore:.2f} {minScore}')

A,Bp,B,Cp,C,Dp,D,F = 0,0,0,0,0,0,0,0

for data in cleanDatas:
    percentage = float(data['Percentage'])
    if percentage > 85:
        A+=1
    elif percentage > 79:
        Bp+=1
    elif percentage > 73:
        B+=1
    elif percentage > 67:
        Cp+=1
    elif percentage > 60:
        C+=1
    elif percentage > 50:
        Dp+=1
    elif percentage > 40:
        D+=1
    else:
        F+=1

print(f'''A: {A}
B+: {Bp}
B: {B}
C+: {Cp}
C: {C}
D+: {Dp}
D: {D}
F: {F}''')