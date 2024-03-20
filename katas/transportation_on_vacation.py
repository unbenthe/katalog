def rental_car_cost(d):
    n = 40
    money = n * d
    if d <= 1:
        return n
    if d >= 7:
        return money - 50
    if d >= 3:
        return money - 20
    
