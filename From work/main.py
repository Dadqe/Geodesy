from schemas import Point

# Дома уже есть

@app.post('/CorAng')
def get_cor_ang(item: Point):
    return item     # Чисто проверить, возвращается ли то, что передали. Для тестов данные уже есть в dict of json.py


@app.get('point')
def get_info_about_point_for_report(q: str = Query(None)):
    pass

# У меня не может быть get-запросов, т.к. у меня нет никакой базы данных, неоткуда брать значения, я могу только возвращать значения, исходя из того, что мне передадут на Бэк