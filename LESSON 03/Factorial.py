
def Factorial(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return x*Factorial(x-1)
x=(int(input('Input an integer. ')))
##while(x<0):
##   
##    x=(int(input('Input an integer. ')))
print(Factorial(x))

##fac=1
##x=(int(input('Input an integer. ')))
##while(x<0):
##   
##    x=(int(input('Input an integer. ')))
##for i in range(1,x+1):
##    fac=fac*i
##print(fac)
