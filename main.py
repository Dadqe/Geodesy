from fastapi import FastAPI, Query
from schemas import Point, Points, Data
from calc import get_correct_angles, send_test_data, get_result1
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
        return send_test_data("Data/DataInput1.json")
    elif id == 2:
        # Данные от Вани из первой таблицы.
        return send_test_data("Data/DataInput2.json")
    elif id == 3:
        # Данные от Вани из первой таблицы (со всеми нужными данными для вычисления (начальный дир. угол + начальные и конечные координаты)).
        return send_test_data("Data/DataInput3.json")
    else:
        return False


@app.post('/GetResult')
def send_result(item: Points):
    '''
    Отослать исправленные горизонтальные углы и плюс вычисления для этого
    '''
    
    data = item.dict()
    
    return get_result1(data)
    return get_correct_angles(data.get('aPoints'), data.get('bearingAngle'))  # type: ignore


@app.post('/Tests/responsemodel', response_model=Points)
def respmodel(item: Points):
    return item

# if __name__ == "__main__":
#     uvicorn.run(app)


# uvicorn main:app --reload