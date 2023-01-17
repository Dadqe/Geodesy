from pydantic import BaseModel
from typing import List     # можно попробовать уже в 3.10 на тайпингах внутри Питона

class Point(BaseModel):
    Deg: int = 0
    Min: int = 0
    Sec: int = 0
    HorDist: float = 0# | int


class BearingAngle(BaseModel):
    Deg: int = 0
    Min: int = 0
    Sec: int = 0

class Coords(BaseModel):
    X: float = 0
    Y: float = 0

class Points(BaseModel):
    aPoints: list[Point] = []
    bearingAngle: BearingAngle
    coords: list[Coords] = []
    direction_of_circling: str = 'right'    # Направление хода, по часовой или против (право или лево, считать от верхней точки круга)
    side_of_angles: str = 'right'           # Сторона измерения углов относительно хода


class Data(BaseModel):
    name: str

# class Point(BaseModel):
#     Name: str = ''
#     Deg: int = 0
#     Min: int = 0
#     Sec: int = 0
#     HorDist: float # | int