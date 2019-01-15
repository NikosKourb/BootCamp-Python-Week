Name = input("What is your name : ")
print("Your name is : ",Name)

Question = "What is your age " + Name +" ? "
Age=input(Question)
print("Your age is : ",Age)

Age=int(Age)
print("Next year you will be : ",Age+1)

True_or_false=Age>=12
print(Name,"is older than 30 is ",True_or_false)
