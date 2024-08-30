import random
from art_works import logo,stages
from words import word_list
empty_list = []
position = -1
game_on = True
print(logo)

random_word = random.choice(word_list)
print(random_word)
for i in range(len(random_word)):
    empty_list.append('_')
print(empty_list)

while game_on:
    user = input("Enter a letter for complete word: ").lower()
    try:
        number = int(user)
    except:
        pass
    else:
        print("Enter a valid letter")

    if user in empty_list:
        print("You already enter that letter")
    elif user in random_word:
        for i in range(len(random_word)):
            if random_word[i] == user:
                empty_list[i]=user
        print(empty_list)
        if "_" not in empty_list:
            print("Game over,You win")
            game_on = False
            break
    elif user not in random_word:
        print("letter not in the word")
        print(stages[position])
        position -=1
        if position==-8:
            print("You loose,Game over")
            game_on=False



