speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

for i, tezlik in sorted(speed.items(), key=lambda x: x[1], reverse=True):
    print(i, tezlik)