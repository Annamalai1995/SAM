#function

#basic function
#define function

'''
def greet():
    ans=input("Tell us desired place: ")
    if ans == 'Chennai':print("dangerous to go")
    elif ans == 'salem':print("safe to go")
    elif ans == 'tirupur':print("don't ever to go")
    else:print("stay home stay safe")
greet()
'''
# calling function
'''
def ask(purpose):
    if purpose == 'Enconomy':print("Dont worry everything sold to corporate")
    elif purpose == 'Health':print("That's state govt business")
    elif purpose == 'Relief':print("lift the light")
    else: print("Bharat matha ji jay")
ask('Health')
ask('Economy')
ask('Women safety')

'''

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':print("you are in uk team")
    elif qual == 'diploma' and ref == 'TestLead':print("Test Associate")
    elif qual == 'diploma' and ref == 'TestLead':print("Test Associate")
    else:print("you are hired")
prompt('engg','Project Manager')
prompt('ug','HR')
prompt(ref='TestLead',qual='diploma')
       

 
