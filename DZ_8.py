import random

player_wins = 0
comp_wins = 0
player_score_all = 0
comp_score_all = 0

while True:
    print("----------------------------------------")
    print("--- Камень, ножницы, бумага, колодец ---")
    print("----------------------------------------")
    print(" Правила игры:")
    print("Побеждает тот, кто наберет больше очков.")
    print("\t[r] - камень\n\t[s] - ножницы\n\t[p] - бумага\n\t[w] - колодец")
    player_score = 0
    player_select = 0
    comp_score = 0
    comp_select = 0
    print("----------------------------------------")
    print("----------- НАЧАЛО ИГРЫ ----------------")
    for i in range(5):
        print("--------- РАУНД №" + str(i + 1) + "---------")
        comp_select = random.choice("rpsw")

        while True:
            player_select = input("\tТвой выбор?:")
            if (player_select == "r") or (player_select == "s") or (player_select == "p") or (player_select == "w"):
                break
            else:
                print("\tОшибка! Введите правильную букву:")
        print("\tКомпютер: " + comp_select)

        if player_select == comp_select:
            print("\tНичья!")
        elif player_select == "r" and comp_select == "w":
            comp_score = comp_score + 1
            print("\tВыиграл компьютер!")
        elif player_select == "r" and comp_select == "s":
            player_score = player_score + 1
            print("\tТвоя победа")
        elif player_select == "r" and comp_select == "p":
            comp_score = comp_score + 1
            print("\tВыиграл компьютер!")
        elif player_select == "w" and comp_select == "p":
            comp_score = comp_score + 1
            print("\tВыиграл компьютер!")
        elif player_select == "p" and comp_select == "r":
            player_score = player_score + 1
            print("\tТвоя победа!")
        elif player_select == "w" and comp_select == "s":
            player_score = player_score + 1
            print("\tТвоя победа!")
        elif player_select == "w" and comp_select == "r":
            player_score = player_score + 1
            print("\tТвоя победа!")
        elif player_select == "p" and comp_select == "s":
            comp_score = comp_score + 1
            print("Победил компьютер!")
        elif player_select == "s" and comp_select == "p":
            player_score = player_score + 1
            print("\tТвоя победа!")
        elif player_select == "s" and comp_select == "r":
            comp_score = comp_score + 1
            print("\tПобедил компьютер!")
        elif player_select == "p" and comp_select == "w":
            comp_score = comp_score + 1
            print("Победил компьютер!")
        elif player_select == "s" and comp_select == "w":
            comp_score = comp_score + 1
            print("Победил компьютер!")

    print("-------------------------------------")
    print("---------- РЕЗУЛЬТАТ ИГРЫ -----------")
    if player_score > comp_score:
        print("ПОЗДРАВЛЯЮ! Ты выиграл!")
        player_wins += 1
    elif comp_score > player_score:
        print("Извини, компьютер победил!")
        comp_wins += 1
    else:
        print("НИЧЬЯ!")
    player_score_all += player_score
    comp_score_all += comp_score

    print("Очки игрока: ",player_score_all," Победы игрока:",player_wins)
    print("Очки компьютера: ",comp_score_all," Победы компьютера: ",comp_wins)

    select_again = input("Хочешь сыграть снова?\n[y] - Да\n[n] - Нет\n")
    if select_again == "n":
        break
