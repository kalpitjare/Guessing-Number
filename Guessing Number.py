# clear screen function making
def cls():
    import os
    os.system('cls')

# clear screen running

cls()

# starting
print("This Is A Game Of Guessing The Number")
print("You Have Only Five Chances")
print("\n************************Rule************************ \n # No Negative Number Are Allowed")

# enter the number

num1 = int(input("\nEnter The Numbers Between '1 - 10' =  "))

number = 4

# if 1 chance

if num1<=3 : print("The Number You Entered Is Smaller")

if num1>number : print("The Number You Entered Is Greater")

if num1==number : print("\nCongratulations!!! You Have Won The Game")

if num1==number : exit()

if num1>10 : print("Invalid Input")

if num1<1 : print("Invalid Input")


#____________________________________________________________________________


# enter the number

num1 = int(input("\nAgain Enter The Numbers Between '1 - 10' =  "))

number = 4

# if 2 chance

if num1<=3 : print("The Number You Entered Is Smaller")

if num1>number : print("The Number You Entered Is Greater")

if num1==number : print("\nCongratulations!!! You Have Won The Game")

if num1==number : exit()

if num1>10 : print("Invalid Input")

if num1<1 : print("Invalid Input")

#____________________________________________________________________________


# enter the number

num1 = int(input("\nAgain Enter The Numbers Between '1 - 10' =  "))

number = 4

# if 3 chance

if num1<=3 : print("The Number You Entered Is Smaller")

if num1>number : print("The Number You Entered Is Greater")

if num1==number : print("\nCongratulations!!! You Have Won The Game")

if num1==number : exit()

if num1>10 : print("Invalid Input")

if num1<1 : print("Invalid Input")


#____________________________________________________________________________


# enter the number

num1 = int(input("\nAgain Enter The Numbers Between '1 - 10' =  "))

number = 4

# if 4 chance

if num1<=3 : print("The Number You Entered Is Smaller")

if num1>number : print("The Number You Entered Is Greater")

if num1==number : print("\nCongratulations!!! You Have Won The Game")

if num1==number : exit()

if num1>10 : print("Invalid Input")

if num1<1 : print("Invalid Input")

#____________________________________________________________________________


# enter the number

num1 = int(input("\nAgain Enter The Numbers Between '1 - 10' =  "))

number = 4

# if 5 chance

if num1<number : print("The Number You Entered Is Smaller")

if num1>number : print("The Number You Entered Is Greater")

if num1==number : print("\nCongratulations!!! You Have Won The Game")

if num1==number : exit()

if num1>10 : print("Invalid Input")

if num1<1 : print("Invalid Input")

print("\n\nYou Have Loss The Game")

exit()

