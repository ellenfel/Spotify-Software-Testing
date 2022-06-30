from logInOut import *
from Play import *
from genre import *
from unfollow import unfollow

i = 0
j = 0
k = 0
l = 0

#follow -unfollow functinality
def recursiveEH3():

    global l

    try:
        unfollow()

    except:
        l += 1
        print("#follow-button failures: ",l)
        recursiveEH3()


#Genre testing functinality
def recursiveEH2():

    global k
    
    try:
        testGenre()
                        
    except:
        k += 1
        print("#testGenre failures: ",k)
        recursiveEH2()

    else:
        recursiveEH3()

#play functinality
def recursiveEH1():

    global j

    try:
        play()
                

    except:
        j += 1
        print("#Play failures: ",j)
        recursiveEH1()

    else:
        recursiveEH2()

#Login-out functionality testing 
def recursiveEH():

    global i
    
    try:
        LogInOut()
        

    except:
        
        i += 1
        print("#Log(in-out) failures: ",i)
        recursiveEH()


    else:
        recursiveEH1()
    
                
recursiveEH()

print("number of test failures happend during func 1 testing is: ",i)
print("number of test failures happend during func 2 testing is: ",j)
print("number of test failures happend during func 3 testing is: ",k)
print("number of test failures happend during func 4 testing is: ",l)