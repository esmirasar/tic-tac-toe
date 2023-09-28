
print("_____Добро пожаловать в игру 'Крестики-нолики'!_____")
table = list(range(1, 10))
victory = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9),
           (3, 5, 7)]  # с помощью кортежа создаеи комбинации, в случае которых наступает победа



def print_table():  # c помощью данной функции будем рисовать игровое поле для пользователя
    for i in range(3):  # рисуем строки
        print('|', table[0 + i * 3], '|', table[1 + i * 3], '|', table[2 + i * 3], '|')


def game_process(move):  # функция принимает значение Х или О и определяет не занята ли клетка
    while True:
        user_data = input(
            f'''Укажите номер ячейки, в которую хотите поставить {move}:  ''')  # выводим сообщение пользователю с возможностью указать позицию
        if user_data not in set("123456789"):  # проверяем соблюдены ли условия границ игры
            print("Вы вышли за пределы игрового поля. Давайте повторим")
            continue
        if len(user_data) != 1:
            print("Значение должно быть одним символом (Х или О): ")
            continue
        else:
            user_data = int(user_data)
            if table[user_data - 1] == "X" or table[
                user_data - 1] == "O":  # указываем -1 потому что у пользователя таблица начинается с 1, а у нас список с 0 индекса
                print("Эта ячейка уже занята. Выберите другую.")
                continue
            else:
                table[user_data - 1] = move
                break


def player_victory():  # с помощью этой функции проверяем победные комбинации
    for j in victory:
        if (table[j[0] - 1]) == (table[j[1] - 1]) == (table[j[2] - 1]):  # циклом пробегаем каждый элемент кортежа, сдвиг на -1 т.к список начинается с 0, а у пользователя с 1
            return table[j[1] - 1]  # возвращаем значение если игра окончена
    return False  # если игра продолжается


def main():
    move_counter = 0
    while True:
        print_table()
        # четные ходы == х, нечетные == 0. Соответственно первым ходит 0
        if move_counter % 2 == 0:
            game_process("X")
        else:
            game_process("O")
        if move_counter > 3:
            examination = player_victory()  # если на поле уже более 3 позиций, то проверяем выигрышные комбинации
            if examination:
                print_table()
                print(f'''__________{examination} выигрывает!__________ ''')
                print("__________Спасибо за игру!_______")
                break
        move_counter += 1  # переходим на следующий ход
        # делаем проверку на окончание игры, если ничья
        if move_counter > 8:
            print_table()
            print("Ничья!")
            break


if __name__ == '__main__':
    main()
