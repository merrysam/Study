import numpy as np


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток(-ки)")


def game_core_v3(number: int=1) -> int:
    """ Делим множество чисел пополам, пока не найдем нужное число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    top_border = 101
    bottom_border = 1
    
    while True:
        predict = (top_border + bottom_border) // 2
            
        if predict == number:
            return count
        elif predict > number:
            top_border = predict
        else:
            bottom_border = predict
        count += 1
 
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)