cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

eng_qimmat = max(cars.values())
eng_arzon = min(cars.values())

for i in cars:
    if cars[i] == eng_qimmat:
        print("Eng qimmat:", i)

    if cars[i] == eng_arzon:  
        print("Eng arzon:", i)