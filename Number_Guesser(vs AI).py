import random

random_num1 = random.randint(1,100) 

user_num1 = int(input(" Guess the number: \t")) 
    
numberof_guesses1 = 1

while (user_num1 != random_num1):
    numberof_guesses1 += 1
    if (user_num1 > random_num1):
        print("\n Guess Lower Number please")
        user_num1 = int(input("Guess the number: \t"))
        
    elif (user_num1 < random_num1):
        print("\n Guess Greater number please")
        user_num1 = int(input("Guess the number: \t")) 
    
print(f"Congratulations you win the game by guessing the correct number {random_num1} \n")
print(f"You took {numberof_guesses1} to guess the correct number.")