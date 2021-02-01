#1
n = 5
for i in range(n):
    for j in range(i + 1):
        if(j == 0 or j == i or i == n - 1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
#2
print("\n\n")
n = 5
for i in range(n - 1,-1,-1):
    for j in range(i + 1):
        if(j == 0 or j == i or i == n - 1):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()


#3
    
row = 5
for i in range(row):
    for j in range(row-i):
        print(' ', end='')
    for j in range(2*i+1):
        if j==0 or j==2*i or i==row-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()

#4
print("\n\n")
row = 5
for i in range(row - 1,-1,-1):
    for j in range(row-i,0,-1):
        print(' ', end='')
    for j in range(2*i+1):
        if j==0 or j==2*i or i==row-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()

#5


n = 5
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if (i == 1 or i == n or	j == 1 or j == n):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#6


n = 5
for i in range(n):    
    print(" "(n-i-1)+" ",end="")    
    if i>=1:        
        print(" "(2*i-1)+" ",end="")    
    print()
for i in range(n-1,-1,-1):    
    print(" "(n-i-1)+" ",end="")    
    if i>=1:        
        print(" "(2*i-1)+" ",end="")    
    print()
#7


n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        if(k == 0 or i == 0 or k == n-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#8
print("\n\n")

n=17
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(mid-i):
            print(" ",end="")
        for k in range(i+1):
            if(k==0 or k==i):
                print("*",end="")
            else:
                print(" ",end="")
    else:
        for j in range(i-mid):
            print(" ",end="")
        for k in range(n-i):
            if(k==n-i-1 or k==0):
                print("*",end="")
            else:
                print(" ",end="")
    print()
#9

n=15
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(i+1):
            if(i == j or j == 0):
                print("*",end="")
            else:
                print(" ",end = "")
    else:
        for j in range(n-i):
            if(i == j or j == 0 or j == n - i - 1):
                print("*",end="")
            else:
                print(" ",end = "")
    print()
#10
n = 6
for i in range(1, n-2) :
    for j in range(1, n+1) :
        if (i == 1 or i == n or	j == 1 or j == n or i == n - 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#11

n=5
for i in range(n, -1,-1):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        if(k == 0 or i == 0 or k == n-i-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
