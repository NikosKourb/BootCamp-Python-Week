def checkage(Age):
    answer=" "
    if(int(Age)>=13):
           if(int(Age)<=19):
                  answer="You are a teenager"
           else:
                  answer="You are not a teenager"
    else:
        answer="You are too young"
    return answer

x=int(input("Enter your Age : "))
print(checkage(x))



##def checkage(Age):
##    answer=" "
##    if(int(Age)>0):
##        if(int(Age)<0):
##            answer="N"
##        else:
##            answer="zero"
##    else:
##        answer="zerooooo"
##    return answer
##
##x=(input("Enter a number : "))
##print(checkage(x))



def NumberCheck(Num):
    if(Num<0):
        #answer="Negative"
        if(Num == 0):                    
            answer="Zero"
        else:
            answer="Negative"
    else:
        answer="Positive"
    return answer

x=int(input("Enter a Number : "))
print(NumberCheck(x))


def NumberCheck(Number):
    if(Number<0):
        answer="Negative"
    elif(Number>0):
        answer="Positive"
    else:
        answer="Not Negative nor Positive"
    return answer

x=int(input("Enter a Number : "))
print(NumberCheck(x))



def NumberCheck2(Number1,Number2):
    if(Number1<Number2):
        answer="Number2 is Bigger than Number1"
    elif(Number1>Number2):
            answer="Number1 is Bigger than Number2"
    else:
            answer="The 2 Numbers are Equal"
    return answer

x=int(input("Enter a Number : "))
y=int(input("Enter another Number : "))
print(NumberCheck2(x,y))





