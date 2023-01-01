from math import sqrt

def calc_sum_of_measured_angles(angles: tuple) -> float:
    '''
    Посчитает сумму углов
    Для этого надо сначала все углы перевести в десятичные градусы
    просуммировать и, вероятнее всего, разложить на гр/мин/сек
    '''
    
    return round(sum([get_decimal_angle(angle) for angle in angles]), 6)


def get_decimal_angle(angle: tuple[int, int, int]) -> float:
    ''' из гр/мин/сек раскладываю в десятичный угол '''
    
    return round(angle[0] + angle[1] / 60 + angle[2] / 3600, 6)


def get_dms_angle(angle: float) -> tuple[int, int, int]:
    ''' из десятичного угла получается гр/мин/сек '''
    
    d = int(angle)
    m = int((angle - d) * 60)
    s = int(round((angle - d - m / 60) * 3600, 0))
    
    return (d, m, s)


def calc_sum_of_theoretical_angles(n: int) -> float:
    ''' Посчитать теоретическую сумму углов в полигоне. В зависимости от количества углов. '''
    
    return 180 * (n - 2)


def calc_difference_ang(measured: float, should_be: float | int) -> float:
    ''' Посчитать разницу между теорией и практикой -> в десятичном виде возвращаю discrepancy '''
    
    return round(should_be - measured, 6)


def calc_amendments(discrepancy: float, n: int) -> float:
    ''' Посчитать, какую поправку надо вносить в каждый угол. будет в десятичном виде '''
    # Есть вопрос в том, можно ли будет ровно столько раскидывать и будут ли углы на самом деле хоть как-то меняться. Типа вдруг поправка будет пол секнды в кажды угол, ну куда это и как раскидывать тогда? надо потестить на различных задачах
    return discrepancy / n


def calc_permissible_discrepancy(n: int, accuracy: int = 1) -> float:
    ''' Посчитать допустимую невязку хода.
    Она зависит от ПРИБОРА, которым измеряют (двойная точность прибора) и от количества углов. Вдруг понадобится менять значение - я напишу параметр, но задам дефолтное значение 1 МИНУТУ, это для Т30. От того, какую величину пишут, будет зависеть то, в какой величине получается допуск. Если 1 минута, значит допуск в минутах, иначе в секундах. '''
    
    return round((accuracy * sqrt(n)) / 60, 6)      # / 60, т.к. я передал сюда 1 минуту и мне надо понимать, что невязка допустимая выражается в минуте, а не в градусах/секундах


def check_difference(calculated: float, theoretical: float) -> bool:
    ''' Проверка на допустимость вычисленной невязки относительно допустимой '''
    # Ещё не проверена
    return abs(calculated) < theoretical


def calc_correct_angle(angle: float, amendment: float) -> float:
    ''' Посчитать исправленный угол. ИМЕННО ОДИН угол. И вернуть его.
    Передаётся угол и поправка, которую вычислил раннее'''
    
    return round(angle + amendment, 6)

def create_dict_out_dms(dms: tuple[int, int, int]) -> dict:
    ''' Из кортежа (d, m, s) получить словарь вида {"Deg": d, "Min": m, "Sec": s} '''
    
    d, m, s = dms
    return {"Deg": d, "Min": m, "Sec": s}


def get_correct_angles(measured_angles: list[dict[str, int | float]]) -> dict[str, list | dict]:    # list[dict]
    ''' Вернуть массив словариков с исправленными углами. Это уже на фронт прокинуть можно
    На вход принимается массив словариков (в словарике значения, которые пользователь прописал: характеристики угла и расстояние)
    Формирую массив кортежей, где каждый кортеж, это собранные характеристики каждого угла ✔️
    Формирую список из углов в десятичной величине ✔️
    Прохожусь по нему формулами, получаю сумму измеренных углов, теоретическую сумму, невязку и поправку ✔️
    Делаю копию масива углов в десятичной величине, в этой копии я внесу поправку в каждый угол ✔️
    Потом пройдусь по каждому элементу массива, сформирую из каждого элемента угол в виде d/m/s и сформирую массив словариков, что б вернуть на фронт ✔️
    Верну словарь JSON в котором есть ключи: углы, сумма измеренных углов, теоретическая сумма углов, невязка, теоретическая невязка, сумма исправленных углов'''
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles(list_of_angles) # type: ignore
    # sum_of_angles_dms = get_dms_angle(sum_of_angles)
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles))
    difference = calc_difference_ang(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    permissible_difference = calc_permissible_discrepancy(len(list_of_angles))  # Допустимая невязка
    correct_angles = [calc_correct_angle(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    sum_correct_angles = calc_sum_of_measured_angles(correct_angles)    # получается вот так...(2159, 59, 60) Возможно надо будет обработку этого дела внутрь функции какой-нибудь запихнуть, что б такого не было. До этого зачем-то к int приводил, поэтому терял десятичную часть, которая была важна, т.к. сумма всех углов, почему-то, получается с таким округлением -_- 2159.9999999999995
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    
    # data_out = {"angles": correct_angles, "sum_measured_angles": sum_of_angles, "theoretical_sum_of_angles": theoretical_sum_of_angles, "difference": difference, "permissible_difference": permissible_difference, "sum_correct_angles": sum_correct_angles}
    
    data_out = {
        "angles": correct_angles, 
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_correct_angles))
        }
    
    return data_out

# print(get_sum_of_measured_angles.__doc__)
# print(get_decimal_ange.__doc__)