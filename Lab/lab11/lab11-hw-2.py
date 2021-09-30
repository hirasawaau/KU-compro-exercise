def hash(*s):
    if ord(s[0]) >= ord(s[1]):
        return ord(s[1]) + 10
    else:
        return ord(s[0]) - 7

def isPhotobook(s:str):
    global isPhoto
    isPhoto = s[0].isalpha() and s[-1].isalpha()
    return isPhoto

def calKey(s:str):
    return sum([hash(s[i],s[i+1]) for i in range(len(s) - 1)])

def isPhotobookGenuine(key:int):
    if not isPhoto:
        return 'Incorrect Type'
    return key%2 == 0

def isAlbumGenuine(key:int):
    if isPhoto:
        return 'Incorrect Type'
    return key%2 == 1

def solve():
    n = int(input())
    ids = [input() for i in range(n)]

    real_photo_book = 0
    fake_album = 0  
    for id in ids:
        print(id)
        isPhotobook(id)
        key = calKey(id)
        
        if isPhoto:
            if isPhotobookGenuine(key):
                real_photo_book+=1
        else:
            if isAlbumGenuine(key):
                fake_album+=1
    
    print(real_photo_book)
    print(fake_album)

solve()