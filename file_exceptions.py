##without tey and except block code
#a=10
#b=0
#c=a/b
#print(c)
#The ouput will shoe the error i.e ZeroDivisionError: division by zero

##que.same code but using try and except
## or-- whithout error name mention
# default exception

try:
    x=15
    y=0
    z=x/y
    print("The divisition of x and y is",z)
except:
    print("We can't divide by zero.provide different number") # default exception.
## or


##  we don't know which type error those time use bellow conditions
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception as e:
    print("exception is:",e)

##que.write program for value error and zerodivision
## for value error
try:
    a = int(input("enter the first number:="))
    b = int(input("enter the second nuber:="))
    c=a/b
    print("The division of a and b is:=",c)
except ValueError as s:
    print("Entered value is wrong:",s)

## for division error
try:
    a = int(input("enter the first number:="))
    b = int(input("enter the second nuber:="))
    c=a/b
    print("The division of a and b is:=",c)
except ZeroDivisionError as e:
    print("can't divide by zero:",e)

##Handle multiple exceptions with a single except clause
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except(ValueError, ZeroDivisionError):
    print("Please enter a valid value or can't divide by zero")
## syntax error not display lt's exmple
try:
    a=10
    b=0
    prin(c)
except Exception as e:
    print("exception is:",e)

### Using try with finally##
#with correct code
try:
    a=10
    b=5
    c=a/b
    print("division of a and b is:=",c)
finally:
    print("By using finally,Division done sucesfully")
## with error
try:
    x=10
    y=0
    z=x/y
    print("the division of x nad y is:=",z)
except Exception as e:
    print("exception is:",e)
finally:
    print("inside a finally block")

## Using try with else clause
# The else block is executed if there is no exception.
try:
    a=20
    b=5
    c=a/b
    print("the division of",a,'and',b,'is:=',c)
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Inside a else block")

## the else block with executed if there is exception present
try:
    x=6
    y=0
    z=x/y
    print(z)
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Inside else block")








