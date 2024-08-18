"""
oyun karşılama mesajı
oyun döngüsü
skor sistemini kur
bunları yazdır.
oyuna devam etmek için sor
yeniden başlatma: bilgisayara da sor!
"""
import random

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

game_list = [rock, paper, scissors]
player_score, computer_score, round_number, match_number = 0, 0, 1, 1
game_over, round_over = False, False
welcome_message = """Welcome to our rock-paper-scissors game!
Rock beats Scissors,
Scissors tears Paper,
Paper wraps Stone!
Make your choice wisely!
"""


def start_game():
    global player_score, computer_score, round_number, match_number, game_over, round_over
    player_score, computer_score, round_number = 0, 0, 1
    match_number += 1
    round_over = False


def tas_kagit_makas_ugur_yuruk(user_choice, pc_choice, player_score, computer_score):
    global game_list, round_number

    if user_choice == pc_choice:
        print("\nYour choice\n"+game_list[user_choice] +
              "\nComputer Choice\n"+game_list[pc_choice]+"\nGame Draw...\n")
    elif user_choice == 0 and pc_choice == 2:
        print("\nYour choice\n"+game_list[user_choice] +
              "\nComputer Choice\n"+game_list[pc_choice]+"\nYou win...\n")
        player_score += 1
    elif user_choice == 1 and pc_choice == 0:
        print("\nYour choice\n"+game_list[user_choice] +
              "\nComputer Choice\n"+game_list[pc_choice]+"\nYou win...\n")
        player_score += 1
    elif user_choice == 2 and pc_choice == 1:
        print("\nYour choice\n"+game_list[user_choice] +
              "\nComputer Choice\n"+game_list[pc_choice]+"\nYou win...\n")
        player_score += 1
    else:
        print("\nYour choice\n"+game_list[user_choice] +
              "\nComputer Choice\n"+game_list[pc_choice]+"\nYou lose...\n")
        computer_score += 1

    return player_score, computer_score


def check_game_over(player_score, computer_score, round_number):
    global round_over
    if player_score == 2:
        print(f"You win! Your score is {player_score}")
        round_over = True
    elif computer_score == 2:
        print(f"You lose :( Your score is {player_score}")
        round_over = True
    else:
        round_number += 1

    return round_number


print(welcome_message)

while not game_over:

    while not round_over:
        print(f"Match: {match_number} Round: {round_number}\n\nPlayer Score:{
              player_score}\nComputer Score:{computer_score}")
        user_choice = int(
            input("\nWhat do you choose? \nType 0 for Rock, \n1 for Paper or \n2 for Scissors. "))

        if user_choice not in [0, 1, 2]:
            print("Please make a valid choice!")
            continue
        
        pc_choice = random.randint(0, 2)
        
        player_score, computer_score = tas_kagit_makas_ugur_yuruk(
            user_choice, pc_choice, player_score, computer_score)

        round_number = check_game_over(
            player_score, computer_score, round_number)

    computer_continue = random.randint(0, 1)
    play_again = input("Would you like to play another game?(y/n)").lower()

    if play_again == 'y' and computer_continue == 1:
        start_game()
    elif computer_continue == 0:
        print("Computer refuses to play, see you!")
        game_over = True
    else:
        game_over = True
        print("It was a good match, thank you!")
