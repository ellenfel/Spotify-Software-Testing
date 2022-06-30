#try:
#   function()

#except:

#except:

#else:

#finally:

from logInOut import *
from Play import *
from genre import *

i = 0
j = 0
k = 0

#Genre testing functinality
def recursiveEH2(k):
    try:
        testGenre()
                        
    except:
        k += 1
        print("#testGenre failures: ",k)
        recursiveEH2(k)

    else:
        return k


#play functinality
def recursiveEH1(j):
    try:
        play()
                

    except:
        j += 1
        print("#Play failures: ",j)
        recursiveEH1(j)

    else:
        recursiveEH2(k)
    return j, k


def recursiveEH(i):

    try:
        LogInOut()
        

    except:
        
        i += 1
        print("#Log(in-out) failures: ",i)
        recursiveEH(i)


    else:
        recursiveEH1(j)
    
    return i, j, k
        
                
recursiveEH(i)


#zprint("number of test failures happend during func 1 testing is: ",i)
#print("number of test failures happend during func 2 testing is: ",j)
#print("number of test failures happend during func 3 testing is: ",k)
#test1, test2, test3 = i,j,k