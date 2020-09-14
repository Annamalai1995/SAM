# theater chart:$,-

chart=""
for row in range(1,5):
    for seat in range(1,7):
        amt=int(input("Tell us amount"))
        if amt>=300:
            print("Ticket booked @",row,seat)
            chart+='$'
        else:
            print("Insufficient balance")
            chart+='_'
   chart+='\n'
print(chart)
