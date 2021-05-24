import random
a=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
l=random.randint(0,2)
if(a==0 and l==0):
  print(rock)
  print("Computer choose:")
  print(rock)
  print("Draw")

elif(a==0 and l==1):
  print(rock)
  print("Computer choose:")
  print(paper)
  print("You lose")

elif(a==0 and l==2):
  print(rock)
  print("Computer choose:")
  print(scissors)
  print("You win")

elif(a==1 and l==1):
  print(paper)
  print("Computer choose:")
  print(paper)
  print("Draw")

elif(a==1 and l==0):
  print(paper)
  print("Computer choose:")
  print(rock)
  print("You win")

elif(a==1 and l==2):
  print(paper)
  print("Computer choose:")
  print(scissors)
  print("You lose")


elif(a==2 and l==2):
  print(scissors)
  print("Computer choose:") 
  print(scissors)
  print("Draw")

elif(a==2 and l==0):
  print(scissors)
  print("Computer choose:")
  print(rock)
  print("You lose")

elif(a==2 and l==1):
  print(scissors)
  print("Computer choose:")
  print(paper)
  print("You win")

else:
  print("You typed an invalid number ")