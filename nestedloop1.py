#nested loop at flash sale example

turns=int(input("Tell us how many times you wish open the sale: "))
for one in range(1,turns+1):
    stock=int(input("Tell us stock forthe sale: "))
    qty=0
    for time in range(1,31):
        required=int(input("Tell us how many quantity you want:"))
        if required <= stock:
            stock-=required
            print("your order of",required,"is placed @",one)
            qty+=required
            if stock<=0 or time==30:print("Sale is over");break
            print(one,"sold items are",qty)
