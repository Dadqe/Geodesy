from pydantic import BaseModel
from typing import List     # можно попробовать уже в 3.10 на тайпингах внутри Питона

class Point(BaseModel):
    Deg: int = 0
    Min: int = 0
    Sec: int = 0
    HorDist: float # | int


class Points(BaseModel):
    aPoints: list[Point]


class Data(BaseModel):
    name: str

# class Point(BaseModel):
#     Name: str = ''
#     Deg: int = 0
#     Min: int = 0
#     Sec: int = 0
#     HorDist: float # | int