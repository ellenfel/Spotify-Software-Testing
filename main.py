from logInOut import *
from Play import *
from genre import *


#implement inherence!
class Test1:
    def __init__(self, i):
        self.i = i

    def get_num(self):
        return self.i

    def set_num(self, i):
        self.i = i

class Test2:
    def __init__(self, j):
        self.j = j

    def get_num(self):
        return self.j

    def set_num(self, j):
        self.j = j

class Test3:
    def __init__(self, k):
        self.k = k

    def get_num(self):
        return self.k

    def set_num(self, k):
        self.k = k

i = Test1(0)
i.set_num(0)

j = Test2(0)
j.set_num(0)

k = Test3(0)
k.set_num(0)

#Genre testing functinality
def recursiveEH2():
    try:
        testGenre()
                        
    except:
        k.set_num(k+=1)
        print("#testGenre failures: ",k.get_num())
        recursiveEH2()

    else:
        return 


#play functinality
def recursiveEH1():
    try:
        play()
                

    except:
        j.set_num(j+=1)
        print("#Play failures: ",j.get_num())
        recursiveEH1()

    else:
        recursiveEH2()


def recursiveEH():

    try:
        LogInOut()
        

    except:
        i.set_num(i+=1)
        print("#Log(in-out) failures: ",i.get_num())
        recursiveEH()


    else:
        recursiveEH1()
            
                
recursiveEH()

print(i.get_num())

#print("number of test failures happend during func 1 testing is: ",i)
#print("number of test failures happend during func 2 testing is: ",j)
#print("number of test failures happend during func 3 testing is: ",k)
#test1, test2, test3 = i,j,k