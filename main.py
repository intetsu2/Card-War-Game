"""The code might look a bit confusing because some of the varialiables names are similar to others"""
import random as rd, time

# start and end numbers & number of cards each player will have
start, end = 2, 11
player1_cards, player2_cards = 26, 26

# players names
player_1_name = input('Enter 1st player name: ').upper()
player_2_name = input('Enter 2nd player name: ').upper()

while True:
  player1 = rd.randint(start, end)
  player2 = rd.randint(start, end)

  time.sleep(2.5)
  print("\v")
  print(f"{player_1_name}'s card is {player1}")
  time.sleep(2)
  print(f"{player_2_name}'s card is {player2} \v")

  # decides who wins
  if player1 > player2:
    player1_cards +=1
    player2_cards -=1

    time.sleep(1)
    print(f'{player_1_name} wins this round!')
    print("----------------------------")
    time.sleep(0.5)
    print(f'{player_1_name} now has {player1_cards} cards')
    print(f'{player_2_name} now has {player2_cards} cards')
    
  elif player2 > player1:
    player2_cards +=1
    player1_cards -=1

    time.sleep(1)
    print(f'{player_2_name} wins this round!')
    print("----------------------------")
    time.sleep(0.5)
    print(f'{player_2_name} now has {player2_cards} cards')
    print(f'{player_1_name} now has {player1_cards} cards')
    
  else:
    if player1 == player2:
      time.sleep(3)
      print('YOU HAVE A WAR')
      print('As you can tell you two have the same card number, and what this means is you two each get another card to determine who wins this round.')
      
      # gives each a number after they get a war
      player1 = rd.randint(start, end)
      player2 = rd.randint(start, end)
      
      time.sleep(2.5)
      print("\v")
      print(f"{player_1_name}'s card is {player1}")
      time.sleep(2)
      print(f"{player_2_name}'s card is {player2} \v")

      if player1 > player2:
        player1_cards += 2
        player2_cards -= 2
        
        time.sleep(3.5)
        print(f'{player_1_name} wins the War')
        print("----------------------------")
        time.sleep(1.5)
        print(f'{player_1_name} now has {player1_cards} cards')
        print(f'{player_2_name} now has {player2_cards} cards')
        
      elif player2 > player1:
        player2_cards += 2
        player1_cards -= 2
        
        time.sleep(3.5)
        print(f'{player_2_name} wins the War')
        print("----------------------------")
        time.sleep(1.5)
        print(f'{player_2_name} now has {player2_cards} cards')
        print(f'{player_1_name} now has {player1_cards} cards')
      else: # just in case if there to be a war the second time
        if player1 == player2:
          time.sleep(2)
          print('\n')
          print('There have been a WAR again')
          print('To settle this round play Rock, Paper, Scisor')
          print('\n')
          
          time.sleep(1.5)
          roc_pap_sci_winner = input('Enter name of who won the (Rock, Paper, Scissor) game: ').upper()
          if roc_pap_sci_winner == player_1_name:
            player1_cards += 3
            player2_cards -= 3
          
            time.sleep(1)
            print(f'{player_1_name} wins this round!')
            print("----------------------------")
            time.sleep(0.5)
            print(f'{player_1_name} now has {player1_cards} cards')
            print(f'{player_2_name} now has {player2_cards} cards')
          elif roc_pap_sci_winner == player_1_name:
            player2_cards += 3
            player1_cards -= 3
          
            time.sleep(1)
            print(f'{player_2_name} wins this round!')
            print("----------------------------")
            time.sleep(0.5)
            print(f'{player_2_name} now has {player2_cards} cards')
            print(f'{player_1_name} now has {player1_cards} cards')
  # next round decision
  time.sleep(1.5)
  print('\v')
  player = input('Press and enter (P to play Q to quit): ').upper()
  if player == 'P':
    if player1_cards == 0:
      print(f'{player_1_name} ran out of cards to play.')
      break
    elif player2_cards == 0:
      print(f'{player_2_name} ran out of cards to play.')
      break
    else:
      continue
  elif player == "Q":
    break

# displays final score
print('\n')

if player1_cards > player2_cards:
  print('The winner is..')
  time.sleep(3)
  
  print(f'{player_1_name} with {player1_cards} cards')
  print(f'The loser is {player_2_name} with {player2_cards} cards')
elif player2_cards > player1_cards:
  print('The winner is..')
  time.sleep(3)
  
  print(f'{player_2_name} with {player2_cards} cards')
  print(f'The loser is {player_1_name} with {player1_cards} cards')
else:
  if player1_cards == player2_cards:
    print('TIE')
    print(f'{player_1_name} has {player2_cards} cards, and {player_2_name} has {player2_cards} cards')

print('\v')
print('Thank You for playing')
time.sleep(2)
print('\v')
print('                 GAME OVER!')