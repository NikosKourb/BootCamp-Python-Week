Name=input("What is your name ? ")
if(len(Name)<5):
    print("You have a very short name")
else:
    print("You don't have a short name")


Age=input("How old are you ? ")
if(int(Age)>31):
    print("You are older than me")
else:
    print("You are younger than me")
    

Age=input("How old are you ? ")
if(int(Age)>=13 and int(Age)<=19):
    print("You are a teenager")
else:
    print("You are not a teenager")*



Age=input("How old are you ? ")
if(13<=int(Age)<=19):
    print("You are a teenager")
else:
    print("You are not a teenager")



def check(Age):
    answer=" "
Age=input("How old are you ? ")
if(int(Age)>=13):
  if(int(Age)<=19):
    print("You are a teenager")
  else:
    print("You are not a teenager")
else:
    print("You are too young")
