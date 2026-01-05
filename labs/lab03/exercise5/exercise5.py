def get_position(cars, car_number):
    for i in range (len(cars)):
        if cars[i] == car_number:
            return i
    return -1

def has_overtaken(before, after, car1, car2):
    car1_bef = get_position(before, car1)
    car2_bef = get_position(before, car2)

    car1_after = get_position(after, car1)
    car2_after = get_position(after, car2)

    if car1_bef > car2_bef and car1_after < car2_after:
        return True
    return False
