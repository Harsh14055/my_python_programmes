from time import *
import random as ran


def mistakes(para,user):
    errors = 0
    for i in range(len(para)):
        try:
            if para[i]!=user[i]:
                errors = errors + 1
        except:
            errors = errors + 1
    return errors
def speed(startTime,endTime,user):
    delay = endTime - startTime
    delay = round(delay,2)
    user = user.split(" ")
    return round(len(user)/delay,2)
if __name__=='__main__':
    while True:
        check = input("Do you want to continue yes/no : ")
        if check=="yes":
            test = ["fiuer iuhgr uhfru uhr","hfieuhg iuhgiuht iuhgiut","uigiur urigue ugiweuhrg","igrfr  ujwrgf wyrg ygf"]

            t1 = ran.choice(test)

            print("_____Type Speed_____")

            print(t1)
            print()
            print()
            start_time = time()
            tin = input("Start Typing press enter after end : ")
            end_time = time()
            print("No. of errors : ",mistakes(t1,tin))
            print("Time taken : ",round(end_time-start_time,2)," secs")
            print("No. of words : ",len(tin.split(" ")))
            print("Speed : ",round(speed(start_time,end_time,tin)*60)," words per min")
        elif check=="no":
            print("Thank You")
            break
        else:
            print("Invalid Input please enter yes or no.")