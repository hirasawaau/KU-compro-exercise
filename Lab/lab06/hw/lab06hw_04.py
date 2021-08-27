from typing import List,Dict


class BookingInfo:
    def __init__(self,Str:str) -> None:
        # 00x541d aaaa -> bbbb 0 / 50
        arr1,arr2 = Str.split('->')
        self.id = arr1.split()[0]
        self.begin = arr1.split()[1]
        self.end = arr2.split()[0]
        self.remain = int(arr2.split()[1])
        self.maximum = int(arr2.split()[3])
        self.booking_people = []
        # self.index = index
        pass

    def AddBooking(self,person):
        if self.remain == self.maximum:
            raise ValueError('Fight is full')
        self.booking_people.append(person)
        self.remain+=1

    def PrintBooking(self):
        print(f'{self.id} is from {self.begin} to {self.end}, number of people booking is {self.remain}/{self.maximum}')

    # def FindBooking(self,name:str):
    #     self.booking_people.append(name)





booking_infos:Dict[str,BookingInfo] = {}

def findBookingByName(name:str):
    global booking_infos
    bookings = list(booking_infos.items())
    filtered_bookings = filter((lambda k:k[1].booking_people.count(name) >= 1 ),bookings)
    return list(filtered_bookings)


print('''Select menu :
1. add flight data
2. flight data by code
3. show all flight data
4. flight booking
5. show people flight data
6. exit''')

while True:
    menu = int(input('menu : '))
    if menu == 1:
        bookingInfo = BookingInfo(input('Add data : '))
        booking_infos.setdefault(bookingInfo.id,bookingInfo)
    elif menu == 2:
        bookingInfo = booking_infos[input('Enter code : ')]
        bookingInfo.PrintBooking()
    elif menu == 3:
        print('All flight data')
        for booking_info in booking_infos.values():
            booking_info.PrintBooking()
    elif menu == 4:
        name = input('Enter your name : ')
        flightCode = input('Enter flight code : ')
        try:
            booking_infos[flightCode].AddBooking(name)
            print('Success')
        except ValueError:
            print('The flight is full, Sorry')

    elif menu == 5:
        name = input('Enter your name : ')
        bookingInfos = findBookingByName(name)
        bookingInfos.reverse()
        print(f'{name} is booking flight code =',end=' ')
        for i in bookingInfos:
            print(i[0],end=' ')
        print()
    elif menu == 6:
        print('EXIT!!!!!!!!!!!!!!!')
        break