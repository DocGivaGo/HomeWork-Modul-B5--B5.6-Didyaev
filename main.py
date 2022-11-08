maps = [1,2,3,                     #карта игры.
        4,5,6,
        7,8,9]

victories = [[0,1,2],              #указываем выигрышные комбинации. указываем не числа в карте, а соответствующие индексы.
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_maps():                   #функция выводит карту на экран
    print("----------")
    print(end="|")
    print(maps[0], end = " | ")
    print(maps[1], end = " | ")
    print(maps[2])
    print("----------")

    print(end="|")
    print(maps[3], end = " | ")
    print(maps[4], end = " | ")
    print(maps[5])
    print("----------")

    print(end="|")
    print(maps[6], end = " | ")
    print(maps[7], end = " | ")
    print(maps[8])
    print("----------")

def step_maps(step,symbol):          #функция реализует процессс хода в ячейку
    ind = maps.index(step)
    maps[ind] = symbol

def get_result():                    #функция реализует проверку выигрышной комбинации
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "Победил крестик!!!!!"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "Победил нолик!!!!!!"

    return win

game_over = False                     #сама игра
player = True

while game_over == False:

    print_maps()                      #показываем карту

    if player == True:                #спрашиваем у игроков куда они будут ходить
        symbol = "X"
        step = int(input("Уважаемы игрок №1, сделайте ход: "))
    else:
        symbol = "O"
        step = int(input("Уважаемый игрок №2 сделайте ход: "))

    step_maps(step,symbol)            #делаем ход в ячейку
    win = get_result()                #определяем победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player = not(player)

print_maps()
print ("Урааа!!!!!", win)