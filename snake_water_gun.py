import random

#compare is a function which compares and returns who won the game
def compare(user,comp):
    if(user == 's'):
        if(comp == 's'):
            return 0
        elif (comp == 'w'):
            return 1
        else:
            return -1
    elif(user == 'w'):
        if(comp == 'w'):
            return 0
        elif(comp =='s'):
            return -1
        else:
            return 1
    else:
        if(comp == 'g'):
            return 0
        elif(comp =='s'):
            return 1
        else:
            return 0


#Taking the input from user in the form of a character and then convert it into a whole string
userchar = input("Enter your choice : Snake(s) / Water(w) / Gun(g) ? : ")
if(userchar == 's'):
    user = "Snake"
elif(userchar == 'w'):
    user = "Water"
else:
    user = "Gun"


#Some random input from the random (in-built) python module
compinput = random.randint(1,3)
if(compinput == 1):
    compchar = 's'
elif (compinput == 2):
    compchar = 'w'
else:
    compchar = 'g'

#Converting the computer's turn from character into a string
if(compchar == 's'):
    comp = "Snake"
elif(compchar == 'g'):
    comp = "Gun"
else:
    comp = "Water"

#Printing both the choices
print("Your choice :",user)
print("Computer's choice :",comp)

#using the compare funtion to calculate who won 
# 1 -> User won
# 0 -> Game tied
# -1 -> Computer Won
result = compare(userchar,compchar)

if(result == 0):
    print("Game tied")
elif(result == 1):
    print("You Won")
else:
    print("Computer Won")





