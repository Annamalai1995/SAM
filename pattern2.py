#pattern
'''
word="selenium"
for row in range(len(word)):
    for col in range(len(word)):print(word[col],end=" ")
    print()
'''
#input get the pattern
'''
word=input("tell us word pattern")
for row in range(len(word)):
    for col in range(len(word)):print(word[col],end=" ")
    print()
'''
#floid pattern
'''
word="selenium"
for row in range(len(word)):
    for col in range(row+1):print(word[col],end=" ")
    print()
'''
#floaid pattern2
word="selenium"
for row in range(len(word),0,-1):
    for col in range(row):print(word[col],end=" ")
    print()
  
