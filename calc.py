from math import sqrt
import json
import math


def calc_sum_of_measured_angles(angles: list[tuple[int, int, int]]) -> float:
    '''
    Посчитает сумму углов
    Для этого надо сначала все углы перевести в десятичные градусы
    просуммировать и, вероятнее всего, разложить на гр/мин/сек
    '''
    
    return round(sum([get_decimal_angle(angle) for angle in angles]), 6)


def calc_sum_of_measured_angles1(angles: list[tuple[int, int, int]]) -> float:
    '''
    Посчитает сумму углов
    Для этого надо сначала все углы перевести в десятичные градусы
    просуммировать и, вероятнее всего, разложить на гр/мин/сек
    '''
    
    return sum([get_decimal_angle(angle) for angle in angles])


def calc_sum_of_corrected_angles(angles: list[float], theoretical) -> float:
    '''
    Посчитает сумму исправленных углов
    Для этого надо сначала все углы перевести в десятичные градусы (они уже должны будут быть в таком виде, по идее. Только для вывода они переводятся в d/m/s)?
    просуммировать. Обычно исправленная сумма должна быть равна числу теоретической суммы. Обычно там целое число. Если это не так, то надо при вычислении суммы использовать исправленные углы, не округлённые до 6 знаков.
    Что б проверить, надо будет беревести в d/m/s, ну и для вышенаписанного условия надо бы передавать или использовать функцию для вычисления теоретическомй суммы и всё. Но лучше передавать, т.к. она уже вычислена будет в программе, по идее
    '''
    
    summa = sum(angles)
    allowable_error = get_decimal_angle((0, 0, 5))  # Допустимая погрешность, для Ваниной таблицы это 5". Исправленные углы в десятичном виде у него дают теоретическую сумму. Где-то я читал про то, что в углы не надо раскидывать меньше 0.1' т.е. 6", эту обработку потом можно будет попробовать накрутить. Но в общем, у него получились углы немного другие, когда он их переводил в d/m/s. Поэтому если сидеть их и складывать, то в них потеряется 5"
    
    if abs(summa - theoretical) < allowable_error:
        return theoretical
    else:
        print("Полученная сумма исправленных углов не сходится с теорией больше чем на 5 секунд")
        return summa     # type: ignore


def get_decimal_angle(angle: tuple[int, int, int]) -> float:
    ''' из гр/мин/сек раскладываю в десятичный угол '''
    
    return round(angle[0] + angle[1] / 60 + angle[2] / 3600, 6)


def get_decimal_angle1(angle: tuple[int, int, int]) -> float:
    ''' из гр/мин/сек раскладываю в десятичный угол '''
    
    return angle[0] + angle[1] / 60 + angle[2] / 3600


def get_dms_angle(angle: float) -> tuple[int, int, int]:
    ''' из десятичного угла получается гр/мин/сек '''
    
    d = int(angle)
    m = int((angle - d) * 60)
    s = int(round((angle - d - m / 60) * 3600, 0))
    
    return (d, m, s)


def calc_sum_of_theoretical_angles(n: int, side: str = 'right') -> float:
    '''Посчитать теоретическую сумму углов в полигоне. В зависимости от количества углов.
    Если в полигоне измерялись внутренние углы "Правые по ходу движени", то формула:
    180 * (n - 2), иначе 180 * (n + 2)'''
    
    res = 180 * (n - 2) if side == 'right' else 180 * (n + 2)
    
    return res


def calc_difference_ang(measured: float, should_be: float | int) -> float:
    ''' Посчитать разницу между теорией и практикой -> в десятичном виде возвращаю discrepancy '''
    
    return round(should_be - measured, 6)


def calc_difference_ang1(measured: float, should_be: float | int) -> float:
    ''' Посчитать разницу между теорией и практикой -> в десятичном виде возвращаю discrepancy '''
    
    return should_be - measured


def calc_amendments(discrepancy: float, n: int) -> float:
    ''' Посчитать, какую поправку надо вносить в каждый угол. будет в десятичном виде '''
    # Есть вопрос в том, можно ли будет ровно столько раскидывать и будут ли углы на самом деле хоть как-то меняться. Типа вдруг поправка будет пол секнды в кажды угол, ну куда это и как раскидывать тогда? надо потестить на различных задачах
    return discrepancy / n


def calc_permissible_discrepancy(n: int, accuracy: int = 1) -> float:
    ''' Посчитать допустимую невязку хода.
    Она зависит от ПРИБОРА, которым измеряют (двойная точность прибора) и от количества углов. Вдруг понадобится менять значение - я напишу параметр, но задам дефолтное значение 1 МИНУТУ, это для Т30. От того, какую величину пишут, будет зависеть то, в какой величине получается допуск. Если 1 минута, значит допуск в минутах, иначе в секундах. '''
    
    return round((accuracy * sqrt(n)) / 60, 6)      # / 60, т.к. я передал сюда 1 минуту и мне надо понимать, что невязка допустимая выражается в минуте, а не в градусах/секундах


def calc_permissible_discrepancy1(n: int, accuracy: int = 1) -> float:
    ''' Посчитать допустимую невязку хода.
    Она зависит от ПРИБОРА, которым измеряют (двойная точность прибора) и от количества углов. Вдруг понадобится менять значение - я напишу параметр, но задам дефолтное значение 1 МИНУТУ, это для Т30. От того, какую величину пишут, будет зависеть то, в какой величине получается допуск. Если 1 минута, значит допуск в минутах, иначе в секундах. '''
    
    return (accuracy * sqrt(n)) / 60      # / 60, т.к. я передал сюда 1 минуту и мне надо понимать, что невязка допустимая выражается в минуте, а не в градусах/секундах


def check_difference(calculated: float, theoretical: float) -> bool:
    ''' Проверка на допустимость вычисленной невязки относительно допустимой '''
    # Ещё не проверена
    return abs(calculated) < theoretical


def calc_correct_angle(angle: float, amendment: float) -> float:
    ''' Посчитать исправленный угол. ИМЕННО ОДИН угол. И вернуть его.
    Передаётся угол и поправка, которую вычислил раннее'''
    
    return round(angle + amendment, 6)


def calc_correct_angle1(angle: float, amendment: float) -> float:
    ''' Посчитать исправленный угол. ИМЕННО ОДИН угол. И вернуть его.
    Передаётся угол и поправка, которую вычислил раннее'''
    
    return angle + amendment


def create_dict_out_dms(dms: tuple[int, int, int]) -> dict:
    ''' Из кортежа (d, m, s) получить словарь вида {"Deg": d, "Min": m, "Sec": s} '''
    
    d, m, s = dms
    return {"Deg": d, "Min": m, "Sec": s}


def calc_sum_of_distance(list_dist: list[float]):
    '''Посчитать периметр хода. Не включаеся дистанция из последней точки. Т.к. там не должно быть расстояния. Либо если есть, то это между двумя исходными пунктами расстояние.'''
    
    return round(sum(list_dist), 3)


def calc_next_bearing(prev_bearing: float, corrected_angle: float, side: str ='right') -> float:
    '''Буду передавать предыдущий дирекционный угол и исправленный горизонтальный угол на пункте. Возвращать вычисленный дирекционный угол. Буду использовать это в цикле для добавления в список. Возможно использовать side что б использовать разные формулы для добавления исправленного горизонтального угла с различным знаком'''
    
    bearing = 0
    
    if side == 'right':
        if prev_bearing + 180 - corrected_angle < 0:
            bearing = prev_bearing + 180 - corrected_angle + 360
        elif prev_bearing + 180 - corrected_angle > 360:
            bearing = prev_bearing + 180 - corrected_angle - 360
        else:
            bearing = prev_bearing + 180 - corrected_angle
    elif side == 'left':
        if prev_bearing - 180 + corrected_angle < 0:
            bearing = prev_bearing - 180 + corrected_angle + 360
        elif prev_bearing - 180 + corrected_angle > 360:
            bearing = prev_bearing - 180 + corrected_angle - 360
        else:
            bearing = prev_bearing - 180 + corrected_angle
    
    return bearing


def get_all_bearing_angles(start_bearing: float, correct_angles: list[float], side: str ='right'):
    '''Посчитать все дирекционные углы, исходя из того, какой начальный дир.угол и какие исправленные углы были получены. Учитывается сторона, с который проводились вычисления относительно хода полигона.'''
    
    previous_bearing = start_bearing    # Изначально предыдущий дир.угол будет переданный начальный. Потом надо будет в цикле подменять на следующий вычисленный
    bearingAngles = []
    # [ang + start_bearing for ang in correct_angles]
    
    for ang in correct_angles:
        present_bearing = calc_next_bearing(previous_bearing, ang, side)
        bearingAngles.append(present_bearing)
        previous_bearing = present_bearing
    
    return bearingAngles


def calc_coordinate_increments(list_dist: list[float], bearingAngles: list[float]):
    '''Передаётся список расстояний и список дирекционных углов, что б посчитать первичные приращения координат. Функция посчитает приращения для каждого пункта и вернёт список из приращений кородинат (incX, incY), в следующей формуле надо будет возвращать исправленные (incXcor, incYcor)
    С этими списками надо работать только в армках количества записей о расстояниях. Дир. углов приходит на один больше, его не надо использовать, прохожусь циклом по спискам только от 0 до len(list_dist)'''
    
    coordinate_increments = [(round(math.cos(math.radians(bearingAngles[i])) * list_dist[i], 3),
                              round(math.sin(math.radians(bearingAngles[i])) * list_dist[i], 3)) for i in range(len(list_dist))]
    
    # Для всех возможных последующих вычислений я могу не округлять до 3х знаков. Т.к. в данном примере практическая сумма приращений по Y получилась меньше на 1 мм. Важно это или нет⁉️❓
    # coordinate_increments = [(math.cos(math.radians(bearingAngles[i])) * list_dist[i],
    #                           math.sin(math.radians(bearingAngles[i])) * list_dist[i]) for i in range(len(list_dist))]
    
    return coordinate_increments


def calc_coordinate_increments1(list_dist: list[float], bearingAngles: list[float]):
    '''Передаётся список расстояний и список дирекционных углов, что б посчитать первичные приращения координат. Функция посчитает приращения для каждого пункта и вернёт список из приращений кородинат (incX, incY), в следующей формуле надо будет возвращать исправленные (incXcor, incYcor)
    С этими списками надо работать только в армках количества записей о расстояниях. Дир. углов приходит на один больше, его не надо использовать, прохожусь циклом по спискам только от 0 до len(list_dist)'''
    
    coordinate_increments = [(math.cos(math.radians(bearingAngles[i])) * list_dist[i],
                              math.sin(math.radians(bearingAngles[i])) * list_dist[i]) for i in range(len(list_dist))]
    
    # Для всех возможных последующих вычислений я могу не округлять до 3х знаков. Т.к. в данном примере практическая сумма приращений по Y получилась меньше на 1 мм. Важно это или нет⁉️❓
    # coordinate_increments = [(math.cos(math.radians(bearingAngles[i])) * list_dist[i],
    #                           math.sin(math.radians(bearingAngles[i])) * list_dist[i]) for i in range(len(list_dist))]
    
    return coordinate_increments


def calc_coordinate_increment_correct(list_coordinate_increments: list[tuple[float, float]], list_dist: list[float], difference_inc: tuple[float, float], perimetr: float):
    '''Посчитает исправленные приращения координат. Вроде вышенаписанная функция не нужна, можно тут всё в одном цикле замутить, если не ошибаюсь, не обязательно так много делегировать и делать функцию для сбора в список в целую одну функцию'''
    
    # мне надо взять невязку по X/Y умножить на дистанцию, делённую на периметр хода
    
    increment_correct = [(round(list_coordinate_increments[i][0] + (difference_inc[0] * list_dist[i] / perimetr), 3),
                          round(list_coordinate_increments[i][1] + (difference_inc[1] * list_dist[i] / perimetr), 3))
                         for i in range(len(list_coordinate_increments))]
    
    return increment_correct


def calc_coordinate_increment_correct1(list_coordinate_increments: list[tuple[float, float]], list_dist: list[float], difference_inc: tuple[float, float], perimetr: float):
    '''Посчитает исправленные приращения координат. Вроде вышенаписанная функция не нужна, можно тут всё в одном цикле замутить, если не ошибаюсь, не обязательно так много делегировать и делать функцию для сбора в список в целую одну функцию'''
    
    # мне надо взять невязку по X/Y умножить на дистанцию, делённую на периметр хода
    
    increment_correct = [(list_coordinate_increments[i][0] + (difference_inc[0] * list_dist[i] / perimetr),
                          list_coordinate_increments[i][1] + (difference_inc[1] * list_dist[i] / perimetr))
                         for i in range(len(list_coordinate_increments))]
    
    return increment_correct


def calc_all_coordinates(initial_coord: list[tuple[float, float]], increment_correct: list[tuple[float, float]]) -> list[tuple[float, float]]:
    '''Посчитаю все координаты, которые надо посчитать, объединю с исходными и верну в скрипт для передачи'''
    
    prev_coord = initial_coord[0]
    coords = []
    
    for inc in increment_correct:
        calculated_coords = (round(prev_coord[0] + inc[0], 3), round(prev_coord[1] + inc[1], 3))
        coords.append(calculated_coords)
        prev_coord = calculated_coords
    
    coords_out = coords[:]
    coords_out.insert(0, initial_coord[0])
    return coords_out


def calc_all_coordinates1(initial_coord: list[tuple[float, float]], increment_correct: list[tuple[float, float]]) -> list[tuple[float, float]]:
    '''Посчитаю все координаты, которые надо посчитать, объединю с исходными и верну в скрипт для передачи'''
    
    prev_coord = initial_coord[0]
    coords = []
    
    for inc in increment_correct:
        calculated_coords = (prev_coord[0] + inc[0], prev_coord[1] + inc[1])
        coords.append(calculated_coords)
        prev_coord = calculated_coords
    
    coords_out = coords[:]
    coords_out.insert(0, initial_coord[0])
    return coords_out


def get_result(data: dict[str, list[dict[str, int | float]] | dict[str, int | float]]) -> dict[str, list | dict]:    # 
    
    measured_angles: list[dict[str, int | float]] = data.get('aPoints')
    bearingAngle: dict[str, int] = data.get('bearingAngle')
    initial_coords: list[dict[str, float]] = data.get('coords')         # Должно находиться 2 координаты всего лишь, начальная и конечная. С первой строки и последней в вебе должны собираться эти точки. Когда будут просчитываться все коориднаты, программа должна посчиатть ещё сама и последнюю координату и сравнить её с той, которую передали. 
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles(list_of_angles) # type: ignore
    
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), 'left')
    difference = calc_difference_ang(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    permissible_difference = calc_permissible_discrepancy(len(list_of_angles))  # Допустимая невязка
    correct_angles = [calc_correct_angle(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore decimal
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, 'left')    # list[decimal, ...]
    bearingAngles_dms = [get_dms_angle(bA) for bA in bearingAngles]
    bearingAngles_dms_dict = [create_dict_out_dms(bA) for bA in bearingAngles_dms]
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]
    perimeter = calc_sum_of_distance(list_dist)
    
    list_coordinate_increments = calc_coordinate_increments(list_dist, bearingAngles)   # Приращения координат
    list_dict_coordinate_increments = [{"incX": X, "incY": Y} for X, Y in list_coordinate_increments]
    
    list_initial_coords = [(d.get('X'), d.get('Y')) for d in initial_coords]    # Начальные переданные координаты
    
    # Следующие переменные лежат в кортеже (X, Y)
    # !!!!!!! Т.к. я начал уже округлять где-то до этого вычисляемые значения, то и тут везде я тоже округляю, что б видеть и понимать нормально, что получается в итоге
    # (Я наверное, так сделал, что б сразу эти занчения передавать на фронт, хотя хз)
    # возможно придётся переделывать всё без округлений и только для вывода на отображение округялть в отдельных функциях....
    sum_theoretical_coordinate_increments = (round(list_initial_coords[1][0] - list_initial_coords[0][0], 3), 
                                             round(list_initial_coords[1][1] - list_initial_coords[0][1], 3))   # Конечная координата - начальная координата
    sum_calculated_coordinate_increments = (round(sum([d[0] for d in list_coordinate_increments]), 3), 
                                            round(sum([d[1] for d in list_coordinate_increments]), 3))          # Просто просуммировал вычисленыне приращения
    difference_increments = (round(sum_theoretical_coordinate_increments[0] - sum_calculated_coordinate_increments[0], 3), 
                             round(sum_theoretical_coordinate_increments[1] - sum_calculated_coordinate_increments[1], 3))  # Теория - практика, что б в следующих вычислениях не пришлось брать невязку с обратным знаком...
    difference_abs = math.hypot(difference_increments[0], difference_increments[1]) # fабс
    difference_relative = (difference_abs / perimeter, 1 / (difference_abs / perimeter)) # fотн Сразу перевёл в удобный вариант масштаба, там всё зависит от разряда теодолитного хода, вот относительно разряда не должно превышать это число. Типа если это условие будет выполняться, то можно приступать к вычислению исправленных приращений координат. Возможно в будущем надо будет придумать эту проверку. ❓ Если число получается больше 0.0005 (это первый разряд 1:2000), например, 0.00019, то значит это хорошо
    
    coordinate_increment_correct = calc_coordinate_increment_correct(list_coordinate_increments, list_dist, difference_increments, perimeter)   # Исправленные приращения координат
    list_dict_coordinate_increment_correct = [{"incXcor": X, "incYcor": Y} for X, Y in coordinate_increment_correct]
    
    all_coords = calc_all_coordinates(list_initial_coords, coordinate_increment_correct)
    all_coords_dict = [{"X": X, "Y": Y} for X, Y in all_coords]
    
    data_out = {
        "angles": correct_angles,
        "bearing_angles": bearingAngles_dms_dict,
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "perimetr": perimeter,
        "coordinate_increments": list_dict_coordinate_increments,
        "coordinate_increment_correct": list_dict_coordinate_increment_correct,
        "all_coords": all_coords_dict
        }
    
    # return sum_cor, sum_correct_angles
    return data_out


def get_result1(data: dict[str, list[dict[str, int | float]] | dict[str, int | float]]) -> dict[str, list | dict]:    # 
    '''Эта функция сработает только если измерялись левые углы по ходу движения, ход был по часовой стрелке (т.е. эти углы были внешними в многоугольнике. Из-за этого по-другому вычислялось теоретическое значение углов'''
    
    measured_angles: list[dict[str, int | float]] = data.get('aPoints')
    bearingAngle: dict[str, int] = data.get('bearingAngle')
    initial_coords: list[dict[str, float]] = data.get('coords')         # Должно находиться 2 координаты всего лишь, начальная и конечная. С первой строки и последней в вебе должны собираться эти точки. Когда будут просчитываться все коориднаты, программа должна посчиатть ещё сама и последнюю координату и сравнить её с той, которую передали. 
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle1(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles1(list_of_angles) # type: ignore
    
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), 'left')
    difference = calc_difference_ang1(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    
    permissible_difference = calc_permissible_discrepancy1(len(list_of_angles))  # Допустимая невязка
    
    correct_angles = [calc_correct_angle1(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore decimal
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, 'left')    # list[decimal, ...]
    bearingAngles_dms = [get_dms_angle(bA) for bA in bearingAngles]
    bearingAngles_dms_dict = [create_dict_out_dms(bA) for bA in bearingAngles_dms]
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]
    perimeter = calc_sum_of_distance(list_dist)
    
    list_coordinate_increments = calc_coordinate_increments1(list_dist, bearingAngles)   # Приращения координат
    list_dict_coordinate_increments = [{"incX": round(X, 3), "incY": round(Y, 3)} for X, Y in list_coordinate_increments]   # Округляю только при сохранении информации, в таком виде будет передаваться для оттображения
    
    list_initial_coords = [(d.get('X'), d.get('Y')) for d in initial_coords]    # Начальные переданные координаты
    
    # Следующие переменные лежат в кортеже (X, Y)
    # !!!!!!! Т.к. я начал уже округлять где-то до этого вычисляемые значения, то и тут везде я тоже округляю, что б видеть и понимать нормально, что получается в итоге
    # (Я наверное, так сделал, что б сразу эти занчения передавать на фронт, хотя хз)
    # возможно придётся переделывать всё без округлений и только для вывода на отображение округялть в отдельных функциях....
    sum_theoretical_coordinate_increments = (list_initial_coords[1][0] - list_initial_coords[0][0], 
                                             list_initial_coords[1][1] - list_initial_coords[0][1])   # Конечная координата - начальная координата
    sum_calculated_coordinate_increments = (sum([d[0] for d in list_coordinate_increments]), 
                                            sum([d[1] for d in list_coordinate_increments]))          # Просто просуммировал вычисленыне приращения
    difference_increments = (sum_theoretical_coordinate_increments[0] - sum_calculated_coordinate_increments[0], 
                             sum_theoretical_coordinate_increments[1] - sum_calculated_coordinate_increments[1])  # Теория - практика, что б в следующих вычислениях не пришлось брать невязку с обратным знаком...
    
    difference_abs = math.hypot(difference_increments[0], difference_increments[1]) # fабс
    difference_relative = (difference_abs / perimeter, 1 / (difference_abs / perimeter)) # fотн Сразу перевёл в удобный вариант масштаба, там всё зависит от разряда теодолитного хода, вот относительно разряда не должно превышать это число. Типа если это условие будет выполняться, то можно приступать к вычислению исправленных приращений координат. Возможно в будущем надо будет придумать эту проверку. ❓ Если число получается больше 0.0005 (это первый разряд 1:2000), например, 0.00019, то значит это хорошо
    
    coordinate_increment_correct = calc_coordinate_increment_correct1(list_coordinate_increments, list_dist, difference_increments, perimeter)   # Исправленные приращения координат
    
    list_dict_coordinate_increment_correct = [{"incXcor": round(X, 3), "incYcor": round(Y, 3)} for X, Y in coordinate_increment_correct]    # Округление для отображения нормальных чисел
    
    all_coords = calc_all_coordinates1(list_initial_coords, coordinate_increment_correct)
    all_coords_dict = [{"X": round(X, 3), "Y": round(Y, 3)} for X, Y in all_coords]
    
    data_out = {
        "angles": correct_angles,
        "bearing_angles": bearingAngles_dms_dict,
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "perimetr": perimeter,
        "coordinate_increments": list_dict_coordinate_increments,
        "coordinate_increment_correct": list_dict_coordinate_increment_correct,
        "all_coords": all_coords_dict
        }
    
    return data_out


def get_correct_angles2(measured_angles: list[dict[str, int | float]], bearingAngle: dict[str, int]) -> dict[str, list | dict]:    # list[dict]
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles(list_of_angles) # type: ignore
    
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), 'left')
    difference = calc_difference_ang(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    permissible_difference = calc_permissible_discrepancy(len(list_of_angles))  # Допустимая невязка
    
    correct_angles = [calc_correct_angle(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore decimal
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, 'left')    # list[decimal, ...]
    bearingAngles_dms = [get_dms_angle(bA) for bA in bearingAngles]
    bearingAngles_dms_dict = [create_dict_out_dms(bA) for bA in bearingAngles_dms]
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]
    perimeter = calc_sum_of_distance(list_dist)
    
    list_coordinate_increments = calc_coordinate_increments(list_dist, bearingAngles)
    list_dict_coordinate_increments = [{"incX": X, "incY": Y} for X, Y in list_coordinate_increments]
    
    
    
    calc_coordinate_increment_correct(list_coordinate_increments, list_dist, difference_inc, perimeter)
    
    data_out = {
        "angles": correct_angles,
        "bearing_angles": bearingAngles_dms_dict,
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "coordinate_increments": list_dict_coordinate_increments,
        "perimetr": perimeter
        }
    
    # return sum_cor, sum_correct_angles
    return data_out


def get_correct_angles(measured_angles: list[dict[str, int | float]], bearingAngle: dict[str, int]) -> dict[str, list | dict]:    # list[dict]
    ''' Вернуть массив словариков с исправленными углами. Это уже на фронт прокинуть можно
    На вход принимается массив словариков (в словарике значения, которые пользователь прописал: характеристики угла и расстояние)
    Формирую массив кортежей, где каждый кортеж, это собранные характеристики каждого угла ✔️
    Формирую список из углов в десятичной величине ✔️
    Прохожусь по нему формулами, получаю сумму измеренных углов, теоретическую сумму, невязку и поправку ✔️
    Делаю копию масива углов в десятичной величине, в этой копии я внесу поправку в каждый угол ✔️
    Потом пройдусь по каждому элементу массива, сформирую из каждого элемента угол в виде d/m/s и сформирую массив словариков, что б вернуть на фронт ✔️
    Верну словарь JSON в котором есть ключи: углы, сумма измеренных углов, теоретическая сумма углов, невязка, теоретическая невязка, сумма исправленных углов'''
    
    # Сюда надо передавать полностью большой словарик, который передаётся с фронта. Что б не протерять дирекционные углы и исходные координаты.
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    # print(list_of_angles)
    list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles(list_of_angles) # type: ignore
    # sum_of_angles_dms = get_dms_angle(sum_of_angles)
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles))
    difference = calc_difference_ang(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    permissible_difference = calc_permissible_discrepancy(len(list_of_angles))  # Допустимая невязка
    correct_angles = [calc_correct_angle(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    # После получения исправленных углов decimal надо просчитать дирекционные углы сразу. Потом проделать такую же процедуру, как с исправленными, чтобы передавать на фронт
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore d/m/s
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, 'right')
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    sum_correct_angles = calc_sum_of_measured_angles(correct_angles)    # получается вот так...(2159, 59, 60) Возможно надо будет обработку этого дела внутрь функции какой-нибудь запихнуть, что б такого не было. До этого зачем-то к int приводил, поэтому терял десятичную часть, которая была важна, т.к. сумма всех углов, почему-то, получается с таким округлением -_- 2159.9999999999995
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]
    perimeter = calc_sum_of_distance(list_dist)
    
    # data_out = {"angles": correct_angles, "sum_measured_angles": sum_of_angles, "theoretical_sum_of_angles": theoretical_sum_of_angles, "difference": difference, "permissible_difference": permissible_difference, "sum_correct_angles": sum_correct_angles}
    
    data_out = {
        "angles": correct_angles, 
        "bearing_angles": bearingAngles,
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        # "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_correct_angles)),
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "perimetr": perimeter
        }
    
    # return perimeter
    return data_out


def get_correct_angles1(measured_angles: list[dict[str, int | float]], bearingAngle: dict[str, int]) -> dict[str, list | dict]:    # list[dict]
    '''Просчитывать корректные углы, если по теодолитному ходу измеряли левые углы по ходу движения....'''
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles(list_of_angles) # type: ignore
    # sum_of_angles_dms = get_dms_angle(sum_of_angles)
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), 'left')
    difference = calc_difference_ang(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    permissible_difference = calc_permissible_discrepancy(len(list_of_angles))  # Допустимая невязка
    correct_angles = [calc_correct_angle(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore d/m/s
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, 'left')
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]
    perimeter = calc_sum_of_distance(list_dist)
    
    # data_out = {"angles": correct_angles, "sum_measured_angles": sum_of_angles, "theoretical_sum_of_angles": theoretical_sum_of_angles, "difference": difference, "permissible_difference": permissible_difference, "sum_correct_angles": sum_correct_angles}
    
    data_out = {
        "angles": correct_angles,
        "bearing_angles": bearingAngles,    # Я ПЕРЕДАЮ УГЛЫ В ВИДЕ D/M/S ЗАВТРА БЫ ПЕРЕДЕЛАТЬ В НОРМАЛЬНЫЙ СПИСОК ДЛЯ ПЕРЕДАЧИ В НОРМАЛЬНЫЙ ВИД НА ФРОНТ
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "perimetr": perimeter
        }
    
    # return sum_cor, sum_correct_angles
    return data_out




# def send_test_data():
#     '''Отослать тестовые данные (Измеренные углы + расстояния)'''
    
#     with open("DataInput.json", "r", encoding="utf-8") as f:
#         data_inp = json.loads(f.read())

#     return(data_inp)


def send_test_data(path: str):
    '''Отослать тестовые данные (Измеренные углы + расстояния)'''
    
    with open(path, "r", encoding="utf-8") as f:
        data_inp = json.loads(f.read())

    return(data_inp)

# print(get_sum_of_measured_angles.__doc__)
# print(get_decimal_ange.__doc__)