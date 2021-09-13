from typing import Dict, List, Set
import json

Data = List[Dict[str,str]]

class Twitter:
    datas:Data

    def __init__(self,fileName:str) -> None:
        self.readFile(fileName)

    def readFile(self,fileName:str) -> None:
        self.datas = json.loads(open(fileName).read().strip())

    def Menu01(self):
        print(len(self.datas))

    def Menu02(self) -> None:
        authors:Set[str] = set()
        for data in self.datas:
            authors.add(data['author'])
        print(len(authors))

    def Menu03(self) -> None:
        author_post:Dict[str,int] = {}
        for data in self.datas:
            try:
                author_post[data['author']]+=1
            except:
                author_post.update({data['author']:1})
        author_items = author_post.items()
        maxAuthor = max(author_items,key=lambda author:author[1])[1]
        for author in [author for author in author_items if author[1] == maxAuthor]:
            print(author[0])

    def Menu04(self) -> None:
        topics:Set[str] = set()
        for data in self.datas:
            topics.add(data['topic'])
        print(len(topics))

    def Menu05(self) -> None:
        length = 0
        for data in self.datas:
            length += 1 if data['topic_priority'] == 'ALERT' else 0
        print(length)

    def Menu06(self) -> None:
        length = 0
        for data in self.datas:
            length += 1 if data['topic_priority'] == 'UNIMPORTANT' else 0
        print(length)

    def Menu07(self) -> None:
        haveAnotherEn = False
        for data in self.datas:
            if data['language'] != 'EN':
                haveAnotherEn = True
                break
        print(haveAnotherEn)
                

    def Menu08(self) -> None:
        def countWord(data:Dict[str,str]) -> int:
            return len(data['text'].split())

        maxWord = max(self.datas,key=countWord)
        print(len(maxWord['text'].split()))

twitter = Twitter(input('File name: '))

Input = int(input('input: '))

if Input == 1:
    twitter.Menu01()
elif Input == 2:
    twitter.Menu02()
elif Input == 3:
    twitter.Menu03()
elif Input == 4:
    twitter.Menu04()
elif Input == 5:
    twitter.Menu05()
elif Input == 6:
    twitter.Menu06()
elif Input == 7:
    twitter.Menu07()
elif Input == 8:
    twitter.Menu08()