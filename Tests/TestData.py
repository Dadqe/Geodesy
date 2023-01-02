import json


def calc_sum_of_corrected_angles(angles: list[tuple[int, int, int]]) -> float:
    '''
    Посчитает сумму исправленных углов
    Для этого надо сначала все углы перевести в десятичные градусы (они уже должны будут быть в таком виде, по идее. Только для вывода они переводятся в d/m/s)?
    просуммировать. Обычно исправленная сумма должна быть равна числу теоретической суммы. Обычно там целое число. Если это не так, то надо при вычислении суммы использовать исправленные углы, не округлённые до 6 знаков.
    Что б проверить, надо будет беревести в d/m/s, ну и для вышенаписанного условия надо бы передавать или использовать функцию для вычисления теоретическомй суммы и всё. Но лучше передавать, т.к. она уже вычислена будет в программе, по идее
    '''
    
    return round(sum(angles), 6)


def get_decimal_angle(angle: tuple[int, int, int]) -> float:
    ''' из гр/мин/сек раскладываю в десятичный угол '''
    
    return round(angle[0] + angle[1] / 60 + angle[2] / 3600, 6)



# Из ведомости вычисления координат, видимо 4 курс, курсач с Таней. со второго листа 313-1-2-3-4-5-314
[(23, 49, 18), (238, 29, 18), (204, 27, 3), (67, 59, 56), (180, 31, 51), (82, 14, 38), (102, 27, 54)]

# Из ведомости вычисления координат по практике за первый курс 12 углов О_о
s2 = [(107, 17, 30, 33.55), (182, 59, 30, 42.35), (205, 0, 0, 41.95), (109, 25, 0, 59.4), (119, 9, 30, 56.8), (172, 43, 0, 66.61), (193, 4, 30, 90.6), (150, 6, 0, 50.81), (214, 47, 30, 78), (109, 39, 30, 52.93), (128, 25, 30, 52.40), (208, 3, 0, 49.38), (119, 16, 30, 46.32), (139, 59, 30, 294.69)]
# В последней точке тип тоже есть информация о том, какое расстояние между последним ПП (Пунктом полигонометрии) и первым ПП, но он в расчёт суммы растояний, почему-то не берётся

# Сумма расстояний = периметр хода
sum_d_s2 = round(sum([t[3] for t in s2[:-1]]), 3)
# print(sum_d_s2)

# aa = s2[:]
# ss = [{"Deg": a[0], "Min": a[1], "Sec": a[2], "HorDist": a[3]} for a in aa]
# # print(ss)
# with open("DataInput.json", "w", encoding="utf-8") as f:
#     out = json.dumps(ss, ensure_ascii=False, indent=4)    # dumps из питоновских типов всех делает строку, сохраняя скобки и потом можно записать в ДЖСОН и всё будет в нормальном виде. Главное не забыть параметры ensure_ascii=False, indent=4
# # с f.read можно и в одну строку запиасть, но так удобнее
#     f.write(out)






s3 = [
        {
            "CorDeg": 314,
            "CorMin": 48,
            "CorSec": 41
        },
        {
            "CorDeg": 143,
            "CorMin": 33,
            "CorSec": 54
        },
        {
            "CorDeg": 163,
            "CorMin": 4,
            "CorSec": 14
        },
        {
            "CorDeg": 207,
            "CorMin": 52,
            "CorSec": 43
        },
        {
            "CorDeg": 133,
            "CorMin": 53,
            "CorSec": 11
        },
        {
            "CorDeg": 296,
            "CorMin": 47,
            "CorSec": 40
        },
        {
            "CorDeg": 276,
            "CorMin": 7,
            "CorSec": 0
        },
        {
            "CorDeg": 155,
            "CorMin": 21,
            "CorSec": 43
        },
        {
            "CorDeg": 210,
            "CorMin": 51,
            "CorSec": 35
        },
        {
            "CorDeg": 167,
            "CorMin": 10,
            "CorSec": 41
        },
        {
            "CorDeg": 270,
            "CorMin": 28,
            "CorSec": 33
        }
    ]

aga = [(d['CorDeg'], d['CorMin'], d['CorSec']) for d in s3]
print(calc_sum_of_measured_angles(aga))