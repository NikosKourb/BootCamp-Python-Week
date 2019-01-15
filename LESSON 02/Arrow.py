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


def stars3(Star_Num3):
    answer3=67*"*"
    x=
    for i in range(Star_Num3):
        answer3=int(x-i)*"*"+59*+"*"*int(x-i)
        answer3=answer3.center(69)
    return answer3

for i in range(5):
    print(stars3(i))


#5 se ka8e meria ara apo 59
##answer=""
##for i in range(2):
##    answer="*"+answer+"*"
##    answer=answer.center(10)
##print(answer)

##answer=45*" "
##for i in range(2):
##    answer="*"+answer+"*"
##    answer=answer.center(70)
##print(answer)

##print(stars(1))
##print(stars(2))
##print(stars(3))
##print(stars(4))
##print(stars(5))
##print(stars(6))
##print(stars(7))
##print(stars(8))
##print(stars(9))
##print(stars(10))
##print(stars(11))
##print(stars(12))


##def stars(Star_Num):
##    answer=""
##    for i in range(Star_Num):
##        answer=answer+"*"
##        answer=answer.center(12)
##        return answer
##
##print(stars(1))
##print(stars(2))
##print(stars(3))
##print(stars(4))
##print(stars(5))
##print(stars(6))
##print(stars(7))
##print(stars(8))
##print(stars(9))
##print(stars(10))
##print(stars(11))
##print(stars(12))

##def stars(Star_Num):
##    answer=""
##    for i in range(Star_Num):
##        answer=answer+"*"+"                                    "+"*"
##    answer=answer.rjust(12)
##    answer=answer.58,70
##    return answer
##
##print(stars(1))
##print(stars(2))
##print(stars(3))
##print(stars(4))
##print(stars(5))
##print(stars(6))
##print(stars(7))
##print(stars(8))
##print(stars(9))
##print(stars(10))
##print(stars(11))
##print(stars(12))
##
