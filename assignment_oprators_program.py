############# Arirthmatic oprators######

##que1.write a programon addition oprators from user value .
x=int(input("Enter first number:="))
y=int(input("Enter second value :="))
add=(x+y)
print("Addition of two  numbers is:=",add)

x=10
y=20
z=(x+y)
print(z)

##que2.write a programon subtraction oprators from user value.
a=int(input("Enter the first value:="))
b=int(input("Enter the second value:="))
sub=(a-b)
print("Subtrraction of two numbers:=",sub)

a=40
b=20
c=(a-b)
print(c)

##que3.write a programon multiplication oprators from user value.
x=int(input("Enter the first value:="))
y=int(input("Enter the second value:="))
mul=(x*y)
print("Multiplication of two numbers is:=",mul)

x=45
y=12
z=(x*y)
print(z)

##qur4.write a programon divition oprators from user value.
a=int(input("Enter the first value:="))
b=int(input("Enter the second value:="))
div=(a/b)
print("Divition  of two numbers:=",div)

a=56
b=5
c=(a/b)
print(c)

##que5.write a programon floor divition oprators from user value.
a=int(input("Enter the first value:="))
b=int(input("Enter the second value:="))
fdiv=(a//b)
print("Floor divition  of two numbers:=",fdiv)

a=27
b=2
c=(a//b)
print(c)

##que6.write a programon moduls oprators from user value.
x=int(input("Enter the first value:="))
y=int(input("Enter the second value:="))
moduls=(x%y)
print("Moduls divition of two numbers is:=",moduls)

x=35
y=7
z=(x%y)
print(z)

##que7.write a program exponent(power) oprator from user.
x=int(input("Enter the first value:="))
y=int(input("Enter the second value:="))
power=(x**y)
print("Exponent or powerof two numbers is:=",power)

x=5
y=2
z=(x**y)
print(z)

################# Relational oprators#########

##que1.write program for graterthan oprator.
x=int(input("Enter the first value:="))
y=int(input("Enter the second value:="))
if x>y:
    print("x is grater than y:=",x)
else:
    print(" y is grater than x:=",y)

x=30
y=25
if x>y:
    print('x is grater than y',x)
else:
    print("y is grater than x:=")

x=8
y=3
x>y


###que2.write program for lessthan oprator.
a=int(input("Enter the first value:="))
b=int(input("Enter the second value:="))
if a<b:
    print("a is less  than b:=",a)
else:
    print(" b is less than a:=",b)

a=10
b=25
if a<b:
    print('a is less than b',a)
else:
    print("b is less than b:=",b)

a=7
b=12
a<b

##que3.write program for graterthan equal to oprator.
x = int(input("Enter the first value:="))
y = int(input("Enter the second value:="))
if x >= y:
    print("x is grater than equale to y:=", x)
else:
    print(" y is grater equal to than x:=", y)

x = 35
y = 25
if x >= y:
    print('x is grater equal to than y', x)
else:
    print("y is grater equal to than x:=", y)

x = 24
y = 9
x >=y

##que4.write program for lessthan equal to  oprator.
a = int(input("Enter the first value:="))
b = int(input("Enter the second value:="))
if a <= b:
    print("a is less than equal to b:=", a)
else:
    print(" b is less than equal to a:=", b)

a = 10
b = 25
if a <= b:
    print('a is less than equal to b', a)
else:
    print("b is less than equal to b:=", b)

a = 7
b = 12
a <= b

##que5.write program for  equal to oprator.
x=int(input("Enter the first value:="))
y=int(input("Enter the second value:="))
if x==y:
    print("x is  equale to y:=",x)

x=25
y=25
if x==y:
    print('x is  equal to y',x)

x=10
y=10
x==y

##que6.write program for not equal to  oprator.
a = int(input("Enter the first value:="))
b = int(input("Enter the second value:="))
if a != b:
    print("a is not equal to b:=", a)

a = 109
b = 225
if a != b:
    print('a is not equal to b', a)

a = 71
b = 12
a != b

############## Assignment oprators#############

##que1.write program for add and assign oprator.
a = int(input("Enter the first value:="))
b = int(input("Enter the second value:="))
a+=b
print("Assign addition oprator is:=",a)

a = 31
b = 22
b+=a
print("Assign addition oprator is:=",b)

##que2.write program for sub  and assign oprator.
x = int(input("Enter the first value:="))
y = int(input("Enter the second value:="))
x-=y
print("Assign subtraction oprator is:=",x)

x = 110
y = 22
y-=x
print("Assign subtraction oprator is:=",y)

##que3.write program for multiplication and assign oprator.
a = int(input("Enter the first value:="))
b = int(input("Enter the second value:="))
a*=b
print("Assign multiplication oprator is a:=",a)

a = 3
b = 22
b*=a
print("Assign multiplicatio oprator is b:=",b)

##que4.write program for divition  and assign oprator.
x = int(input("Enter the first value:="))
y = int(input("Enter the second value:="))
x/=y
print("Assign divition oprator is x:=",x)

x = 56
y = 7
y/=x
print("Assign divition oprator is y:=",y)

x=10
y=3
x/=y
print(x)

##que4.write program for floor divition  and assign oprator.
x = int(input("Enter the first value:="))
y = int(input("Enter the second value:="))
x//=y
print("Assign floor divition oprator is x:=",x)

x = 9
y = 75
y//=x
print("Assign floor divition oprator is y:=",y)

x=-56
y=5
x//=y
print(x)


##que6.write program for moduls divition  and assign oprator.
x = int(input("Enter the first value:="))
y = int(input("Enter the second value:="))
x%=y
print("Assign moduls divition oprator is x:=",x)

x = 7
y = 71
y%=x
print("Assign moduls divition oprator is y:=",y)

x=-75
y=8
x%=y
print(x)

################# Logical oprators###############

##que1.write a program for and logic opraror.
a = 2
b = 4
if a > 0 and b < 0:  ### and
    print(" both condiotion are true:=", a, 'and', b)
    print(a * b)
else:
    print('do nothing')

print(10 and 20)
print(100 and 30)

##que2.write a program for or logic opraror.
a = 8
b = 4
if a > 0 or b < 0:  ### and
    print(" both condiotion are true:=", a, 'and', b)
    print(a + b)
else:
    print('do nothing')

print(20 or 15)
print(90 or 300)

##que3.write a program for Not logic opraror.
a=True
if not a:
    print(a)
else:
    print("do nothing")

print(not 1)
print(not 0)
print(not 10)
print(not 14)

################# Membership oprator(in)###############

##que1.write program on membersgip oprator.
list = [1, 2, 3, 4, 5]
print(list)
num = 2
if num in list:
    print("Member present in list:=", num)
else:
    print(" not present")

my_list = [11, 15, 21, 29, 50, 70]
print(my_list)
number = 15
if number in my_list:
    print("number is present", number)
else:
    print("number is not present")

l1 = ['a', 'b', 'c', 'd', 'e']
print(l1)
char = 'a'
if char in l1:
    print("char is present in list:=", char)
else:
    print("char is not present in list")

list = ['madhuri', 'anant', 'swara', 'komal']
print(list)
name = 'anant'
print(name)
if name in list:
    print("name is present in list:=", name)
else:
    print(" name is not present list")

# que2.write program on membership oprator (not in).
list = [1, 2, 3, 4, 5]
print(list)
num = 7
print('num=', num)
if num not in list:
    print("number is not present in list:=", num)
else:
    print('present in list')

l1 = ['a', 'b', 'c', 'd', 'e']
print(l1)
char = 'm'
print('char', char)
if char not in l1:
    print("char is not in present  list:=", char)
else:
    print("char is present in list")

list = ['madhuri', 'anant', 'swara', 'komal']
print(list)
name = 'ankita'
print('name', name)
if name not in list:
    print("name is not in present list:=", name)
else:
    print(" name is present in list")


################# Identity operator##################

##que1.write a program for is oprator.
x=10
print(id(x))
y=10
print(id(x))
print(x is y)

x='a'
print(id(x))
y='b'
print(id(x))
print(x is y)

##que2.write a program for is not oprator.
a=10
print(id(a))
b=20
print(id(b))
print(a is not b)

x='a'
print(id(x))
y='b'
print(id(x))
print(x is not y)

x=10
print(id(x))
y=10
print(id(x))
print(x is not y)


############# Bitwise oprator##############

##que1.write program for &(and) oprator.
a=7           ## note-convert int to binary value and get ans again in int.
b=4
c=5
print(a & b)
print(b & c)
print(c & a)

x=10
y=2
z=8
print(x & y)
print(y & z)
print(z & x)

##que2.write a program for |(or) oprator.
a=4          ## note-convert int to binary value and get ans again in int.
b=7
c=5
print(a|b)
print(b|c)
print(c|a)

x=1
y=3
z=4
print(x|y)
print(y|z)
print(a|z)
##que3.write a program for ^(xor) oprator.
a=1
b=3
c=6
print(a^b)
print(b^c)
print(a^c)

x=0
y=6
z=4
print(x^y)
print(y^x)
print(z^x)

##que4.write a program for 1's complement(~) oprator.
a=2
b=1
c=3
print(~a,~b,~c)

##que5.write a program for bitwise left shift(<<) oprator.
print(4<<2)
print(6<<2)
print(12<<3)

##que5.write a program for bitwise right shift(>>) oprator.
print(4>>2)
print(8>>2)
print(2>>3)
