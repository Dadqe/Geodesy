import math

Deg = 123.88957099999999
Dist = 35.516

DegRad = math.radians(Deg)
DegCos = math.cos(DegRad)

out = DegCos * Dist
print(round(out, 3))
print(round(math.cos(math.radians(Deg)) * Dist, 3))