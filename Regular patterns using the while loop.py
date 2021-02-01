#1
i=1
while i<=4:
    j=1
    while j<=i:
        print("*",end = " ")
        j=j+1
    print(" ")
    i=i+1

#2
print("\n\n")
rows = 5
i=rows
while i>=0:
    j=0
    while j<=i:  
        print("*", end=' ')
        j=j+1
    print(" ")
    i=i-1

#3
rows = 5
i=0
while i<rows:
    j=0
    while j<=i-1:  
        print("*", end=' ')
        j=j+1
    print(" ")
    i=i+1
i=rows+1
while i>=0:
    j=0
    while j<=i-1:  
        print("*", end=' ')
        j=j+1
    print(" ")
    i=i-1

#4

rows = 5
space = 2 * rows - 2
i=0
while i<=rows:
    j=0
    while j<=space:
        print(end = " ")
        j=j+1
    space -= 2
    while j<i+1:
        print("*", end=" ")
        j=j+1
    print()
    i=i+1

#5
i=1
while i<6:
  print (' ' * (5 - i), '* ' * i)
  i=i+1


#6
print("\n\n")
i=5
while i>=1:
  print (' ' * (5 - i), '* ' * i)
  i=i-1

print("\n\n")

#7

i=1
while i<=6:
  print (' ' * (5 - i), '* ' * i)
  i=i+1
i=5
while i>=1:
  print (' ' * (5 - i), '* ' * i)
  i=i-1


#8

print()

num = 5
i=1
while i<=num:
    j=1
    while j<=num:
        print("* ", end="")
        j=j+1
    print()
    i=i+1

#9


n = 5
i=n
while i>=0: 
    print((n-i) * ' ' + i * '*')
    i=i-1



#10

i=1
while i<=3:
    j=1
    while j<=6:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1



#11
n = 5
i=1
while i<=n: 
    print((n-i) * ' ' + i * '*')
    i=i+1
i=n
while i>=0: 
    print((n-i) * ' ' + i * '*')
    i=i-1
    
