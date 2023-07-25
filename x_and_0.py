cell = [' '] * 9
#field
def field_cells():
    print('|', cell[0], '|', cell[1], '|', cell[2], '|')
    print('--1---2---3--')
    print('|', cell[3], '|', cell[4], '|', cell[5], '|')
    print('--4---5---6--')
    print('|', cell[6], '|', cell[7], '|', cell[8], '|')
    print('--7---8---9--')
# Варианты выигрыша
def check_win_vars():
    vars = [
        # горизонт
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # вертикал
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # диагональ
        [0, 4, 8], [2, 4, 6]
    ]
    for i in vars:
        if cell[i[0]] == cell[i[1]] == cell[i[2]] != ' ':
            return True
        # else:
    return False

def deal(player):
    pos = int(input(f'Очередь {player}.\nЯчейка 1-9: ')) - 1
    if pos in range(9) and cell[pos] == ' ':
        cell[pos] = player
    else:
        print(f'Ячейка вне диапазона (1-9).\nОчередь {player}.\nЯчейка 1-9: ')
# Game
def play():
    # Х gamer
    curplayer = 'X'
    while True:
        field_cells()
        deal(curplayer)
        if check_win_vars():
            field_cells()
            print(f'Игра окончена.\nПобеда игрока {curplayer}!!!')
            break
        if ' ' not in cell:
            field_cells()
            print(f'Игра окончена.\nНичья.')
            break
        # 0 gamer
        curplayer = 'O' if curplayer == 'X' else 'X'
play()
