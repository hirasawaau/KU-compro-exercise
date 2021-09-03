from typing import List


class Decoder:

    def __init__(self , public:str,private:str) -> None:
        self.public = Decoder.__read(public).split('\n')
        self.private = Decoder.__read(private).split('\n')
    
    def decode(self):
        results = []
        for index,public in enumerate(self.public):
            _results = []
            publicASCII = [ord(p) for p in public]
            privateASCII = [ord(p) for p in self.private[index]]

            for _index,key in enumerate(publicASCII):
                _results.append(self.__decrypt(key,privateASCII[_index],index))
            
            results.append(''.join(_results))

        return results
            
    def __beginPrivate(self,index) -> str:
        return self.private[index][0]

    
    def __decrypt(self,public:int,private:int,index:int) -> str:
        result = (public + private) % 26   
        return chr(97+result) if Decoder.isInt(self.__beginPrivate(index)) else chr(65+result) 

    @staticmethod
    def isInt(r:str) -> bool:
        try:
            int(r)
            return True
        except:
            return False

    @staticmethod
    def __read(path) -> str:
        with open(path) as file:
            return file.read().strip()
    


publicFile = input('Enter publickey filename : ')
privateFile = input('Enter privatekey filename : ')

decoder = Decoder(publicFile,privateFile)
st = decoder.decode()

for i in st:
    print(i)