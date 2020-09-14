alpha=int(input("Tell us the no of floor:"))
beta=int(input("Tell us the house:"))
sum=0
for row1 in range(1,alpha+1):
    for row2 in range(1,beta+1):
        rent=int(input("bring the rent"))
        if row2==2 or row2==4:
            if rent>8000:print("Thanks for the payment");sum+=rent
            else:print("Need to pay")
        elif row2==1 or row2==3:
            if rent>6000:print("Thanks for the payment");sum+=rent
            else:print("Need to pay")
print("totalcollection:",sum)

