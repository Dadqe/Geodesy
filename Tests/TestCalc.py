import sys
import os
import json

# Добавляю в поиск путей корневую директорию всех файлов
sys.path.insert(1, os.getcwd())
from calc import get_decimal_angle, calc_sum_of_measured_angles, get_dms_angle, calc_sum_of_theoretical_angles, calc_difference_ang, calc_permissible_discrepancy, send_test_data, get_result, get_result1, get_result2

# Прочитывать для исходных данных, что б можно было использовать в следующих тестах. Тут данные с практики 1го курса
with open("Data/Input/DataInput1.json", "r", encoding="utf-8") as f:
    TESTDATA1 = json.loads(f.read())

# Исходные данные из Ваниной таблицы первой. ЕСТЬ БЕДА В ТОМ, что у него расстояния записаны с кучей знаков после запятой -_- так не должно быть, по идее, мы должны округлять по 3 знака, до см только.

# Мне надо переделывать тестовые данные под то, что будет щас ещё передаваться дирекционный угол, набор входных данных немного надо преобразовать для проверки решения
# with open("Data/Input/DataInput2.json", "r", encoding="utf-8") as f:
#     TESTDATA2 = json.loads(f.read())

# Тестовые данные от Вани с добавлением дир.угла
# with open("Data/Input/DataInput2 copy.json", "r", encoding="utf-8") as f:
#     TESTDATA2_1 = json.loads(f.read())
    
# Тестовые данные от Вани с добавлением дир.угла, начальной и конечной координаты
with open("Data/Input/DataInput3 copy.json", "r", encoding="utf-8") as f:
    TESTDATA3 = json.loads(f.read())


# ang1 = (180, 50, 35)
# ang2 = (20, 10, 5)
# ang1_dms = get_decimal_angle(ang1)

# test_site1 = [(23, 49, 18), (238, 29, 18), (204, 27, 3), (67, 59, 56), (180, 31, 51), (82, 14, 38), (102, 27, 54)]

# IS1 = calc_sum_of_measured_angles(tuple(test_site1))
# SHOULD_BE1 = calc_sum_of_theoretical_angles(len(test_site1))
# dif1 = calc_difference_ang(IS1, SHOULD_BE1)


# test_site2 = [(107, 17, 30), (182, 59, 30), (205, 0, 0), (109, 25, 0), (119, 9, 30), (172, 43, 0), (193, 4, 30), (150, 6, 0), (214, 47, 30), (109, 39, 30), (128, 25, 30), (208, 3, 0), (119, 16, 30), (139, 59, 30)]

# IS2 = calc_sum_of_measured_angles(tuple(test_site2))
# SHOULD_BE2 = calc_sum_of_theoretical_angles(len(test_site2))
# dif2 = calc_difference_ang(IS2, SHOULD_BE2)
# theoretical_dif2 = calc_permissible_discrepancy(len(test_site2))


# assert get_decimal_angle(ang1) == 180.843056, "Неверный угол получился, должен был быть 180.843056"
# assert calc_sum_of_measured_angles((ang1, ang2)) == 201.011112, "Неверная сумма углов получилась, должна была быть 201.011112"
# assert get_dms_angle(ang1_dms) == ang1, "Неверно получен угол в виде гр/мин/сек при раскладывании из десятичного, д.б. 180, 50, 35"
# assert calc_sum_of_theoretical_angles(len(test_site1)) == 900, "Неверно получена теоретическая сумма углов по полигону, д.б. 900"
# assert calc_difference_ang(IS1, SHOULD_BE1) == 0.000556, "Неверно получена невязка между теорией и практикой, д.б. 0.000556 или (0, 0, 2) если раскладывать в гр/мин/сек"
# assert calc_difference_ang(IS2, SHOULD_BE2) == 0.058332, "Неверно получена невязка между теорией и практикой, д.б. 0.058332 или (0, 3, 30) если раскладывать в гр/мин/сек"
# assert calc_permissible_discrepancy(len(test_site2)) == 0.062361, "Неверно получена допустимая невязка хода в test_site2, д.б. 0.062361 или (0, 3, 44) если раскладывать"



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


# Проверка работоспособности основной функции возвращения исправленных углов
# TT_O = get_correct_angles(TESTDATA2)
# print(TT_O)

# TT_O_leftsides = get_correct_angles1(TESTDATA2_1)
# print(TT_O_leftsides)

# TT_O_leftsides = get_correct_angles2(TESTDATA2_1.get('aPoints'), TESTDATA2_1.get('bearingAngle'))
# print(TT_O_leftsides)


# with open("Data/DataOutput2 copy.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(TT_O_leftsides, ensure_ascii=False, indent=4))


TT_O = get_result2(TESTDATA3)

# with open("Data/Output/DataOutput33 copy2.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(TT_O, ensure_ascii=False, indent=4))
