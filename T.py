import requests

headers = {
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'null',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.818 Yowser/2.5 Safari/537.36',
    'accept': '*/*',
    'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'aPoints': [
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
            "Deg": 119,
            "Min": 9,
            "Sec": 30,
            "HorDist": 56.8
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
        }
    ],
}

response = requests.post('http://127.0.0.1:8000/Test2', headers=headers, json=json_data)
print(response)

