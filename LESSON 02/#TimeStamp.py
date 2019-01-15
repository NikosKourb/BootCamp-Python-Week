from time import strftime,gmtime
print("Python cell was run on  : ",strftime("%a,%d-%b-%Y %H:%M",gmtime()))



from time import strftime,localtime
print("Python cell was run on  : ",strftime("%a,%d-%b-%Y %H:%M",localtime()))



from time import strftime
print("Python cell was run on  : ",strftime("%a,%d-%b-%Y %H:%M"))

