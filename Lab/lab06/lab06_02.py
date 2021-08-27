dictionary = {
    "arm":{
        1:"n",
        2:"แขน"
    },
    "hello":{
        1:"v",
        2:"สวัสดี"
    },
    "beautiful":{
        1:"adj",
        2:"สวย"
    },
    "toilet":{
        1:"n",
        2:"ห้องน้ำ"
    },
    "kick":{
        1:"v",
        2:"เตะ"
    },
    "handsome":{
        1:"adj",
        2:"หล่อ"
    },
}

while True:
    word = input()
    if word == '0':
        break
    try:
        while True:
            dictionary[word]
            call = int(input())
            try:
                dictionary[word][call]
                print(dictionary[word][call])
                break
            except KeyError:
                print('Invalid option.')
                continue
    except KeyError:
        print('Word not in dictionary.')
    
