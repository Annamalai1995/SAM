#pyramid
'''
n= int(input("TEll us "))
limit=1
for row in range(1,n+1):
    for col in range(n-1,row-1,-1):print(" ",end="")
    for data in range(1,limit+1):print("#",end="")
    limit+=2;print()
'''
n=int(input("Tell us"))
limit=4
for row in range(n.row-1):
    for col in range(n+1,row+1,1):
        print(" ",end="")
        for data in range(1,limit-1):print("#",end="")
        limit+=2;print()
