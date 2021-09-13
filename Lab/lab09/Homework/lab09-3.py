import json
from typing import Dict, KeysView, List, Tuple

Data = List[Dict[str,str]]

class Amazon:
    datas:Data = []

    def __init__(self,fileName:str) -> None:
        self.readFile(fileName)

    def readFile(self,fileName:str) -> None:
        with open(fileName) as files:
            for file in files:
                data = json.loads(file)
                self.datas.append(data)
    
    def Menu01(self):
        print(len(self.datas))

    def Menu02(self):
        reviewer = set()
        for data in self.datas:
            reviewer.add(data['reviewerID'])
        print(len(reviewer))

    def Menu03(self):
        products = set()
        for data in self.datas:
            products.add(data['productID'])
        print(len(products))

    def Menu04(self):
        mainCategories = set()
        # Electronics > Accessories & Supplies > Audio & Video Accessories > TV Accessories & Parts > TV Ceiling & Wall Mounts
        for data in self.datas:
            mainCategory = data['category'].split('>')[0]
            mainCategories.add(mainCategory)

        print(len(mainCategories))

    def Menu05(self):
        sub1Categories = set()
        # Electronics > Accessories & Supplies > Audio & Video Accessories > TV Accessories & Parts > TV Ceiling & Wall Mounts
        for data in self.datas:
            subCategory = data['category'].split('>')[1]
            sub1Categories.add(subCategory)

        print(len(sub1Categories))

    def Menu06(self):
        reviewerDict: Dict[str,int] = {}
        for data in self.datas:
            try:
                reviewerDict[data['reviewerID']]+=1
            except:
                reviewerDict.update({data['reviewerID']:1})
        
        maxReviewer = max(reviewerDict.items(),key=lambda data:data[1])
        print(maxReviewer[0])

    def Menu07(self):
        productDict:Dict[str,List[float]] = {}

        for data in self.datas:
            try:
                productDict[data['productName']].append(data['overall'])
            except:
                productDict.update({data['productName']:[data['overall']]})

        productAvg:Dict[str,Tuple[float,int]] = {}

        for product in productDict.items():
            productAvg.update({product[0] : (sum(product[1]) / len(product[1]),len(product[1]))})
        
        maxAvg = max(productAvg.items(),key=lambda data:data[1][0])
        # print(maxAvg)
        sortedData = sorted(list(filter(lambda data:data[1][0] == maxAvg[1][0],productAvg.items())) , key=lambda data:data[1][1] , reverse=True)
        print(sortedData[0][0])
        # for data in sortedData:
        #     print(data[0])
        #     break

    def Menu08(self):
        texts:Dict[str,list[int]] = {}
        for data in self.datas:
            try:
                texts[data['productName']].append(len(data['reviewText'].split(' ')))
            except KeyError:
                texts.update({data['productName']:[len(data['reviewText'].split(' '))]})
        
        maxReviewWord = max(texts.items(),key=lambda data:sum(data[1]) / len(data[1]))
        print(maxReviewWord[0])

amazon = Amazon(input('file name: '))
i = input('input: ')

if i == '1':
    amazon.Menu01()
elif i == '2':
    amazon.Menu02()
elif i == '3':
    amazon.Menu03()
elif i == '4':
    amazon.Menu04()
elif i == '5':
    amazon.Menu05()
elif i == '6':
    amazon.Menu06()
elif i == '7':
    amazon.Menu07()
elif i == '8':
    amazon.Menu08()
            
