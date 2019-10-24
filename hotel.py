from time import sleep
class room():
    def __init__(self):
        self.dates={'1.10.2019':0, '2.10.2019':0, '3.10.2019':0, '4.10.2019':0, '5.10.2019':0, '6.10.2019':0, '7.10.2019':0}
    ## מראה את כל התאריכים שקיימים
    def alldates(self):
        for x in self.dates:
            print(str(x) + " : " + str(self.dates[x]))
    ##מראה את התאריכים הפנויים רק
    def freeroom(self):
        for x in self.dates:
            if self.dates[x]==0:
                print(x)
    ##בודק שהתאריך שבחר זה לא שבת או שישי
    def friday_saturday(self, date3):
        count3=1
        for i in self.dates:
            if i == date3:
                break
            count3=count3+1
        if count3%5==0 or count3%6==0:
            return True
        else:
            return False
    ##בודק אם התאריכים שבח פנויים או לא
    def if_the_room_free(self, date, day):
        count=0
        for x in self.dates:
            if x == date:
                break
            count = count + 1

        for y in range(int(day)):
            if self.dates[list(self.dates)[count]]!= 0:
                return False
            else:
                count = count + 1
        return True
    ##מבצע הזמנה ושומר את השם וסכום ההזמנה
    def invitation(self, date2, day2, alotheder, invitnumber):
        count2=0
        for x in self.dates:
            if x == date2:
                break
            count2 = count2 + 1
        name=input("enter your full name : ")
        for y in range(int(day2)):
            self.sum=(float(alotheder)*float(day2)*1.17)
            self.dates[list(self.dates)[count2]]=[name, self.sum, invitnumber]
            count2=count2+1

    def cancel_room(self, date, day, name, invitnumber):
        count=0
        tf=0
        for i in self.dates:
            if i==date:
                for y in range(int(day)):
                    if self.dates[list(self.dates)[count]][0] == name and self.dates[list(self.dates)[count]][2] == int(invitnumber):
                        self.dates[list(self.dates)[count]] = 0

                        tf=1
                    count = count + 1
            count=count+1

        if tf==1:
            return True
        else:
            return False

    def exist_invit(self, date, day, name, invitnumber):
        count=0
        tf=0
        for i in self.dates:
            if i==date:
                for y in range(int(day)):
                    if self.dates[list(self.dates)[count]][0] == name and self.dates[list(self.dates)[count]][2] == int(invitnumber):
                        tf=1
                    count = count + 1
            count=count+1

        if tf==1:
            return True
        else:
            return False

def menu():
    sleep(2)
    print("welcome to our hotel")
    print("to see all the free date press 1")
    print("to see if the dates you want is clear press 2")
    print("to do invitation press 3")
    print("to cancel your invitation press 4")
    print("to enter admin mode enter 6")

##main
roomzog1=room()
roomzog2=room()
roomshalosh1=room()
roomshalosh2=room()
bol=0
invitnumber=0
while bol==0:
    menu()
    num=int(input(""))
    if num==1:
        print("for room number 1 for 2 adults:")
        roomzog1.freeroom()
        print("for room number 2 for 2 adults:")
        roomzog2.freeroom()
        print("for room number 1 for 3 adults:")
        roomshalosh1.freeroom()
        print("for room number 2 for 3 adults:")
        roomshalosh2.freeroom()
    elif num==2:
        date=input("enter the date you want to check")
        day=input("enter how much days you want to rent")
        adult=int(input("enter how much adults you want in the room"))
        if adult==2:
            if roomzog1.if_the_room_free(date, day)==True:
                print("room zog number 1 is free for that's dates")
            else:
                print("room zog number 1 is not free for that's dates")
            if roomzog2.if_the_room_free(date, day)==True:
                print("room zog number 2 is free for that's dates")
            else:
                print("room zog number 2 is not free for that's dates")
        if adult==3:
            if roomshalosh1.if_the_room_free(date, day)==True:
                print("the room shalosh number 1 is free for that's dates")
            else:
                print("the room shalosh number 1 is not free for that's dates")
            if roomshalosh2.if_the_room_free(date, day)==True:
                print("the room shalosh number 2 is free for that's dates")
            else:
                print("the room shalosh number 2 is not free for that's dates")
    elif num==3:
        print("room for 2 adults cost 300$ for every day")
        print("room for 3 adults cost 400$ for every day")
        date2 = input("enter the date you want to rent")
        day2 = input("enter how much days you want to rent")
        adult2=int(input("enter how much adults you want in the room"))
        if adult2==2:
            alot='300'
            if roomzog1.if_the_room_free(date2, day2)==True:
                if roomzog1.friday_saturday(date2)==False:
                    roomzog1.invitation(date2, day2, alot, invitnumber)
                    print("the cost for the room number 1: " + str(roomzog1.sum))
                    print("your invitation number : " + str(invitnumber))
                    invitnumber = invitnumber + 1
                else:
                    print("we are not rent room on since friday and saturday")

            elif roomzog2.if_the_room_free(date2, day2)==True:
                if roomzog2.friday_saturday(date2)==False:
                    roomzog2.invitation(date2, day2, alot, invitnumber)
                    print("the cost for the room number 2 : " + str(roomzog2.sum))
                    print("your invitation number : " + str(invitnumber))
                    invitnumber = invitnumber + 1
                else:
                    print("we are not rent room on since friday and saturday")
            else:
                print("all the dates you choose for 2 adults are not free")
        elif adult2==3:
            alot=400
            if roomshalosh1.if_the_room_free(date2, day2)==True:
                if roomzog2.friday_saturday(date2)==False:
                    roomshalosh1.invitation(date2, day2, alot, invitnumber)
                    print("the cost for the room number 1 : " + str(roomshalosh1.sum))
                    print("your invitation number : " + str(invitnumber))
                    invitnumber = invitnumber + 1
                else:
                    print("we are not rent room on since friday and saturday")
            elif roomshalosh2.if_the_room_free(date2, day2)==True:
                if roomshalosh2.friday_saturday(date2)==False:
                    roomshalosh2.invitation(date2, day2, alot, invitnumber)
                    print("the cost for the room number 2 : " + str(roomshalosh2.sum))
                    print("your invitation number : " + str(invitnumber))
                    invitnumber = invitnumber + 1
                else:
                    print("we are not rent room on since friday and saturday")

            else:
                print("all the dates you choose for 3 adults are not free")

    elif num==4:
        date=input("insert your invitation date")
        day=input("insert how much day you invite")
        name=input("insert your full name")
        invit=input("inser your invitation number")
        if roomzog1.cancel_room(date, day, name, invit)==True:
            print("your invitation canceled")
            print("you need to pay ticket for : " +str(roomzog1.sum*0.1) +" $")
        elif roomzog2.cancel_room(date, day, name, invit)==True:
            print("your invitation canceled")
            print("you need to pay ticket for : " + str(roomzog2.sum * 0.1) + " $")
        elif roomshalosh1.cancel_room(date, day, name, invit)==True:
            print("your invitation canceled")
            print("you need to pay ticket for : " + str(roomshalosh1.sum * 0.1) + " $")
        elif roomshalosh2.cancel_room(date, day, name, invit)==True:
            print("your invitation canceled")
            print("you need to pay ticket for : " + str(roomshalosh2.sum * 0.1) + " $")
        else:
            print("wrong name, invitation number or date")

    elif num==5:
        date=input("insert your invitation date")
        day=input("insert how much day you invite")
        name=input("insert your full name")
        invit2=input("insert your invitation number")
        if roomzog1.exist_invit(date, day, name, invit2) == True:
            print("the invitation exist in room 1 for 2 adults")
        elif roomzog2.exist_invit(date, day, name, invit2) == True:
            print("the invitation exist in room 2 for 2 adults")
        elif roomshalosh1.exist_invit(date, day, name, invit2) == True:
            print("the invitation exist in room 1 for 3 adults")
        elif roomshalosh2.exist_invit(date, day, name, invit2) == True:
            print("the invitation exist in room 2 for 3 adults")


    elif num==6:
        if input("enter password")=='112233':
            print("##all the dates with name + sum##")
            print("room zog num 1 : ")
            roomzog1.alldates()
            print("room zog num 2 :")
            roomzog2.alldates()
            print("room shalosh num 1 : ")
            roomshalosh1.alldates()
            print("room shalosh num 2 : ")
            roomshalosh2.alldates()


# dates = {'1.10.2019': 0, '2.10.2019': 2, '3.10.2019': 0, '4.10.2019': 0, '5.10.2019': 0, '6.10.2019': 0,
#               '7.10.2019': 0}
# print(dates)
# nn='2.10.2019'
# dates[list(dates)[1]]=['amit', 2000]
# print(dates)


# dd='2.10.2019'
# print(list(dates)[0])
# # print(dates[dd])
# print(dates[list(dates)[0]])
# # if dates[list(dates)[0]]==0:
# #     print("yes")
# # else:
# #     print("no")
#
#
#
# print("----")
# count=0
# print(count)
# for x in dates:
#     if x==dd:
#         print("sss")
#         break
#     count=count+1
# for y in range(3):
#     if dates[list(dates)[count]]==0:
#         print("yes")
#         count=count+1
#     else:
#         print("no")
#         count=count+1

#a
