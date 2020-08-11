#Rock paper scissors game#
import random

print('Hello, welcome to Rock Paper Scissors')

user = input('Choose rock, paper, or scissors : ')

rps = ['rock', 'paper', 'scissors']

computer = random.choice(rps)

if user not in rps:
	print('You must pick "Rock, Paper, or Scissors"')
elif user.capitalize() == computer.capitalize():
	print('Computer chose ' + computer + ' TIE!')
elif ((user.capitalize() == 'Rock' and computer.capitalize == 'Scissors') or (user.capitalize() == 'Paper' and computer.capitalize == 'Rock') or (user.capitalize() == 'Scissors' and computer.capitalize == 'Paper')):
	print('Computer chose '+ computer + ' YOU WIN!')
else:
	print('Computer chose ' + computer + ' YOU LOSE!')