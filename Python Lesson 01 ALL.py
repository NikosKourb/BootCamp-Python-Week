#0 Commenting the code
#This is a comment
#This is another comment

#1 Printing simple words or Results
print("Hello World")
print("Do my work for me")


print(10-(6-4))
print(31*7+112/2-(5-2))

#2 Variable Assignment
x=4
print(x)
x=4
x=5
print(x)

x=5
x=int(x)
print(x+10)


x="Giwrgi"
print(x+" den pas kala "+x+" !!!")
x=10
x=str(x)
print("5+5= "+x)


#3 True False
print(3>2)
print(5<2)
print(2<1 or 5<2)
print(10<9 or 2>1)


A=False
B=True
C=True
print(A and B)
print((A and B) or C)
print(B or C)
print(A and (B or C))


#4 User input checks for True or False
Name=input("What is your name ? ")
print("Your name is "+Name)
Question="What is your age "+Name+" ? "
Age=input(Question)
print("Your age is "+Age+" "+Name+" !!!")
print("Next year you will be ",int(Age)+1," "+Name+" !!!")
True_or_False=int(Age)>30
print("The fact that "+Name+" is older than 30 years is ",True_or_False)


#5 User Input Calculation
a=input("Dwse mou enan akeraio : ")
b=input("Dwse mou enan akoma akeraio : ")
print("To a8roisma twn duo akeraiwn einai ",int(a)+int(b)," !!!")


a=input("Dwse mou enan akeraio : ")
b=input("Dwse mou enan akoma akeraio : ")
sum=int(a)+int(b)
print("To a8roisma twn duo akeraiwn einai ",int(sum)," !!!")

#6 Integer Swap
x=input("Dwse mou enan akeraio : ")
y=input("Dwse mou enan akoma akeraio : ")
print("Mou edwses x= "+x+" kai gia y= "+y+" !!!")
z=x
x=y
y=z
print("Meta apo swap exw x=",int(x),"kai gia y=",int(y),"!!!")


#7 Lists
Games=["Minecraft","Skyrim","War Robots","Mario Cart","The Witcher","Assassins Creed"]
print(Games[0])
Games.sort()
print("My favorite PC Games are ",Games)
print(Games.index("Minecraft"))
Games.reverse()
print("My favorite PC Games are ",Games)
Games.insert(0,"Democracy 3")
print("My favorite PC Games are ",Games)


#8 Tuples
Months=("January","February","March","April","May","June","July","August","September","October","November","December")

