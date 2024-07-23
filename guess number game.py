#بازی حدس عدد
# guess number game
from random import randint
print("I Choose A Number From 0 To 100,Tell Me The Number")
print("You Have 5 Chance")
def correct(a , b):
    if (a > 100 or a < 0) :
        return 1
    elif (a < b):
        return 2
    elif (a > b):
        return 3
    elif (a == b):
        return 0
def correct_2(c):
    if (c == 0):
        print('You Won!')
    elif (c == 1):
        print('Number Is Between 0 And 100')
    elif (c == 2):
        print('Number Is Bigger')
    elif (c == 3):
        print('Number Is Lower')     
number = randint (0 , 100)
user_input = int(input('Enter Number: '))
c = correct(user_input , number)
correct_2(c)
if (c == 0):
        print('You Won!')
count = 1
while (count != 5):
    user_input = int(input('Enter Number: '))
    count = count + 1
    if (count == 5):
        print('You Lose!')
        print('Number Is' , number)
        break
    c = correct(user_input , number)
    c_2 = correct_2(c)
    if (c == 0):
        break
        
    
    

        
    
