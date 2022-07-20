#importing random
import random
List = ['rock', 'paper', 'scissors']
#counter
c = 3
#scores
Hscore = 0
Myscore = 0
#The gamestarts
print("####### rock, paper and scissors #######")
print('________________________________________')
print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
while c>0 :
#His or her answer
  R1 = input('rock, paper, scissors now!, choose one: ')
  IndexR1 = List.index(R1)
#My answer
  L1 = List[random.randint(0,2)]
  IndexL1 = List.index(L1)
  print('I chose: ',L1)
#Who won?
  #Tie
  if R1 == L1:
    c+=1
  if (IndexR1-IndexL1) == 2:
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('I won')
    Myscore += 1
  elif (IndexR1-IndexL1) > 0 or (IndexR1-IndexL1) == -2 :
    Hscore += 1
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('You won')
  elif (IndexR1-IndexL1) == 0 :
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('Nobody won')
  else:
    Myscore += 1
    print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
    print('I won')
  c -= 1  
print('Your score is ',Hscore)
print('My score is ',Myscore)

if Hscore > Myscore :
  print('You are the winner')
else:
  print('I am the winner')