print("********************************","\n")
print(" "*7+"\033[1;94;40mPrinting Traingles\033[0m\n")
print("********************************")
#header with allignment and coloured Text

n=int(input("Enter no. of rows: "))
#accepting input for number of rows

for i in range(1,n+1):
    print("* "*i)
#printing * in a right triangular fashion 

#printing $ to form equilateral triangle
def print_triangle(n): #defining triangle function and passing arg: number of rows
    space = 2*n - 2 #calculating spaces
    
    for i in range(0, n):
        for j in range(0, space):
            print(end=" ") #print spaces for j times
        
        space = space - 1 #decrement space by 1
    
        for j in range(0, i+1):
             print(" \033[1;37;4%sm$\033[0m"%(i), end="") #print $ in a row for j times in (0 to i)
        print("\r")#next line
        
print_triangle(n) #calling function and passing the number of rows

#result: ✔
#1
#$ py ml_5_Printing_a_Triangle.py
#********************************

#       Printing Traingles

#********************************
#Enter no. of rows: 10
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
                   $
                  $ $
                 $ $ $
                $ $ $ $
               $ $ $ $ $
              $ $ $ $ $ $
             $ $ $ $ $ $ $
            $ $ $ $ $ $ $ $
           $ $ $ $ $ $ $ $ $
          $ $ $ $ $ $ $ $ $ $

#2
#********************************

#       Printing Traingles

#********************************
#Enter no. of rows: 3
*
* *
* * *
     $
    $ $
   $ $ $

