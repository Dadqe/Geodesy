    # [
    #     {
    #         "CorDeg": 107,
    #         "CorMin": 17,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 182,
    #         "CorMin": 59,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 205,
    #         "CorMin": 0,
    #         "CorSec": 15
    #     },
    #     {
    #         "CorDeg": 109,
    #         "CorMin": 25,
    #         "CorSec": 15
    #     },
    #     {
    #         "CorDeg": 172,
    #         "CorMin": 43,
    #         "CorSec": 15
    #     },
    #     {
    #         "CorDeg": 193,
    #         "CorMin": 4,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 150,
    #         "CorMin": 6,
    #         "CorSec": 15
    #     },
    #     {
    #         "CorDeg": 214,
    #         "CorMin": 47,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 109,
    #         "CorMin": 39,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 128,
    #         "CorMin": 25,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 208,
    #         "CorMin": 3,
    #         "CorSec": 15
    #     },
    #     {
    #         "CorDeg": 119,
    #         "CorMin": 16,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 139,
    #         "CorMin": 59,
    #         "CorSec": 45
    #     },
    #     {
    #         "CorDeg": 119,
    #         "CorMin": 9,
    #         "CorSec": 45
    #     }
    # ]



t = [107.295833, 182.995833, 205.004167, 109.420833, 172.720833, 193.079167, 150.104167, 214.795833, 109.6625, 128.429167, 208.054167, 119.279167, 139.995833, 119.1625]

summa_t = 0
for el in t:
    summa_t += el
print(round(summa_t, 6))