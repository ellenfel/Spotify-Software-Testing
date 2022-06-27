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
def recurrsiveEH2(k):
    try:
        testGenre()
                        
    except:
        k += 1
        print("#testGenre failures: ",k)
        recurrsiveEH2(k)

    else:
        return i,j,k


#play functinality
def recurrsiveEH1(j):
    try:
        play()
                

    except:
        j += 1
        print("#Play failures: ",j)
        recurrsiveEH1(j)

    else:
        recurrsiveEH2(k)


def recurrsiveEH(i):
    try:
        LogInOut()
        

    except:
        i += 1
        print("#Log(in-out) failures: ",i)
        recurrsiveEH(i)


    else:
        recurrsiveEH1(j)
                
recurrsiveEH(i)

test1, test2, test3 = i,j,k
print("number of test failures happend during func 1 testing is: ",test1)
print("number of test failures happend during func 2 testing is: ",test2)
print("number of test failures happend during func 3 testing is: ",test3)