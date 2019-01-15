##
##from random import randint
##list=[]
##
##for i in range(100):
##    list.insert(0,randint(1,9))
##print(list)



def pattern(List):
    count=0
    for i in range (0,98):
        if (list[i]==1 and list[i+1]==1):
            count=count+1
        else:
            count=0   
    print ("Pattern found",count,"time/times")  
pattern(list)



##
##thislist = ["apple", "banana", "cherry"]
##if "apple" in thislist:
##  print("Yes, 'apple' is in the fruits list")
