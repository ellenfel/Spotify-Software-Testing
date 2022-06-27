#try:
#   function()

#except:

#except:

#else:

#finally:

from logInOut import *
i = 0

def recurrsiveEH(i):
    try:
        LogInOut()

    except:
        i += 1
        print(i)
        recurrsiveEH(i)

    else:
        return i

recurrsiveEH(i)

if(i!=0):
    print("number of exceptions during tests = ",i)