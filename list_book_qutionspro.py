## que1.Create a list of five elements. Pass the list to a function and compute the average of five numbers
def calculate_avg(lst3):
    print('list',lst3)
    print('The sum of list:=',sum(lst3))
    avg=sum(lst3)/len(lst3)
    print('The average of list is:=',avg)

lst3=[1,2,3,4,5,6]
calculate_avg(lst3)

##que2.Write a function Split_List(Lst,n), where list Lst is split into two parts and the length of the fi rst part
##is given as n.
##Lst = [1,2,3,4,5,6]
##Split_List(Lst,2)
##Lst1=[1,2]
##Lst2=[3,4,5,6]

def split_List(lst,n) :
    list1 = lst[:n]
    list2 = lst[n:]
    print('first list with', n, 'element')
    print(list1)
    print('second list with',len(lst)-n, 'element')
    print(list2)

lst=[10,20,30,50,60,100]
print('list lst before split')
print(lst)
split_List(lst,4)

## RETURNING LIST FROM A FUNCTION
##que3.Write a program to pass a reverse list to function
def Reverse_list(lst):
    print('before reverse list=',lst)
    lst.reverse()
    print('after reverse list=',lst)
    return lst

lst=[1,3,5,7,9,11]
Reverse_list(lst)

##que4.Write a function that accepts a positive integer k and returns a list that contains the first five
#multiples of k.The first five multiples of 3 are 3, 6, 9, 12, and 15.

def multi_list(k):
    my_list = []
    for i in range(1,6):
        res = i*k
        my_list.append(res)
    return my_list

print(multi_list(3))

##que5.same but mul by 5
def multiplication_of_list(k):
    my_list=[]
    for i in range(1,11):
        res=k*i
        my_list.append(res)
    return my_list
print("The multiplication table of 5")
print(multiplication_of_list(5))

##que6.Write a function that accepts two positive integers, viz. a and b and returns a list of all the even
#numbers between a and b (including a and not including b).Even numbers between 10 and 20.[10,12,14,16,18]

def even_num(start,end):
    my_list = []
    for num in range(start,end):
        if num%2==0:
            my_list.append(num)
    return my_list
print(even_num(10,20))

### or odd numbers

def odd_numbers(start,end):
    output=[]
    for num in range(start,end):
        if num%2==1:
            output.append(num)
    return output
print(odd_numbers(10,20))

##que7.Write a function is_Lst_Palindrome(Lst) to check whether a list is palindrome. It should return True
##if Lst is palindrome and False if Lst is not palindrome.
def is_Lst_Palindrome(Lst):
    r= Lst[::-1]
    for i in range(0,(len(Lst) +1)//2):
        if r[i] != Lst[i]:
            return False
    return True

Lst = [1,2,3,2,1]
x = is_Lst_Palindrome(Lst)
print(Lst,'( is palindrome): ',x)
Lst1 = [1,2,3,4]
x = is_Lst_Palindrome(Lst1)
print(Lst1,'(is palindrome): ',x)

##Write a function check_duplicate(Lst) which returns True if a list Lst contains duplicate elements.
##It should return False, if all the elements in the list Lst are unique.
def check_duplicate(lst):
    dup_list=[]
    for i in lst:
        if i not in dup_list:
            dup_list.append(i)
        else:
            return True
    return False
lst=[1,2,3,4,1,2,3,6]
print(lst)
x=check_duplicate(lst)
print(x)
lst1=[10,20,30,40]
print(lst1)
x=check_duplicate(lst1)
print(x)

##Write a program that prompts a user to enter the element of a list and add the element to a list.
##Write a function maximum(Lst) and minimum(Lst) to fi nd the maximum and minimum number from the list.
##Lst = [ 12,34,45,77] Should return 12 as Minimum and 77 as Maximum.
lst=[]
for i in range(0,4):
    x=int(input("Enter the number to add to list"))
    lst.append(x)
print(lst)
def maximum(lst):
    max=lst[0]
    for num in lst:
        if max<num:
            max=num
    return max
def minimum(lst):
    min=lst[0]
    for num in lst:
        if min>num:
            min=num
    return min
y=minimum(lst)
print("The minimum number of list is=:",y)
y=maximum(lst)
print("The maximum number of list is:=",y)

##Write a function Assign_grade(Lst) which reads the marks of a student from a list and
##assigns a grade based on the following conditions:
##if Marks >=90 then grade A
## if Marks >=80 && <90 then grade B
 ##if Marks >65 && < 80 then grade C
 ##if Marks > =40 && <=65 then grade D
 ##if Marks <40 then grade F
##Consider the List of Marks of a 5 Student in English Subject.
 ##Lst=[78,90,34,56,89]
#Should return
 ##Student 1 Marks 78 grade C
## Student 2 Marks 90 grade A
 ##Student 3 Marks 34 grade F
 ## 4 Marks 56 grade D
 ##Student 5 Marks 89 grade B

def Assign_Grade(lst):
    for marks in lst:
        if marks>90:
            print('Student',lst.index(marks)+1,'marks=',marks,'Grade A')
        elif marks>80 and marks<90:
            print('student',lst.index(marks)+1,'marks=',marks,'Grade B')
        elif marks>65 and marks<80:
            print('student',lst.index(marks)+1,'marks=',marks,'Grade C')
        elif marks>40 and marks<65:
            print('student',lst.index(marks)+1,'marks=',marks,'Grade D')
        else:
            print('student',lst.index(marks)+1,'marks=',marks,'Grade F')
lst=[78,35,67,88,93]
print("Marks of 5 students is=",lst)
Assign_Grade(lst)

##Write a function check_duplicate(Lst) which returns True if a list Lst contains duplicate elements.
##It should return False if all the elements in the list Lst are unique.
def duplicate_list(lst):
    dup_list=[]
    for i in lst:
        if i not in dup_list:
            dup_list.append(i)
        else:
            return True
    return  False
lst=[1,2,3,4,4,5,1]
print(lst)
x=duplicate_list(lst)
print('duplicate numbers in list=',x)
lst1=[11,12,13,14]
print(lst1)
x=duplicate_list(lst1)
print("duplicate numbers in list",x)

##queWrite a function print_reverse(Lst) to reverse the elements of a list.
##Note: Reverse the contents of a list without using the reverse() method of a list and without using slicing
##Lst=[12,23,4,5]
 # Should reverse the contents of list as follows
 ##Lst=[5,4,23,12]

def Reverse_list(lst):
    print("before reversing list")
    print(lst)
    l2=[]
    count=1
    for i in lst:
        l2.append(lst[len(lst)-count])
        count+=1
    return l2
lst=[11,23,4,5,6,7]
x=Reverse_list(lst)
print("after reversing list")
print(x)

##Write a function that accepts two positive integers a and b (a is smaller than b) and returns a list
##that contains all the odd numbers between a and b (including a and including b if applicable)in descending order.
##Odd numbers between 10 and 20 should create the list and print the list in descending order as follows
# [19, 17, 15, 13, 11]
def desendind_odd(start,end):
    l1=[]

    for i in range(start,end+1):
        if i%2==1:
            l1.append(i)
            l1.sort()
            l1.reverse()
    return l1
print(desendind_odd(10,20))

##Write a program to return prime numbers from a list.
list1=[3,17,9,2,4,8,97,43,39]
print('List1= ',list1)
lst=[]
for a in list1:
    prime=True
    for i in range(2,a):
        if (a%i==0):
            prime=False
            break
    if prime:
        lst.append(a)
print("The prime numbers are in list:=",lst)
##que.Write a program to search an element from a list

def linear_search(my_list,key):
    for i in range(len(my_list)):
        if (my_list[i]==key):
            return i
            break
    return -1
my_list=[31,22,14,45,12]
print(my_list)
key=int(input("Enter the number to be searched:="))
l1=linear_search(my_list,key)
if l1!=-1:
    print(key,"is found at index potion:=",l1+1)
else:
    print(key,"is not found in list")

##que.Write a program for binary search.
def binary_search(my_list, key):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (len(my_list) // 2)
        if my_list[mid] == key:
            return mid
        elif key > my_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


my_list = [5, 3, 23, 28, 10, 31]
print(my_list)
key=int(input("Enter the number to be searched"))
x = linear_search(my_list, key)
if (x == -1):
    print(key, "is not found in list")
else:
    print(key, "ispresent in list at index potionis:=", x)

