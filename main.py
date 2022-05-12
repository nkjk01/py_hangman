import random

wordlist = ["космос", "комета", "космонавт", "ракета", "метеорит","станция", "спутник", "планета", "звезда", ]

def hangman(word):
    wrong = 0
    stages = ["",
             "______      ",
             "|        |       ",
             "|        |       ",
             "|        O      ",
             "|       /|\     ",
             "|       / \     ",
             "|                "
              ]
    right_letter = list(word)
    board = ["-"] * len(word)
    win = False
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Угадайте букву: "
        char = input(msg)
        if char in right_letter:
            cind = right_letter \
                   .index(char)
            board[cind] = char
            right_letter[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "-" not in board:
            print("Вы победили!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("Вы проиграли! Загаданное слово - {}.".format(word))

hangman(random.choice(wordlist))
