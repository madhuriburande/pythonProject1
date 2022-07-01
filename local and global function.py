##que1.write program for local variable.
from functools import reduce


def function1():
    local_var=3122
    print("local variable is:=",local_var)
function1()

##que2.Global Variable in function
global_var='Madhuri Anat burande'
def fun_Global():
       print("Global variable is:=",global_var)
fun_Global()

##que3.the global keyword using.
x='outside var i.e global var'
def function1():
    local_var='Python'
    print('local variable:=',local_var)
function1()
def function2():
    local_var2='Data science'
    print('local variable2:=',local_var2)
function2()
def key_var_Global():
    global x
    print(x)
key_var_Global()

##que4.glonal key use
a=31
def function3(x,y=22):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    print('add', add, 'sub', sub, 'mul', mul, 'div', div)
    return add,sub,mul,div
function3(14)

def function4(b):
    global a
    sum=a+b
    print("Addition of two number is:=",sum)
    sub=a-b
    print("subtraction of two number is:=",sub)
function4(20)

### by using nonlocal variable
def outer_func():
    x='I am Anant and my birth date is 22/08/1992'
    def inner_func():
        nonlocal x
        print('Hello I am Madhuri and',x)
        return inner_func
    inner_func()
    print("Thank you")
outer_func()

##que Positional Arguments
def add_sub(a,b):
    sum=a+b
    z=a-b
    print('addition is:=', sum,'subtraction is:=',z)
    return sum,z

add_sub(50,10)

## Keyword Arguments.
def name_details(name,last_name):
    print("Hello Every one i am",name,last_name)
    print('Hi my self',name,last_name)
name_details('Madhuri','Burande')
name_details('anant','Burande')

##Default Arguments
def function1(name='Madhuri'):
    print("Hello",name,'How r u')
function1('Anant')
function1('Team Brain work')
function1()

## Variable-length Arguments
def fun(*num):
    total=0
    for i in num:
        total=total+i
    print(total)
fun(10,39,45,23)
fun(1,2,3,4,5)

## by usinglist
def even_odd(*lst):
    for i in lst:
        if i % 2== 0:
            print('even number is:=',i)
        else:
            print('odd number is',i)

lst=[31,22,14,23,5,28,10,3]
print(lst)
even_odd(*lst)
even_odd(1,2,3,4,5)

##Recursive Function
def factorial(no):
    if no == 0:
        return 1
    else:
        return no*factorial(no-1)
print("Factorial number is:=",factorial(5))

## by using user define value
def factorial_fun(x):
    #x=int(input("Enter the numbber:="))
    if x==0:
        return 1
    else:
        return x*factorial_fun(x-1)
print("factorial number is:=",factorial_fun(3))

##  Python Anonymous/Lambda Function.
l=[31,22,43,5,3,23,10,28]
print(l)
l1=list(filter(lambda x: x%2==0,l))
print("even number in list=",l1)

## by using lambda function
l1=[2,4,6,3,5,9,11,22,31]
print(l1)
#l2=list(filter(lambda x: x%2==1 ,l1))
#print("odd number in list=",l2)

####  Python Anonymous/filter with lambda Function
l1=[-10, 5, 12, -78, 6, -1, -7, 9]
print(l1)
positive_num=list(filter(lambda x: x>0,l1))
print("The positive number in lists are:=",positive_num)

negative_num=list(filter(lambda x: x<0 ,l1))
print("The negative number in lists are:=",negative_num)

## map() function in Python
list1 = [2, 3, 4, 8, 9]
print(list1)
list2=list(map(lambda x: x*x*x,list1))
print("The cube of list :=",list2)

##reduce() function in Python
from functools import reduce
l1=[2,4,6,8,2,9,11]
print(l1)
add= reduce(lambda x,y: x+y,l1)
print("The addition of list:=",add)







