def mult_by_2(num):
    return num*2

times_two=mult_by_2
print("4*2=",times_two(4))



def get_func_mult_num(num):
    def mult_by(value):
        return num * value
    return mult_by
generated_func=get_func_mult_num(5)

print("5 * 10 =",generated_func(10))



listOfFuncs=[times_two,generated_func]

print("5*9=", listOfFuncs[1](9))


def is_it_odd(num):
    if num % 2==0:
        return False
    else:
        return True
    
def change_list(list, func):

    oddlist=[]

    for i in list:
        if func(i):
            oddlist.append(i)
    return oddlist
alist=range(1,20)

print(change_list(alist,is_it_odd))



def random_func(name:str, age:int,weight:float):
    print("Name:",name)
    print("Age:",age)
    print("Weight:",weight)
    
    return "{} is {} years old and weighs {}".format(name,age,weight)
print(random_func("Derek",41,165.55))


sum =lambda x,y:x+y
print("sum :",sum(4,5))

can_vote= lambda age:True if age >=18 else False
print("Can Vote :", can_vote(19))


powerList=[lambda x:x**2,
           lambda x:x**3,
           lambda x:x**4]

for func in powerList:
    print(func(4))










    attack={'quick':(lambda :print("Quick Attack")),
            'power':(lambda :print("Power Attack")),
            'miss':(lambda :print("Missed Attack"))}
    attack['quick']()

    import random

    attackKey=random.choice(list(attack.keys()))
attack[attackKey]()


import random
#create list
fliplist=[]
#populate list with 100 Hs and Ts
for i in range(1,1001):
    fliplist += random.choice(['H','T'])
#output results

print("Heads :", fliplist.count('H'))
print("Tails :",fliplist.count('T'))


#Mapfunction
oneTo10=range(1,11)

def dbl_num(num):
    return num*2
print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x:x*3),oneTo10)))

aList=list(map((lambda x,y:x+y),[1,2,3],[1,2,3]))
print(aList)

#Filter in Lists

print(list(filter((lambda x:x%2==0),range(1,11))))


#Find the multiples of 9 from a random 100 value list with
#values between 1 and 1000

#List

RandList = list(random.randint(1,101) +78+8+8+88for i in range(100))
print(list(filter((lambda x:x % 9==0),RandList)))






import random

for i in range(1,1000):

#Use modulus to find multiples of 9



#Inheritance in python

#code reusability
#Transaction readsbility
#IMPORTANCE OF USING CLASS IN PYTHON
#Safe from bug
#Easy to understand
#Ready for change

#class Parent:
    #def funct1(self):
        #print('this is a parent function')
#class Child(Parent):
    #def func2(self)
       # print("this is a child function")
#ob=Child()
#ob.funct1()#







ob.func2()















