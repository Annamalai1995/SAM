'''
num=1
for row in range(1,6):
    for colu in range(1,6):
        print(num,end=" ")
        #if row%2==0:num+=1
        #else:num+=1
        num+=1
'''

#example
'''
1 2 3 4 5
6 8 10 12
14 15 16
17 19
21
'''
'''

data=1
n=5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(data,end=" ")
    print()
'''
data=1
n=5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(data,end=" ")
        if row%2==0:data+=2
        else:data+=1
    print()
