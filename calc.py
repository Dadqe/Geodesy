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
    # !!! Тут пробую тоже использовать функцию без округления. До 15.02.23 использовалась функция перевода в десятичную меру с округлением до 6 знаков get_decimal_angle
    return sum([get_decimal_angle1(angle) for angle in angles])


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
    ''' из гр/мин/сек раскладываю в десятичный угол и округляю до 6 знаков после запятой '''
    
    return round(angle[0] + angle[1] / 60 + angle[2] / 3600, 6)


def get_decimal_angle1(angle: tuple[int, int, int]) -> float:
    ''' из гр/мин/сек раскладываю в десятичный угол без округления, что б не запортачить дальнейшие вычисления '''
    
    return angle[0] + angle[1] / 60 + angle[2] / 3600


def get_dms_angle(angle: float) -> tuple[int, int, int]:
    ''' из десятичного угла получается гр/мин/сек '''
    
    d = int(angle)
    m = int((angle - d) * 60)
    s = int(round((angle - d - m / 60) * 3600, 0))
    
    return (d, m, s)


def calc_sum_of_theoretical_angles(n: int, side: str = 'inner') -> float:
    # НАДО ПОМЕНЯТЬ АТРИБУТ side outer or inner , вычислять этот параметр надо до этого, что б понимать, внешние по периметру или внутренние углы измерялись
    '''Посчитать теоретическую сумму углов в полигоне. В зависимости от количества углов.
    Если в полигоне измерялись внутренние углы "Правые по ходу движения", то формула:
    180 * (n - 2) ДЛЯ углов ВНУТРИ фигуры, которую образовывает полигон, иначе 180 * (n + 2) ДЛЯ ВНЕШНИХ углов фигуры'''
    
    res = 180 * (n - 2) if side == 'inner' else 180 * (n + 2)
    
    return res


def calc_difference_ang(measured: float, should_be: float | int) -> float:
    ''' Посчитать разницу между теорией и практикой -> в десятичном виде возвращаю discrepancy '''
    
    return round(should_be - measured, 6)


def calc_difference_ang1(measured: float, should_be: float | int) -> float:
    ''' Посчитать разницу между теорией и практикой -> в десятичном виде возвращаю discrepancy '''
    
    return should_be - measured


def calc_amendments(discrepancy: float, n: int) -> float:
    ''' Посчитать, какую поправку надо вносить в каждый угол. будет в десятичном виде '''
    # Есть вопрос в том, можно ли будет ровно столько раскидывать и будут ли углы на самом деле хоть как-то меняться. Типа вдруг поправка будет пол секнды в кажды угол, ну куда это и как раскидывать тогда? надо потестить на различных задачах.
    
    # !!! Есть очень важный вопрос в том, что в некоторых текстах пишут, что нет смысла рскидыать невязки, если она меньше 0.1' надо это проверить и попытаться учитывать это, если придётся
    
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
    # bearingAngles = [start_bearing]   # Вообще, если созадвать форму, как мы часто делали в универе, как вот у Вани в расчётах и моих, то в первых двух строках должны находиться два исходных пункта и поэтому исходный дир. угол стоило бы поместить между ними, а для этого его надо будет тоже передать, но на счёт этого подумать ещё стоит, как правильно формировать. Закладная есть.
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
    
    return coordinate_increments


def calc_coordinate_increment_correct(list_coordinate_increments: list[tuple[float, float]], list_dist: list[float], difference_inc: tuple[float, float], perimetr: float):
    '''Посчитает исправленные приращения координат. Вроде вышенаписанная функция не нужна, можно тут всё в одном цикле замутить, если не ошибаюсь, не обязательно так много делегировать и делать функцию для сбора в список в целую одну функцию'''
    
    # мне надо взять невязку по X/Y умножить на дистанцию, делённую на периметр хода
    
    increment_correct = [(round(list_coordinate_increments[i][0] + (difference_inc[0] * list_dist[i] / perimetr), 3),
                          round(list_coordinate_increments[i][1] + (difference_inc[1] * list_dist[i] / perimetr), 3))
                         for i in range(len(list_coordinate_increments))]
    
    return increment_correct


def calc_coordinate_increment_correct1(list_coordinate_increments: list[tuple[float, float]], list_dist: list[float], difference_inc: tuple[float, float], perimetr: float):
    '''Посчитает исправленные приращения координат. Вроде вышенаписанная функция не нужна, можно тут всё в одном цикле замутить, если не ошибаюсь, не обязательно так много делегировать и делать функцию для сбора в список в целую одну функцию. Но пускай так, зато отдельная функция считает, если тут будут проблемыЫ, проще создать тестовые данные и посмотреть'''
    
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
    coords = [initial_coord[0]]
    
    for inc in increment_correct:
        calculated_coords = (prev_coord[0] + inc[0], prev_coord[1] + inc[1])
        coords.append(calculated_coords)
        prev_coord = calculated_coords
    
    return coords

# 15.02.23
def get_result3(data: dict[str, list[dict[str, int | float]] | dict[str, int | float]]) -> dict[str, list | dict]:    # ЕСЛИ СРАБАТЫВАЕТ АССЕРТ, то возможно надо обрабатывать это в try except и возвращать что-то на фронт в этом случае, каждую ошибку обработать надо. Бэк то блочится/крашится, а фронт ничего не получает
    '''15.02.23 пошагово смотрю, что делает каджая строчка функции второй версии и делаю универсальную функцию, ищу всевозможные варианты решения замкнутого полигона через некоторые формулы для разомнутого теодолитного хода'''
    
    measured_angles: list[dict[str, int | float]] = data.get('aPoints')
    bearingAngle: dict[str, int] = data.get('bearingAngle')
    initial_coords: list[dict[str, float]] = data.get('coords')         # Должно находиться 2 координаты всего лишь, начальная и конечная. С первой строки и последней в вебе должны собираться эти точки. Когда будут просчитываться все коориднаты, программа должна посчиатть ещё сама и последнюю координату и сравнить её с той, которую передали.
    direction_of_circling = data.get('direction_of_circling')
    side_of_angles = data.get('side_of_angles')
    if direction_of_circling == 'right' and side_of_angles == 'right' or direction_of_circling == 'left' and side_of_angles == 'left': 
        help_side = 'inner'
    elif direction_of_circling == 'right' and side_of_angles == 'left' or direction_of_circling == 'left' and side_of_angles == 'right':
        help_side = 'outer'
    
    nl = '\n'   # newline for f-string
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # [(d/m/s), ...] print(list_of_angles)
    list_of_decimal_angles = [get_decimal_angle1(a) for a in list_of_angles] # type: ignore [d.ms(decimal), ...] Тут нет округления, что б вычисления не попортить print(list_of_decimal_angles)
    sum_of_angles = calc_sum_of_measured_angles1(list_of_angles) # type: ignore print(sum_of_angles)
    
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), help_side) # type: ignore Тут жалуется, потому как переменная help_side объявляется внутри условий и по идее я должен буду достучаться до неё, но интерпретатор думает, что этой переменной ещё нет. Но я проверил, всё нормально если после этих строк вызвать принт этой переменной, значит всё распечатается норм.
    
    difference = calc_difference_ang1(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой. Потом при формировании выходных данных там в секунды пересчитывается само, что б можно было пропарсить словарик и получить нормального вида данные, но если нули в старших разрядах угла, то их не стоит писать, но это ньюансы, наверное
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    
    permissible_difference = calc_permissible_discrepancy1(len(list_of_angles))  # Допустимая невязка. Потом при формировании выходных данных там в секунды пересчитывается само
    assert difference < permissible_difference, "Невязка горизонтальных углов больше, чем допустимая невязка, надо бы что-то с этим сделать (возможно неправильно указана точность прибора, которым делали измерения)"
    
    correct_angles = [calc_correct_angle1(angle, amendments) for angle in list_of_decimal_angles]    # decimal. Без округления
    
    bearingAngle_decimal = get_decimal_angle1((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore decimal
    bearingAngles = get_all_bearing_angles(bearingAngle_decimal, correct_angles, side_of_angles)    # list[decimal, ...] side_of_angles (правые или левые по ходу углы измерялись, по идее тут ничего не надо трогать, просто передавать нужный и всё)
    # if data.get('is_closed'): # По идее тут не стоит проверять, замкнутый ли это полигон, т.к. эта функция должна будет просчитывать только замкнутые полигоны, где оба исходных пункта лежат внутри полигона, и т.е. из-за этого расчёты будут проводиться используя некоторые формулы из разомкнутого хода. Для разомкнутого(диагонального или просто раз.) надо написать другую функцию
    assert get_dms_angle(bearingAngle_decimal) == get_dms_angle(bearingAngles[-1]), "В замкнутом полигоне исходный дирекционный угол должен быть равен последнему просчитанному.\nПосле прочситывания всех дирекционных углов, конечный просчитанный угол не равен исходному, а должен... проверить  просчитывание/передачу исходного дир. угла и количество/порядок передачи измеренных углов."
    
    bearingAngles_dms = [get_dms_angle(bA) for bA in bearingAngles]
    bearingAngles_dms_dict = [create_dict_out_dms(bA) for bA in bearingAngles_dms]
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория и будет оповещение в терминале
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    # correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...] лучше я это сделаю при формировании данных, вдруг нужно будет ещё какие-то проверки делать или использовать углы. 
    
    list_dist = [d.get('HorDist') for d in measured_angles[:-1]]        # почему-то в Ванином варианте не весь периметр вычислялся -_- не бралось в расчёт горизонтальное проложение между твёрдыми пунктами. Есть логика в том, что мы используем формулы для разомкнутого хода, выходим из одного начального пункта и заканчиваем вычисления в конечном, поэтому нам не нужно расстояние между исходными пунктами
    # Не включаеся дистанция из последней точки. Т.к. там не должно быть расстояния. Либо если есть, то это между двумя исходными пунктами расстояние.
    perimeter = round(sum(list_dist), 3)    # округляю до 3-х знаков после запятой, потому что то уже мм, нам достаточно, всегда так считали. Ну и типа зачем на это отдельная функция -_-
    
    list_coordinate_increments = calc_coordinate_increments1(list_dist, bearingAngles)   # Приращения координат
    list_dict_coordinate_increments = [{"incX": round(X, 3), "incY": round(Y, 3)} for X, Y in list_coordinate_increments]   # Округляю только при сохранении информации, в таком виде будет передаваться для оттображения
    
    list_initial_coords = [(d.get('X'), d.get('Y')) for d in initial_coords]    # Начальные переданные координаты
    
    # возможно придётся переделывать всё без округлений и только для вывода на отображение округялть в отдельных функциях, на 15.02.23 так и делаю, все расчёты стараюсь без округлений. Только если сравниваю, то сравниваю обе округлённые величины и переведённые в градусы, например, что б точно верно проверять
    
    sum_theoretical_coordinate_increments = (list_initial_coords[1][0] - list_initial_coords[0][0], 
                                             list_initial_coords[1][1] - list_initial_coords[0][1])   # Конечная координата - начальная координата ЭТО ПРИМЕНЯЕТСЯ ТОЛЬКО ТОГДА, КОГДА ХОД РАЗОМКНУТЫЙ!!!! В замкнутом ходу должна равняться нулю -_- но замкнутый ход типа начинается из одной твёрдой точки и заканчивается в ней
    sum_calculated_coordinate_increments = (sum([d[0] for d in list_coordinate_increments]), 
                                            sum([d[1] for d in list_coordinate_increments]))          # Просто просуммировал вычисленыне приращения
    difference_increments = (sum_theoretical_coordinate_increments[0] - sum_calculated_coordinate_increments[0], 
                             sum_theoretical_coordinate_increments[1] - sum_calculated_coordinate_increments[1])  # Теория - практика, что б в следующих вычислениях не пришлось брать невязку с обратным знаком...
    
    difference_abs = math.hypot(difference_increments[0], difference_increments[1]) # fабс По моему вычисление квадрата суммы переменных
    difference_relative = (difference_abs / perimeter, 1 / (difference_abs / perimeter)) # fотн Сразу перевёл в удобный вариант масштаба, там всё зависит от разряда теодолитного хода, вот относительно разряда не должно превышать это число. Типа если это условие будет выполняться, то можно приступать к вычислению исправленных приращений координат. Возможно в будущем надо будет придумать эту проверку. ❓ Если число получается больше 0.0005 (это первый разряд или технический? у нас так же на первом курсе было. В интернете написано, что 1й разряд 1:2000, 2й разряд 1:1000), например, 0.00019, то значит это хорошо
    assert difference_relative[0] <= 1 / 2000, f"Относительная невязка не меньше 1:2000, что является допуском линейной невязки для теодолитного хода 1го разряда, что-то сделать с этим надо. По идее только перемерять расстояния в поле?{nl}Вот вычисленные значения: {difference_relative}"
    
    coordinate_increment_correct = calc_coordinate_increment_correct1(list_coordinate_increments, list_dist, difference_increments, perimeter)   # Исправленные приращения координат list[tuple[float, float]]
    sum_corrected_coordinate_increments = (sum([c[0] for c in coordinate_increment_correct]),
                                           sum([c[1] for c in coordinate_increment_correct]))   # Это может и не надо, но может и стоило бы добавить куда-нибудь
    assert tuple([round(n, 3) for n in sum_corrected_coordinate_increments]) == tuple([round(n, 3) for n in sum_theoretical_coordinate_increments]), f"Исправленные приращения координат не равны теоретическим, надо проверить...{nl}Теория: {sum_theoretical_coordinate_increments}{nl}Практика исправленная: {sum_corrected_coordinate_increments}"
    # list_dict_coordinate_increment_correct = [{"incXcor": round(X, 3), "incYcor": round(Y, 3)} for X, Y in coordinate_increment_correct]    # Округление для отображения нормальных чисел
    
    all_coords = calc_all_coordinates1(list_initial_coords, coordinate_increment_correct)
    assert {"X": round(all_coords[-1][0], 3), "Y": round(all_coords[-1][1], 3)} == initial_coords[-1], f'Вычисленные координаты конечной точки не равны переданной конечной, надо проверить вычисления.{nl}Переданные: {initial_coords[-1]}{nl}Вычисленные: {dict([("X", round(all_coords[-1][0], 3)), ("Y", round(all_coords[-1][1], 3))])}'
    
    data_out = {
        "angles": [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles],
        "bearing_angles": bearingAngles_dms_dict,
        "sum_measured_angles": create_dict_out_dms(get_dms_angle(sum_of_angles)), 
        "theoretical_sum_of_angles": create_dict_out_dms(get_dms_angle(theoretical_sum_of_angles)), 
        "difference": create_dict_out_dms(get_dms_angle(difference)), 
        "permissible_difference": create_dict_out_dms(get_dms_angle(permissible_difference)), 
        "sum_correct_angles": create_dict_out_dms(get_dms_angle(sum_cor)),
        "perimetr": perimeter,
        "coordinate_increments": list_dict_coordinate_increments,
        "coordinate_increment_correct": [{"incXcor": round(X, 3), "incYcor": round(Y, 3)} for X, Y in coordinate_increment_correct],    # Округление для отображения нормальных чисел
        "sum_theoretical_coordinate_increments": (round(sum_theoretical_coordinate_increments[0], 2), 
                                                  round(sum_theoretical_coordinate_increments[1], 2)),
        "sum_calculated_coordinate_increments": tuple(map(lambda inc: round(inc, 2), sum_calculated_coordinate_increments)),
        "difference_increments": tuple(map(lambda inc: round(inc, 2), difference_increments)),  # Решил через мап, что б не делать постоянно эти две строки округления, оставлю и такой и такой вариант
        "sum_corrected_coordinate_increments": (round(sum_corrected_coordinate_increments[0], 2),
                                                round(sum_corrected_coordinate_increments[1], 2)),  # По идее это не надо передавать, но по идее, надо бы понимать, что эти значения равны велчинам теретического приращения
        "difference_abs": difference_abs,
        "difference_relative": (round(difference_relative[0], 4), round(difference_relative[1])),
        "all_coords": [{"X": round(X, 3), "Y": round(Y, 3)} for X, Y in all_coords]
        }
    
    return data_out


def get_result2(data: dict[str, list[dict[str, int | float]] | dict[str, int | float]]) -> dict[str, list | dict]:    # 
    '''Функция хорошо решает задачи для разомкнутого хода, но надо чётко прописать алгоритм, как правильно заполнять данные необходимо, где начальные, где конечные точки и какие расстояния указать
    15.02.23 оставил эту функцию за шаблон, возможно удалить надо будет её. в третьей версии пошагово смотрю, как работаю с данными и ввожу дополнительные атрибуты и проверки для универсального вычисления.'''
    
    measured_angles: list[dict[str, int | float]] = data.get('aPoints')
    bearingAngle: dict[str, int] = data.get('bearingAngle')
    initial_coords: list[dict[str, float]] = data.get('coords')         # Должно находиться 2 координаты всего лишь, начальная и конечная. С первой строки и последней в вебе должны собираться эти точки. Когда будут просчитываться все коориднаты, программа должна посчиатть ещё сама и последнюю координату и сравнить её с той, которую передали.
    direction_of_circling = data.get('direction_of_circling')
    side_of_angles = data.get('side_of_angles')
    if direction_of_circling == 'right' and side_of_angles == 'right' or direction_of_circling == 'left' and side_of_angles == 'left': 
        help_side = 'inner'
    elif direction_of_circling == 'right' and side_of_angles == 'left' or direction_of_circling == 'left' and side_of_angles == 'right':
        help_side = 'outer'
    
    list_of_angles = [(d.get('Deg'), d.get('Min'), d.get('Sec')) for d in measured_angles]  # d/m/s
    list_of_decimal_angles = [get_decimal_angle1(a) for a in list_of_angles]
    sum_of_angles = calc_sum_of_measured_angles1(list_of_angles) # type: ignore
    
    theoretical_sum_of_angles = calc_sum_of_theoretical_angles(len(list_of_angles), help_side) # Тут жалуется, потому как переменная help_side объявляется внутри условий и по идее я должен буду достучаться до неё, но интерпретатор думает, что этой переменной ещё нет. Но я проверил, всё нормально если после этих строк вызвать принт этой переменной, значит всё распечатается норм.
    difference = calc_difference_ang1(sum_of_angles, theoretical_sum_of_angles)  # Разница между теорией и пратикой
    amendments = calc_amendments(difference, len(list_of_angles)) # Поправка в каждый угол поделённая поровну между всеми углами.
    
    permissible_difference = calc_permissible_discrepancy1(len(list_of_angles))  # Допустимая невязка
    
    correct_angles = [calc_correct_angle1(angle, amendments) for angle in list_of_decimal_angles]    # decimal
    
    bearingAngle_dms = get_decimal_angle((bearingAngle.get("Deg"), bearingAngle.get("Min"), bearingAngle.get("Sec")))   # type: ignore decimal
    bearingAngles = get_all_bearing_angles(bearingAngle_dms, correct_angles, side_of_angles)    # list[decimal, ...] side_of_angles (правые или левые по ходу углы измерялись, по идее тут ничего не надо трогать, просто передавать нужный и всё)
    bearingAngles_dms = [get_dms_angle(bA) for bA in bearingAngles]
    bearingAngles_dms_dict = [create_dict_out_dms(bA) for bA in bearingAngles_dms]
    
    sum_cor = calc_sum_of_corrected_angles(correct_angles, theoretical_sum_of_angles)   # Сумма исправленных углов. Если оне не сходится с теорией меньше чем на 5", то для вывода инфы передастся теория
    
    correct_angles = [get_dms_angle(angle) for angle in correct_angles] # d/m/s
    correct_angles = [{"CorDeg": a[0], "CorMin": a[1], "CorSec": a[2]} for a in correct_angles] # [{d/m/s}, ...]
    
    list_dist = [d.get('HorDist') for d in measured_angles]        # measured_angles[:-1] было, почему-то в Ванином варианте не весь периметр вычислялся -_- не бралось в расчёт горизонтальное проложение между твёрдыми пунктами
    perimeter = calc_sum_of_distance(list_dist)
    
    list_coordinate_increments = calc_coordinate_increments1(list_dist, bearingAngles)   # Приращения координат
    list_dict_coordinate_increments = [{"incX": round(X, 3), "incY": round(Y, 3)} for X, Y in list_coordinate_increments]   # Округляю только при сохранении информации, в таком виде будет передаваться для оттображения
    
    list_initial_coords = [(d.get('X'), d.get('Y')) for d in initial_coords]    # Начальные переданные координаты
    
    # Следующие переменные лежат в кортеже (X, Y)
    # !!!!!!! Т.к. я начал уже округлять где-то до этого вычисляемые значения, то и тут везде я тоже округляю, что б видеть и понимать нормально, что получается в итоге
    # (Я наверное, так сделал, что б сразу эти занчения передавать на фронт, хотя хз)
    # возможно придётся переделывать всё без округлений и только для вывода на отображение округялть в отдельных функциях....
    
    sum_theoretical_coordinate_increments = (list_initial_coords[1][0] - list_initial_coords[0][0], 
                                             list_initial_coords[1][1] - list_initial_coords[0][1])   # Конечная координата - начальная координата ЭТО ПРИМЕНЯЕТСЯ ТОЛЬКО ТОГДА, КОГДА ХОД РАЗОМКНУТЫЙ!!!! В замкнутом ходу должна равняться нулю -_-
    # sum_theoretical_coordinate_increments = (0, 0)
    
    sum_calculated_coordinate_increments = (sum([d[0] for d in list_coordinate_increments]), 
                                            sum([d[1] for d in list_coordinate_increments]))          # Просто просуммировал вычисленыне приращения
    difference_increments = (sum_theoretical_coordinate_increments[0] - sum_calculated_coordinate_increments[0], 
                             sum_theoretical_coordinate_increments[1] - sum_calculated_coordinate_increments[1])  # Теория - практика, что б в следующих вычислениях не пришлось брать невязку с обратным знаком...
    
    difference_abs = math.hypot(difference_increments[0], difference_increments[1]) # fабс По моему вычисление квадрата суммы переменных
    difference_relative = (difference_abs / perimeter, 1 / (difference_abs / perimeter)) # fотн Сразу перевёл в удобный вариант масштаба, там всё зависит от разряда теодолитного хода, вот относительно разряда не должно превышать это число. Типа если это условие будет выполняться, то можно приступать к вычислению исправленных приращений координат. Возможно в будущем надо будет придумать эту проверку. ❓ Если число получается больше 0.0005 (это первый разряд 1:2000), например, 0.00019, то значит это хорошо
    
    coordinate_increment_correct = calc_coordinate_increment_correct1(list_coordinate_increments, list_dist, difference_increments, perimeter)   # Исправленные приращения координат list[tuple[float, float]]
    sum_corrected_coordinate_increments = (sum([c[0] for c in coordinate_increment_correct]),
                                           sum([c[1] for c in coordinate_increment_correct]))   # Это может и не надо, но может и стоило бы добавить куда-нибудь
    
    # print(round(sum_theoretical_coordinate_increments[0], 2) == round(sum_corrected_coordinate_increments[0], 2), round(sum_theoretical_coordinate_increments[1], 2) == round(sum_corrected_coordinate_increments[1], 2))   # Что б сравнить полученную сумму приращений с теоретической
    
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
        "sum_theoretical_coordinate_increments": (round(sum_theoretical_coordinate_increments[0], 2), 
                                                  round(sum_theoretical_coordinate_increments[1], 2)),
        "sum_calculated_coordinate_increments": tuple(map(lambda inc: round(inc, 2), sum_calculated_coordinate_increments)),
        "difference_increments": tuple(map(lambda inc: round(inc, 2), difference_increments)),  # Решил через мап, что б не делать постоянно эти две строки округления, оставлю и такой и такой вариант
        "sum_corrected_coordinate_increments": (round(sum_corrected_coordinate_increments[0], 2),
                                                round(sum_corrected_coordinate_increments[1], 2)),  # По идее это не надо передавать, но по идее, надо бы понимать, что эти значения равны велчинам теретического приращения
        "difference_abs": difference_abs,
        "difference_relative": (round(difference_relative[0], 4), round(difference_relative[1])),
        "all_coords": all_coords_dict
        }
    
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
    sum_corrected_coordinate_increments = (sum([c[0] for c in coordinate_increment_correct]),
                                           sum([c[1] for c in coordinate_increment_correct]))   # Это может и не надо, но может и стоило бы добавить куда-нибудь
    
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
        "sum_theoretical_coordinate_increments": (round(sum_theoretical_coordinate_increments[0], 2), 
                                                  round(sum_theoretical_coordinate_increments[1], 2)),
        "sum_calculated_coordinate_increments": sum_calculated_coordinate_increments,
        "sum_corrected_coordinate_increments": (round(sum_corrected_coordinate_increments[0], 2),
                                                round(sum_corrected_coordinate_increments[1], 2)),  # По идее это не надо передавать, но по идее, надо бы понимать, что эти значения равны велчинам теретического приращения
        "difference_abs": difference_abs,
        "difference_relative": difference_relative,
        "all_coords": all_coords_dict
        }
    
    return data_out


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


def send_test_data(path: str):
    '''Отослать тестовые данные (Измеренные углы + расстояния)'''
    
    with open(path, "r", encoding="utf-8") as f:
        data_inp = json.loads(f.read())

    return(data_inp)

# print(get_sum_of_measured_angles.__doc__)
# print(get_decimal_ange.__doc__)