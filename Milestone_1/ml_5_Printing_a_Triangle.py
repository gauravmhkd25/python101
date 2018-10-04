print("********************************","\n")
print(" "*7+"\033[1;94;40mPrinting Traingles\033[0m\n")
print("********************************")
n=int(input("Enter no. of rows: "))

for i in range(1,n+1):
    print("* "*i)

k = n * 2 - 1

def triangle(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
             print(" \033[1;37;4%sm$\033[0m"%(i), end="")
        print("\r")
triangle(n)
