#try:
#   function()

#except:

#except:

#else:

#finally:

from logInOut import *
i=0

try:
    LogInOut()

except:
    i += 1
    print(i)
    LogInOut()

else:
    print("total number of runs before it worked is ",i)
