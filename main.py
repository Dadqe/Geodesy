from fastapi import FastAPI, Query
from schemas import Point, Points, Data
from calc import get_correct_angles, send_test_data1
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

@app.get('/TestData/{id}')
def get_adj_test(id: int):
    '''
    Отослать тестовые данные вторые из Ваниной таблицы
    '''
    
    if id == 1:
        # Данные с практики первого курса
        return send_test_data1("Data/DataInput1.json")
    elif id == 2:
        # Данные от Вани из первой таблицы.
        return send_test_data1("Data/DataInput2.json")
    else:
        return False


@app.post('/GetResult')
def send_result(item: Points):
    '''
    Отослать исправленные горизонтальные углы и плюс вычисления для этого
    '''
    
    data = item.dict()
    
    # return item
    return get_correct_angles(data.get('aPoints'), data.get('bearingAngle'))  # type: ignore


@app.post('/Tests/responsemodel', response_model=Points)
def respmodel(item: Points):
    return item

# if __name__ == "__main__":
#     uvicorn.run(app)


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