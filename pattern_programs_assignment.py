##que1.Write a program to display the pattern of stars given as follows:
# * * * * *
# * * * *
# * * *
# * *
# *

num=7
x=num
for i in range(1,6,1):
    num=num-1
    for j in range(1,num,1):
        print('*',end=' ')
        x=num-1
    print()

## form user enter value
num = int(input("Enter the value of star:="))
x = num
for i in range(1, num, 1):
    num = num - 1
    for j in range(1, num, 1):
        print('*', end=' ')
        x = num - 1
    print()

##que2.Write a program to display the pattern of stars given as follows:
# *
# * *
# * * *
# * * * *
# * * * * *
num=5
for i in range(1,num+1,1):
    for j in range(i):
        print('*',end=' ')
    print()
########### or
num=int(input("Enter the value of stars:="))
for i in range(1,num+1,1):
    for j in range(i):
        print('*',end=' ')
    print()
########### or
num=int(input("Enter the value of stars:="))
x=num
for i in range(1,num+1,1):
    num=num+1
    for j in range(i):
        print('*',end=' ')
    print()


##que3.Write a program to display the pattern of numbers given as follows:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

num=1
x=num
for i in range(1,6,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num+1
    print()

########## from user value##
num=int(input("Enter the value of numbers:="))
x=num
for i in range(1,num,1):
    num=num+1
    for j in range(1,i):
        print(j,end=' ')
        x=num+1
    print()



##que3.Write a program to display the pattern of numbers given as follows:
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
#1 2 3 4 5 6
num=int(input("Enter the value of number"))
x=num
for i in range(1,num,1):
    x=num+1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num+1
    print()

##que4.Write a program to display the pattern of numbers given as follows:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3
#1 2
#1

num=1
x=num
for i in range(1,5,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num+1
    print()
num=5
x=num
for i in range(1,5,1):
    num=num-1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num-1
    print()

###### same above que nut num=8
num=1
x=num
for i in range(1,8,1):
    num=num+1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num+1
    print()
num=8
x=num
for i in range(1,8,1):
    num=num-1
    for j in range(1,num,1):
        print(j,end=' ')
        x=num-1
    print()

##que5.Write a program to display the pattern of numbers given as follows:
##Right Triangle Star Pattern In Python.
#    *
#   **
#  ***
# ****
#*****
#size=int(input("Enter the number of stars:="))
size=5
for i in range(size):
    for j in range(1,size-i):
        print(' ',end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    print()
#que7.Write a program to display the pattern of numbers given as follows:
##Hollow Square Pattern
#size=int(input("Enter the value of stars:="))
size=5
for i in range(size):
    for j in range(size):
        if  i== 0 or i==size-1 or j==0 or j==size-1:
            print('*',end=' ')

        else:
            print(' ',end=' ')
    print()

##que8.Write a program to display the pattern of downward triangle star pattern
# *****
# ****
# ***
# **
# *
size=5
for i in range(size):
    for j in range(size-i):
        print('*',end=' ')
    print()
##que9.Write a program to display the pattern of Right Downward Triangle Pattern
#*****
# ****
#  ***
#   **
#    *

size=int(input("Enter the value of stars:="))
for i in range(size):
    for j in range(i):
        print(' ',end=' ')
    for j in range(size,i,-1):
        print('*',end=' ')
    print()

##que10.Write a program to display the pattern of hollow triangle star pattern.
#*
#**
#* *
#*  *
#*   *
#******
n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print('*',end=' ')
        else:
            if i!=n:
                print(' ',end=' ')
            else:
                print('*',end=' ')
    print()

##que11.Write a program to display the pattern of Pyramid Pattern in python
#    *
#   ***
#  *****
# *******
#*********
n=int(input("Enter the value of stars:="))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()

######### or######33
n=5
for i in range(n):
    print(' '*(n-i-1) + '*' * (2*i+1))


