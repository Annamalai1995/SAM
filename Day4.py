#identity opearator: is ,is not
'''sam=int(input("pin:"))
sam1=int(input("confirm pin:"))
print(sam is sam1)
print(sam is not sam1)
'''

#member opeartor: in,not in
'''
developer="ANNAMALAI"
print('A' in developer)
print('MA' not in developer)
'''
# relational and logical operator

#control statements: if and elif

#biggest among three string
'''
dev1=input("devlpoer name1:")
dev2=input("devlpoer name2:")
dev3=input("devlpoer name3:")
if dev1>dev2:
    print(dev1,"bigger than",dev2,"and",dev3)
elif dev2>dev3:print(dev2,"bigger than",dev1,"and",dev3)
else:print(dev3,"bigger than",dev1,"and",dev2)
'''

#AC based condenser and warranty thn type
condenser=input("condenser name:")
boardyear=int(input("warranty year:"))
if boardyear>=3:
    print(" voltas 1 or 2 tons available")
elif boardyear==1 and condenser=='copper':
    print("samsung")
elif boardyear==2 and condenser=='aluminium':
    print("blue star")
elif boardyear==1 and condenser=='copper':
    print("carrier")
elif boardyear==2 and condenser=='aluminium':
    print("hitachi")
else:
    print("not available in this shop")
    
