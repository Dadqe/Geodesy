from fastapi import FastAPI, Query
from schemas import Point, Points, Data
from calc import get_correct_angles
import uvicorn

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"key": "Hello FastAPI"}


@app.post('/CorAng')
def get_cor_ang(item: Point):
    ''' Вернуть исправленные углы
    Для этого надо сначала посчитать теорию, потом практику, невязку и раскидать невязку. 
    Возможно через генератор раскидывать потому как надо будет целочисленным делением это делать
    и остатки кидать в конце'''
    
    # print(f"Type of response body:\n{type(item)}")
    
    d = item.dict()
    # print(type(d))
    # print(d)
    # Name, HorDist = d.get("Name"), d.get("HorDist")
    # print(type(Name), Name, '\n', type(HorDist), HorDist)
    # print(type(d['Deg']))
    
    # return d        # Я могу даже просто словарик возвращать О_о
    return item     # Чисто проверить, возвращается ли то, что передали. Для тестов данные уже есть в dict of json.py


@app.post('/CorAngs')
def get_cor_angs(item: Points):
    '''
    Вернуть список написанных углов + горизонтальное проложение
    '''
    
    print(f"Type of response body:\n{type(item)}")
    
    d = item.dict()
    print(type(d))
    print(d)
    
    return item


@app.post('/Test1')
def send_cor_angs(item: Points):
    '''
    Отослать исправленные горизонтальные углы и плюс вычисления для этого
    '''
    
    data = item.dict()
    # print(type(data))
    # print(data)
    
    return True
    # return get_correct_angles(data.get('Points'))


@app.post('/Test2')
def send(item: Points):
    '''
    Отослать исправленные горизонтальные углы и плюс вычисления для этого
    '''
    
    data = item.dict()
    # data1 = data.get('aPoints')
    # print(type(data1))
    # print(data1)
    
    # return item
    return get_correct_angles(data.get('aPoints'))


if __name__ == "__main__":
    uvicorn.run(app)


# uvicorn main:app --reload

# {
#     "angles": [
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
#             "CorDeg": 119,
#             "CorMin": 9,
#             "CorSec": 45
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
#         }
#     ],
#     "sum_measured_angles": {
#         "Deg": 2159,
#         "Min": 56,
#         "Sec": 30
#     },
#     "theoretical_sum_of_angles": {
#         "Deg": 2160,
#         "Min": 0,
#         "Sec": 0
#     },
#     "difference": {
#         "Deg": 0,
#         "Min": 3,
#         "Sec": 30
#     },
#     "permissible_difference": {
#         "Deg": 0,
#         "Min": 3,
#         "Sec": 44
#     },
#     "sum_correct_angles": {
#         "Deg": 2160,
#         "Min": 0,
#         "Sec": 0
#     }
# }