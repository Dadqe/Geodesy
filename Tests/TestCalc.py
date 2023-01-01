import sys
import os
import json

# Добавляю в поиск путей корневую директорию всех файлов
sys.path.insert(1, os.getcwd())
from calc import get_decimal_angle, calc_sum_of_measured_angles, get_dms_angle, calc_sum_of_theoretical_angles, calc_difference_ang, calc_permissible_discrepancy, get_correct_angles, send_test_data


ang1 = (180, 50, 35)
ang2 = (20, 10, 5)
ang1_dms = get_decimal_angle(ang1)

test_site1 = [(23, 49, 18), (238, 29, 18), (204, 27, 3), (67, 59, 56), (180, 31, 51), (82, 14, 38), (102, 27, 54)]

IS1 = calc_sum_of_measured_angles(tuple(test_site1))
SHOULD_BE1 = calc_sum_of_theoretical_angles(len(test_site1))
dif1 = calc_difference_ang(IS1, SHOULD_BE1)


test_site2 = [(107, 17, 30), (182, 59, 30), (205, 0, 0), (109, 25, 0), (119, 9, 30), (172, 43, 0), (193, 4, 30), (150, 6, 0), (214, 47, 30), (109, 39, 30), (128, 25, 30), (208, 3, 0), (119, 16, 30), (139, 59, 30)]

IS2 = calc_sum_of_measured_angles(tuple(test_site2))
SHOULD_BE2 = calc_sum_of_theoretical_angles(len(test_site2))
dif2 = calc_difference_ang(IS2, SHOULD_BE2)
theoretical_dif2 = calc_permissible_discrepancy(len(test_site2))


assert get_decimal_angle(ang1) == 180.843056, "Неверный угол получился, должен был быть 180.843056"
assert calc_sum_of_measured_angles((ang1, ang2)) == 201.011112, "Неверная сумма углов получилась, должна была быть 201.011112"
assert get_dms_angle(ang1_dms) == ang1, "Неверно получен угол в виде гр/мин/сек при раскладывании из десятичного, д.б. 180, 50, 35"
assert calc_sum_of_theoretical_angles(len(test_site1)) == 900, "Неверно получена теоретическая сумма углов по полигону, д.б. 900"
assert calc_difference_ang(IS1, SHOULD_BE1) == 0.000556, "Неверно получена невязка между теорией и практикой, д.б. 0.000556 или (0, 0, 2) если раскладывать в гр/мин/сек"
assert calc_difference_ang(IS2, SHOULD_BE2) == 0.058332, "Неверно получена невязка между теорией и практикой, д.б. 0.058332 или (0, 3, 30) если раскладывать в гр/мин/сек"
assert calc_permissible_discrepancy(len(test_site2)) == 0.062361, "Неверно получена допустимая невязка хода в test_site2, д.б. 0.062361 или (0, 3, 44) если раскладывать"



# print(get_decimal_angle(ang1))
# print(get_sum_of_measured_angles((ang1, ang2)))
# print(get_dms_angle(ang1_dms) == ang1)
# print(IS1)
# print(get_dms_angle(IS1))
# print(IS2)
# print(get_dms_angle(IS2))
# print(SHOULD_BE1)   # 900
# print(SHOULD_BE2)   # 2160
# print(dif1)
# print(get_dms_angle(dif1))
# print(dif2)
# print(get_dms_angle(dif2))
# print(get_dms_angle(theoretical_dif2))

# ТЕСТ get_correct_angles

# with open("DataInput.json", "r", encoding="utf-8") as f:
#     data_inp = json.loads(f.read())

# cor_angles = get_correct_angles(data_inp)

# print(get_dms_angle(cor_angles))
# print(cor_angles)
# with open("DataOutput.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(cor_angles, ensure_ascii=False, indent=4))




# T = [
#         {
#             "CorDeg": 107,
#             "CorMin": 17,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 182,
#             "CorMin": 59,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 205,
#             "CorMin": 0,
#             "CorSec": 15
#         },
#         {
#             "CorDeg": 109,
#             "CorMin": 25,
#             "CorSec": 15
#         },
#         {
#             "CorDeg": 172,
#             "CorMin": 43,
#             "CorSec": 15
#         },
#         {
#             "CorDeg": 193,
#             "CorMin": 4,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 150,
#             "CorMin": 6,
#             "CorSec": 15
#         },
#         {
#             "CorDeg": 214,
#             "CorMin": 47,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 109,
#             "CorMin": 39,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 128,
#             "CorMin": 25,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 208,
#             "CorMin": 3,
#             "CorSec": 15
#         },
#         {
#             "CorDeg": 119,
#             "CorMin": 16,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 139,
#             "CorMin": 59,
#             "CorSec": 45
#         },
#         {
#             "CorDeg": 119,
#             "CorMin": 9,
#             "CorSec": 45
#         }
#     ]

# list_of_angles = [(d.get('CorDeg'), d.get('CorMin'), d.get('CorSec')) for d in T]
# list_of_decimal_angles = [get_decimal_angle(a) for a in list_of_angles]
# sum_of_angles = calc_sum_of_measured_angles(list_of_angles)
# print(get_dms_angle(sum_of_angles))
# print(list_of_decimal_angles)

TT = [
    {
        "Deg": 107,
        "Min": 17,
        "Sec": 30,
        "HorDist": 33.55
    },
    {
        "Deg": 182,
        "Min": 59,
        "Sec": 30,
        "HorDist": 42.35
    },
    {
        "Deg": 205,
        "Min": 0,
        "Sec": 0,
        "HorDist": 41.95
    },
    {
        "Deg": 109,
        "Min": 25,
        "Sec": 0,
        "HorDist": 59.4
    },
    {
        "Deg": 172,
        "Min": 43,
        "Sec": 0,
        "HorDist": 66.61
    },
    {
        "Deg": 193,
        "Min": 4,
        "Sec": 30,
        "HorDist": 90.6
    },
    {
        "Deg": 150,
        "Min": 6,
        "Sec": 0,
        "HorDist": 50.81
    },
    {
        "Deg": 214,
        "Min": 47,
        "Sec": 30,
        "HorDist": 78
    },
    {
        "Deg": 109,
        "Min": 39,
        "Sec": 30,
        "HorDist": 52.93
    },
    {
        "Deg": 128,
        "Min": 25,
        "Sec": 30,
        "HorDist": 52.4
    },
    {
        "Deg": 208,
        "Min": 3,
        "Sec": 0,
        "HorDist": 49.38
    },
    {
        "Deg": 119,
        "Min": 16,
        "Sec": 30,
        "HorDist": 46.32
    },
    {
        "Deg": 139,
        "Min": 59,
        "Sec": 30,
        "HorDist": 294.69
    },
    {
        "Deg": 119,
        "Min": 9,
        "Sec": 30,
        "HorDist": 56.8
    }
]

# Проверка работоспособности основной функции возвращения исправленных углов
# TT_O = get_correct_angles(TT)
# print(TT_O)
# angles = TT_O.get("angles")
# list_of_angles = [(d.get('CorDeg'), d.get('CorMin'), d.get('CorSec')) for d in angles]
# sum_of_angles = calc_sum_of_measured_angles(list_of_angles)


# print(sum_of_angles)


# dms_out = [(107, 17, 45), (182, 59, 45), (205, 0, 15), (109, 25, 15), (172, 43, 15), (193, 4, 45), (150, 6, 15), (214, 47, 45), (109, 39, 45), (128, 25, 45), (208, 3, 15), (119, 16, 45), (139, 59, 45), (119, 9, 45)]

# new_out = [get_decimal_angle(angle) for angle in dms_out]
# print(get_dms_angle(sum(new_out)))
# print(get_dms_angle(calc_sum_of_measured_angles(dms_out)))


# t = [107.295833, 182.995833, 205.004167, 109.420833, 172.720833, 193.079167, 150.104167, 214.795833, 109.6625, 128.429167, 208.054167, 119.279167, 139.995833, 119.1625]

# summa_t = 0
# for el in t:
#     summa_t += el
# summa_t = round(summa_t, 6)
# print(get_dms_angle(summa_t))

# Проверка тестовых данных
# send_test_data()
