
# Игра виселица
import random
words=['яблоко', 'апельсин', 'лимон', 'мандарин']
target=random.choice(words)
repeat_letter = []
wrong = 0   #отслеживает количество неправильных букв
actions = ["",                    #список рисования висельника
           "__________      ",
           "|               ",
           "|        |      ",
           "|        0      ",
           "|       /|\     ",
           "|       / \     ",
           "|               "
           ]
rletters = list(target)
board = ["__"] * len(target)
win = False
print("Начало игры. Казнь начинается!")

print(*board)
while wrong < len(actions) - 1:
        print("\n")
        char = input("Введите букву: ")
        count_char = 0   #количество повторяющихся букв
        if char in rletters:
            count_char = rletters.count(char)
            if count_char > 1:
                    for i in range(count_char):
                            s = rletters.index(char)
                            board[s] = char
                            rletters[s] = '#'
            else:
                s = rletters.index(char)
                board[s] = char
                rletters[s] = '#'
        else:
            wrong += 1
            print('Нет буквы', char)
        print((" ".join(board)))
        e = wrong + 1  #для среза
        print("\n".join(actions[0: e]))
        if "__" not in board:
            print("Вы счастливчик! Вас не казнили! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
if not win:
        print("\n".join(actions[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(target))













            

