##que1.create function without parameter
def message():
    print("Hello wlecome to python class")
    print("Thank you")
message()

##que2.create function with parameter.
def Name_details(first_name,last_name):
    print("My name first name is",first_name)
    print("my last name is",last_name)

Name_details('Madhuri','Burande')
## or---
def course_details(name,course_name):
    print("My name is",name)
    print("cource name is",course_name,"and python program is very easy to learn,read and write language")
course_details('Madhuri','Python')

##que3.assing by using parameter function.
def Addition(a,b):
    print("The additionof pass two parameter is:=",a+b)
Addition(50,20)

##qur4.by using function write program for addition ,subtraction,multiplication,& division.
def Arithmatic(a,b):
    add=a+b
    print("The addition of two numbers is:=",add)
    mul=a*b
    print("The multiplication of two number is:=",mul)
    sub=a-b
    print("The subtraction of two number is:=",sub)
    div=a/b
    print("The division of two number is:=",div)
Arithmatic(120,10)

def User_Arithmatic():
    a=int(input("Enter the first number:="))
    b=int(input("Enter the second number:="))
    add=a+b
    print("The addition of two numbers is:=",add)
    mul=a*b
    print("The multiplication of two number is:=",mul)
    sub=a-b
    print("The subtraction of two number is:=",sub)
    div=a/b
    print("The division of two number is:=",div)
User_Arithmatic()

##que5.function with parameters with return valaue.
def even_odd(x):
    if x%2==0:
        print("The given number is even:=",x)
    else:
        print("The given number is odd:=",x)
        return x
even_odd(75)

##que6.write program for even and odd and given value by user.
def user_evodd():
    x=int(input("Enter the number:="))
    if x%2==0:
        print("The number is even:=",x)
    else:
        print("The number is odd:=",x)
        return x
user_evodd()

##que7.write program for list all elelments addition
def list_add(lst):
    for i in lst:
        i=i+i
        print(i,end=' ')
lst=[1,2,3,4,5]
print(lst)
list_add(lst)
print()

## que8.totla add of list
def total_add_list(lst1):
    total=0
    for i in lst1:
        total=total+i
    print(total)
    return total
lst1=[1,2,3,4,5,6,]
print(lst1)
total_add_list(lst1)

### or
def add_l1(lst1):
    sum=0
    for i in lst1:
        sum=sum+i
    print("Total addition of list is:=", sum)
    return sum
lst1=[4,5,3,8,9]
print(lst1)
add_l1(lst1)

##que9. create docstring
## single line doc string
def message(x):
    ''''This is doc string function.there are two types singleline and two line doc strin here use single line doc string.'''
    return x
print(message.__doc__)

## doubble line doc string.
def dubble_message(y):
    """Hello every on welcome to python class,python is high level langauge.It is portable language."""
    return y
print(dubble_message.__doc__)

##que7.return value from function.
def is_even(lst):
    evennum=[]
    for i in lst:
        if i%2==0:
            evennum.append(i)

    return evennum
evennum=is_even([2,3,7,8,9,11,31,22])
print("even numberis:=",evennum)

## for odd number
def is_odd(lst):
    oddnum=[]
    for i in lst:
        if i%2==1:
            oddnum.append(i)
    return oddnum
oddnum=is_odd([3,5,2,4,6,7,8])
print("odd number is:=",oddnum)

##que9.Returns multiple value
def arithmatic_fun(a,b):
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    return add,sub,div,mul
a,b,c,d=arithmatic_fun(50,10)
print('add=',a,'sub=',b,'div=',c,'mul=',d)

##que12.default value(parameter)
def default_val(x=10,y=30):
    print("addition of default value is:=",x+y)
default_val()

## recuring multiple values from return
def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(40,10)
print(type(t))
for i in t:
    print(i)

## function are object:python function  are first class
def emp(x):
    return x.upper()
print(emp("Hello  my name is madhuri"))
user=emp
print(user("Hello my name is Anant"))

## function can be passed as a arguments.
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(fun):
    greeting=fun(" " " I am created by function pass as a arrgument" " ")
    print(greeting)
greet(shout)
greet(whisper)

## function can return  as function.
def outer_fun(x):
    def inner_fun(y):
        return x+y
    return inner_fun
add=outer_fun(15)
print("Addition of two number",add(20))

## function can return as a function
def outer1_func(a):
    def inner1_func(b):
        add=a+b
        sub=a-b
        mul=a*b
        return add,sub,mul
    return inner1_func
x=outer1_func(45)
print(x(10))







