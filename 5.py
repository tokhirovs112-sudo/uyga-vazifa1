car = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

engkop=max(car.values())
engkam=min(car.values())
for i in car :
    if car[i] ==engkop:
        print("Eng kop sotilgan: ", i, engkop)
    elif car[i]== engkam:
        print("Eng kam sotilgan: ", i, engkam)


