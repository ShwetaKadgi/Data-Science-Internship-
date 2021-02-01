#1
for i in range(4):
    for j in range(i+1):
        print("*",end = " ")
    print(" ")
#2
print("\n\n")
rows = 5  
for i in range(rows + 1,0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  

#3
rows = 5

for i in range(0,rows + 1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ") 

for i in range(rows + 1,0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")
#4

rows = 5
space = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, space):
        print(end = " ")
    space -= 2
    for j in range(0, i + 1):
        print("*", end=" ")
    print()
#5

for i in range(1, 6):
  print (' ' * (5 - i), '* ' * i)
#6
print("\n\n")
for i in range(5, 0,-1):
  print (' ' * (5 - i), '* ' * i)

print("\n\n")
#7

for i in range(1, 6):
  print (' ' * (5 - i), '* ' * i)
for i in range(5, 0,-1):
  print (' ' * (5 - i), '* ' * i)

#8


num = 5
for i in range(num):
    for j in range(num):
        print("* ", end="")
    print()
#9


n = 5
for i in range (n, 0, -1): 
    print((n-i) * ' ' + i * '*')
#10


for i in range(3):
    for j in range(6):
        print("*",end=" ")
    print()
#11
n = 5
for i in range (1, n): 
    print((n-i) * ' ' + i * '*')

for i in range (n, 0, -1): 
    print((n-i) * ' ' + i * '*')
