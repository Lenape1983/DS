import game_v2
import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # обьявляем счетчик
    count = 0 
    # устаналиваем границы для генерации случайных чисел
    first = 1
    last = 101  
    while True:
        count += 1
        predict_number = np.random.randint(first, last)
        if predict_number > number:
            last = predict_number  # изменяем верхний диапазон случайных чисел
        elif predict_number < number:
            first = predict_number + 1  # изменяем нижний диапазон случайных чисел
        else:
            break
    return count


if __name__ == "__main__":
    # RUN
    game_v2.score_game(game_core_v3)