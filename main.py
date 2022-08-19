import random

def get_choices():
  player_choice=input('Enter a choice (rock, paper, scissors): ')
  options=['rock', 'paper', 'scissors']
  computer_choice=random.choice(options)
  choices={'player':player_choice, 'computer':computer_choice}
  return choices
  

def check_win(player, computer):
  print(f'you chose {player}, computer chose {computer}')
  if player==computer:
    return 'it\'s a tie'
  elif player=='rock':    #rock
    if computer=='scissors':
      return 'rock smashes scissors, u win'
    else:
      return 'paper covers rock, you loose.'

  elif player=='paper':    #paper
    if computer=='rock':
      return 'paper covers rock, u win'
    else:
      return 'scissors cuts paper, you loose.'

  elif player=='scissors':    #scissors
    if computer=='paper':
      return 'scissors cut paper, u win'
    else:
      return 'rock smashes scissors, you loose.'

choices=get_choices()
result=check_win(choices['player'],choices['computer'])
print(result)