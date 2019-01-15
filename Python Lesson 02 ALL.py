#Εγκατάσταση του PYGAME


#Βρισκω την directory της python
#Παω στην cmd και παταω cd και κανω paste την directory της python
#(π.χ C:\Users\NIKOS\AppData\Local\Programs\Python\Python37-32)
#Μου βγαζει την dir
#Γράφω pip install wheel
#Πατάω Enter και περιμενω λιγο (Βγαζει κατι πορτοκαλι γράμματα και τελειωνει)
#Γράφω pip intall pygame (Βγαζει κατι οτι κανει downloading και κατι πορτοκαλι γράμματα)
#Αφου τελειώσει παω στην dir της Python -->Lib-->site-packages-->pygame-->examples
#Εκει εχει όλα τα παιχνίδια κ.α.


#1 IF...ELSE Statement

Age=int(input("How old are you ? "))
if Age>31:
    print("You are older than me !!!")
else:
    print("You are younger than me !!!")


Name=input("What's your name ? ")
if (len(Name)<5):
    print("You have a short name !!!")
else:
    print("You don't have a short name !!!")


Age=int(input("How old are you ? "))
if (13<=Age<=19):
    print("You are a teenager !!!")
else:
    print("You are not a teenager !!!")


Age=int(input("How old are you ? "))
if (Age>=13 and Age<=19):
    print("You are a teenager !!!")
else:
    print("You are not a teenager !!!")


Age=int(input("How old are you ? "))
if (Age>=13):
    if (Age<=19):
        print("You are a teenager")
    else:
        print("You are too old to be a teenager !!!")
else:
    print("You are too young !!!")


Number=int(input("Type one integer : "))
if Number<0:
    print("Negative")
elif Number==0:
    print("Not Negative nor Positive")
else:
    print("Positive")

#Αυτη δεν λειτουργεί διοτι τα υποσυνολα που δηλωνονται δεν επικαλυπτονται
Number=int(input("Type one integer : "))
if (Number>0):
    print("P")
    if (Number==0):
        print("Not Negative nor Positive")
    else:
        print("N")
else:
    print("N")



#2 FOR LOOP

answer=""
for i in range(10):
    answer=answer+"*"
print(answer)


answer=""
for i in range(15):
    answer=answer+"*"
print(answer)




Num=""
for i in range(20):
    Num=Num+"@"
print(Num)

list=[]
x=15
for i in range(15):
    list.insert(0,x)
    x=int(x)-1
print(list)
    
#Το append τα βαζει στο τέλος αντι για την αρχή
list=[]
for i in range(15):
    list.append(i+1)
print(list)


list=[]
x=20
for i in range(20):
    list.insert(0,x)
    x=int(x)-1
print(list)

#Το append τα βαζει στο τέλος αντι για την αρχή
list=[]
for i in range(20):
    list.append(i+1)
print(list)


#for i in range(start, stop, step)
list=[]
for i in range(20,300,50):
    list.append(i)
print(list)


list=[]
for i in range(10,100,10):
    list.append(10*i+10)
print(list)




#3 WHILE LOOP

x=10
while int(x)>0:
    print(x)
    x=x-1

    
x=3000
while int(x)>0.5:
    print(x)
    x=x/2

list=[]
x=100
while int(x)>=0:
    list.insert(0,x)
    x=x-5
print(list)


#Το append τα βαζει στο τέλος αντι για την αρχή
list=[]
x=0
while int(x)<=100:
    list.append(x)
    x=x+5
print(list)


#Το append τα βαζει στο τέλος αντι για την αρχή    
list=[]
x=0
while x<10:
    list.append(10*x+10)
    x=x+1
print(list)



list=[]
x=100
while x>=0:
    list.insert(0,x)
    x=x-10
print(list)




#4 FUNCTIONS

def CheckAge(Age):
    answer=" "
    if Age>=13:
        if Age<=19:
            answer="You are a teenager !!!"
        else:
            answer="You are too old to be a teenager !!!"
    else:
        answer="You are too young !!!"
    return answer

x=int(input("How old are you ? "))
print(CheckAge(x))



def NumCheck(Num):
    answer=" "
    if Num>0:
        answer="Positive"
    elif Num==0:
        answer="Nothing"
    else:
        answer="Negative"
    return answer

x=int(input("Type an integer : "))
print(NumCheck(x))



def NumComp(Num1,Num2):
    answer=" "
    if Num1>Num2:
        answer=int(Num1)," is bigger than ",int(Num2)
    elif Num1<Num2:
        answer=int(Num2)," is bigger than ",int(Num1)
    else:
        answer="The 2 numbers are equal !!!"
    return answer

x=int(input("Type one integer : "))
y=int(input("Type another integer : "))
print(NumComp(x,y))





#5 LIBRARIES

from random import randint

print("Rolling a dice 15 times...")
for i in range(15):
    print(randint(1,6))


from random import randint
print("I Roll a dice 15 times.....")
for i in range(0,15):
    print(randint(1,6))


from time import strftime,gmtime
print("Python cell was run on : ",strftime("%a,%d-%b-%Y %H:%M",gmtime()))

from time import strftime,localtime
print("Python cell was run on : ",strftime("%a,%d-%b-%Y %H:%M",localtime()))

from time import strftime
print("Python cell was run on : ",strftime("%a,%d-%b-%Y %H:%M"))


import math
list=[]
x=int(input("Type an integer : "))
for i in range(10):
    list.insert(i,pow(x,i))
print(list)

import math
x=int(input("Type an integer between 1 and 100 : "))
while x>=100 or x<=1:
    x=int(input("Type an integer between 1 and 100 : "))




#6 ARROW FUNCTION LOOP

def stars(Star_Num):
    answer=45*" "
    for i in range(Star_Num):
        answer="*"+answer+"*"
    answer=answer.center(69)
    return answer

for i in range(7):
    print(stars(i))

def stars2(Star_Num2):
    answer2=(45+14)*"*"
    for i in range(Star_Num2):
        answer2="*"+answer2+"*"
    answer2=answer2.center(69)
    return answer2

for i in range(6):
    print(stars2(i))
