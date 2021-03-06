import random
destinations = ['Hong kong', 'Bangkok', 'London', 'Lahore', 'Singapore', 'Paris', 'Dubai', 'New York City', 'Kuala Lumpur', 'Istanbul']
transportation = ['taxi', 'bus', 'rental car', 'train', 'bike']
restaurants = ['city fameous restaurant', 'fancy restaurant', 'normal local restaurant', 'exotic food restaurant']
entertainment = ['sight seeing', 'visiting museums', 'watching plays', 'follow tour guides', 'souvenir shopping']


def randomize_list(trip_list):
    limit = len(trip_list) - 1
    random_number = random.randint(0, limit)
    random_activity = trip_list[random_number]
    return random_activity

def user_input():
    has_acceped = False
    while has_acceped == False:
        users_response = input('enter y - yes or n - no: \n')
        if users_response == 'y':
            has_acceped = True
            return has_acceped
        elif users_response == 'n':
            has_acceped = False
            return has_acceped
        else:
            print('invalid input\n')

def select_destination():
    has_acceped = False
    while has_acceped == False:
        city = randomize_list(destinations)
        print(f'your destination is {city}, is this ok?\n')
        has_acceped = user_input()
    print(f'your destination is now {city} now!\n')
    return city

def select_transportation():
    has_acceped = False
    while has_acceped == False:
        ride = randomize_list(transportation)
        print(f'your transportation will be by {ride}, is this ok?\n')
        has_acceped = user_input()
    print(f'your transportation will be by {ride} now!\n')
    return ride

def select_restuarant():
    has_acceped = False
    while has_acceped == False:
        food = randomize_list(restaurants)
        print(f'you will go to a {food} for food, is this ok?\n')
        has_acceped = user_input()
    print(f'your going to a {food} to eat now!\n')
    return food

def select_entertainment():
    has_acceped = False
    while has_acceped == False:
        thing_to_do = randomize_list(entertainment)
        print(f'your entertainment will be {thing_to_do}, is this ok?\n')
        has_acceped = user_input()
    print(f'{thing_to_do} will now be your activity in your trip!\n')
    return thing_to_do

def full_trip():
    city = select_destination()
    ride = select_transportation()
    food = select_restuarant()
    thing_to_do = select_entertainment()
    trip_confirmation(city, ride, food, thing_to_do)

def trip_confirmation(city, ride, food, thing_to_do):
    has_acceped = False
    while has_acceped == False:
        print(f'In your trip you will go to {city} and travel around by {ride}.')
        print(f'while there you will eat at a {food} and go {thing_to_do} for fun, is this ok?\n')
        has_acceped = user_input()
        if has_acceped == False:
            trip_recomfirmation(city, ride, food, thing_to_do)
            break
        else:
            print(f'Have a safe trip at {city}!')

def trip_recomfirmation(city, ride, food, thing_to_do):
    print('what do you want to change?\n')
    user_input = input('enter c - city, r - ride, f - food, e - entertainment, or a - all: \n')
    if user_input == 'a':
        city = select_destination()
        ride = select_transportation()
        food = select_restuarant()
        thing_to_do = select_entertainment()
        pass
    elif user_input == 'c':
        city = select_destination()
    elif user_input == 'r':
        ride = select_transportation()
    elif user_input == 'f':
        food = select_restuarant()
    elif user_input == 'e':
        thing_to_do = select_entertainment()
    else:
        print('invalid input\n')
    trip_confirmation(city, ride, food, thing_to_do)


full_trip()