import random

def state(random_word):
    attempts = 10 
    hidden_word = ["_"] * len(random_word)
    letters_used = []

    print("\nДобро рожаловать в игру Висельница!")

    while attempts > 0 and "_" in hidden_word:
        print(f"\nСлово: '{"".join(hidden_word)}'")
        print(f"Осталось попыток: {attempts}")
        print(f"Буквы,которые вы использовали ранее: {", ".join(letters_used)}")

        while True:
            letter = input("\nВведите 1 букву: ")
            if len(letter) == 1 and letter.isalpha():
                if letter in letters_used:
                    print(f"Вы уже вводили букву: '{letter}'")
                else:
                    break
            else:
                print(f"Нужно ввести ровно 1 букву!")
            
        letters_used.append(letter)

        if letter in random_word:
            print(f"Поздравляем!Вы угадали букву: '{letter}'")
            for i in range(len(random_word)):
                if random_word[i] == letter:
                    hidden_word[i] = letter
        else:
            print(f"К сожелению буквы '{letter}' нет в слове)")
            attempts -= 1

    if "_" not in hidden_word:
        print(f"\nПоздравляем!Вы угадали слово: {"".join(hidden_word)}")
    else:
        print(f"\nВы прогирали, загаданное слово было: {random_word}")

while True:
    try:  
        with open('words.txt', 'r', encoding='utf-8') as file:
            text = file.read().split()
    except FileNotFoundError:
        print("Файл: 'words.txt' не был найден!")
        break
    if text:
        random_word = random.choice(text)
        state(random_word)
    else:
        print("Файл пуст!")

    play_again = input("\nХотите ли вы сыграть еще раз? (да/нет): ").lower().strip()
    if play_again not in ['д', 'да', 'у', 'yes', 'y']:
        print("Спасибо за игру, удачи!")
        break
    

    




            

            
                
        





