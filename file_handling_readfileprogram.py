## another file read by using path
Fp=open("c:/Users/Admin/Desktop/file handling/madhuri/sonali/prime_number.py",'r')
print(Fp.read())
Fp.close()
## another example.
fp=open("add_sub.txt.py",'r')
print(fp.read())
fp.close()

##read file with "with" acess mode
with open("div_mul.txt.py",'r') as f:
    print(f.read())

### prgram for readline(): Read a File Line by Line ,here only fist line read.
with open ("div_mul.txt.py",'r') as F:
    line=F.readline()
    print(line)

##readline(): Read a File Line by Line
with open ("add_sub.txt.py",'r') as R:
    line=R.readline()
    print("Here print first line of program,it given below")
    print(line)

### by using for loops readline We can read the first few set of lines from a file by using the readline() method.
# Run a loop fo n times using for loop and range() function, and use the readline() ,
with open ("div_mul.txt.py",'r') as A:
    for i in range(3):
        print(A.readline().strip())

##Reading Entire File Using readline() by using while loop.
with open ("add_sub.txt.py",'r') as file:
    Line=file.readline()
    while Line!='':
        print(Line,end=' ')
        Line=file.readline()
        print()

##Reading First and the Last line using readline()
with open ("div_mul.txt.py",'r') as M:
    first_line=M.readline()
    print("First line of code")
    print(first_line)
    for last_line in M:
        pass
    print("Last line of code")
    print(last_line)

##readlines(): Reading File into List  The reading of the contents will start from the
# beginning of the file till it reaches the EOF (End of File).
with open("Read_list.py",'r') as l:
    Lines=l.readlines()
    print(Lines)
##Reading first N lines from a file
N=3
with open ("Read_list.py",'r') as H:
    line_3=[next(H) for x in range(N)]
print(line_3)

##Reading the last N lines in a file
n=1
with open ("div_mul.txt.py",'r') as E:
    line_2_last=E.readlines()[n:]
print(line_2_last)

##Reading N Bytes From The File. # read file with absolute path
try:
    filename = open("c:/Users/Admin/Desktop/file handling/madhuri/sonali/palindrome.py", 'r')
    print(filename.read(300))
    filename.close()
except FileNotFoundError:
    print("Please enter the correct path")

## Reading and Writing to the same file
#with open("add_sub.txt.py",'r+') as R_W:
 #   print(R_W.read())
 #   R_W.write("\n This addition of two numbers.")
 #   print(R_W.read())

##Reading File in Reverse Order
print("Read reversed program:=")
with open ("add_sub.txt.py",'r') as  reve:
    line=reve.readlines()
    for Lines in reversed(line):
        print(Lines)
##### python seek() file start from nth number  ####
with open("c:/Users/Admin/Desktop/file handling/madhuri/sonali/prime_number.py",'r') as FP:
    print("Here first three chara is missing bcoz set pointer from 3 to end .")
    FP.seek(3)
    print(FP.read())

## Seek the Beginning of the File
#with open("seek_file_rewr.txt.",'w') as s:
 #   s.write("My first line\n")
  #  s.write("my second line\n")
   # s.seek(0)
    #print(s.read())

## Seeking The End of File..
with open(r'C:\Users\Admin\PycharmProjects\pythonProject1\seek_file_rewr.txt' , 'r+') as e:
    e.seek(0, 2)
    e.write("\n This content addes at the end of the line")
    e.seek(0)
    print(e.read())

import os

# Absolute path of a file
#old_name = r"C:/Users/Admin/PycharmProjects/pythonProject1/details.txt"
#new_name = r"C:/Users/Admin/PycharmProjects/pythonProject1/new_details.txt"
#if os.path.isfile(new_name):
#    print("The file all ready existing")
#else:
 #   os.rename(old_name,new_name)

import os
old_name = r"C:/Users/Admin/PycharmProjects/pythonProject1/details.txt"
new_name = r"C:/Users/Admin/PycharmProjects/pythonProject1/new_details.txt"
try:
    os.rename(old_name,new_name)
except:
    print("The file all ready existing")
    print("remove existing file")
    os.remove(new_name)
    os.rename(old_name,new_name)
    print("done remaining file.")






