import datetime
import math

import charge as charge

CAR_PARK_LIST = {}


def add_car_to_list(plate_number):

    # Get the time of car getting into car park
    time_of_car_in = datetime.datetime.now()

    # Add car to the list of cars inside park
    CAR_PARK_LIST[plate_number] = time_of_car_in


def remove_car_from_list(plate_number):
    time_of_car_in = CAR_PARK_LIST[plate_number]
    time_of_car_out = datetime.datetime.now()
    charge = calculate_charge_for_parking(time_of_car_in, time_of_car_out)
    print("You are charged: ", charge, " for the parking.")
    return charge


def calculate_charge_for_parking(time_in, time_out):
    time_of_car_inside = abs(time_out - time_in)
    charge_carpark = math.ceil(time_of_car_inside.seconds / 3600 /3) * 2
    charge_garage = math.ceil(time_of_car_inside.seconds/3600) * 0.50
    charge_total = charge_carpark + charge_garage
    print('Charge: ', charge_total)
    return charge_total


def calculate_total_of_all_parking_charges():
    total = 0
    time_now = datetime.datetime.now()
    for car_plate in CAR_PARK_LIST.keys():
        this_car_charge = calculate_charge_for_parking(CAR_PARK_LIST[car_plate], time_now)
        total += this_car_charge
    print("Total charge of all cars parked ", total)


if __name__ == '__main__':
    car1 = 'dawdawdf2'
    add_car_to_list(car1)
    CAR_PARK_LIST[car1] += datetime.timedelta(hours=5)

    car2 = 'dadf2'
    add_car_to_list(car2)
    CAR_PARK_LIST[car2] += datetime.timedelta(minutes=180)

    car3 = 'df2'
    add_car_to_list(car3)
    CAR_PARK_LIST[car3] += datetime.timedelta(minutes=60)

    calculate_total_of_all_parking_charges()


    # try:
    #     remove_car_from_list(car1)
    # except Exception as e:
    #     print("No Car Plates Found In System: ", e)


