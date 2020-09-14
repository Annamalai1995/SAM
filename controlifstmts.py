#control statement if....if....if..else
#Theme park

amt=int(input("Enter the amonut"))
if amt>1000:
    print("enjpy the wonderla")
    weight=float(input(" Enter the weight"))
    if weight>=45 and weight<60:
        print("waves games")
    if weight>=50 and weight<80:
        print("rapid river")
    if weight>=90 and weight<120:
        print("roller coaster")
    if weight>=60 and weight<100:
        print("you can enjoy swimming pool")
    else:
        print("you can enjoy all sort dry games")
else:
    print("insufficient amount")
            
