class Pantip:
    def __init__(self,fileName:str) -> None:
        self.fileName = fileName

    def read(self):
        with open(self.fileName) as file:
            rawData = file.read().split('\n')

        self.rawData = rawData
        return self

    def lineLength(self):
        return len(self.rawData) 

    def mapData(self):
        header = self.rawData[0].split(',')
        self.data = [dict(zip(header,[int(i) for i in rawData.split(',')[1:-1]] + [rawData.split(',')[-1]])) for rawData in self.rawData[1:]]
        return self

    def findMaxRead(self):
        caches = dict(zip([key for key in self.data[0].keys()] , [0 for key in self.data[0].keys()]))
        for data in self.data:
            items = data.items()
            for key,value in items:
                caches[key]+=value
        return max(caches.items(),key=lambda data:data[1])[0]
    
    def sortTopThreeBluePlanet(self):
        caches = sorted(self.data,key=lambda data:data['blueplanet'],reverse=True)
        return caches[0:3]

    def findMaxAllUser(self):
        def SumDict(d):
            items = d.values()[:-1]
            return (d['uid'],sum(items))

        caches = list(map(SumDict,self.data))

        return max(caches,key=lambda F:F[1])

    def findMaxTvShowUser(self):
        return max(self.data, lambda R:R['tvshow'])
    
    def FindKoreaMoreThan500(self) -> int:
        def KoreaDict(d):
            return (d['uid'],d['korea'])

        caches = list(map(KoreaDict,self.data))

        return len(list(filter(lambda D:D[1] >= 500,caches)))

    def FindSiamMoreThanFood(self) -> int:
        return len(list(filter(lambda D:D['siam'] > D['food'],self.data)))

    def FindMaxRajdumnernProportion(self):
        def SumDict(d):
            items = d.values()[:-1]
            return (d['uid'],d['rajdumnern']/sum(items))

        caches = list(map(SumDict,self.data))
        return max(caches,key=lambda R:R[1])

    def FindMoreThan70PercentProportion(self):
        def SumDict(d):
            items = d.values()[:-1]
            return (d['uid'],sum(items))

        def TopTwoDict(d):
            items = d.values()[:-1]
            items.sort(reverse=True)
            return {d['uid']:sum(items[0:1])}

        Sum = list(map(SumDict,self.data))
        TopTwo = dict(map(TopTwoDict,self.data))
        users = [key for key,value in Sum if TopTwo[key] > value*0.7]
        
        return len(users)
    
    def NoPantip(self):
        users = list(filter(lambda R:R['pantip'] == 0,self.data))
        return len(users)
                

fileName = input('File name: ')

pantip = Pantip(fileName)
pantip.read().mapData()

n = print('enter number: ')

if n == '1':
    length = pantip.lineLength()
    print(length)
elif n == '2':
    room = pantip.findMaxRead()
    print(room)
elif n == '3':
    users = pantip.sortTopThreeBluePlanet()
    print(users[0]['uid'],users[1]['uid'],users[2]['uid'],sep=' ')
elif n == '4':
    user = pantip.findMaxAllUser()
    print(user[0] , user[1])
elif n == '5':
    user = pantip.findMaxTvShowUser()
    print(user[0],user[1])
elif n == '6':
    users = pantip.FindKoreaMoreThan500()
    print(users)
elif n == '7':
    users = pantip.FindSiamMoreThanFood()
    print(users)
elif n == '8':
    user = pantip.FindMaxRajdumnernProportion()
    print(user[0],user[1],sep=" ")
elif n == '9':
    user = pantip.FindMoreThan70PercentProportion()
    print(user)
elif n == '10':
    user = pantip.NoPantip()
    print(user)
else:
    pass



    
        
        

        
