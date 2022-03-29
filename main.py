import random
destinations = ['Hong kong', 'Bangkok', 'London', 'Lahore', 'Singapore', 'Paris', 'Dubai', 'New York City', 'Kuala Lumpur', 'Istanbul']
transportation = ['taxi', 'bus', 'rental car', 'train', 'bike']
restaurants = ['city fameous restaurant', 'fancy restaurant', 'normal local restaurant', 'exotic food restaurant']
entertainment = ['sight seeing', 'visiting museums', 'watching plays', 'following tour guides', 'souvenir shopping']


def randomize_list(trip_list):
    limit = len(trip_list) - 1
    random_number = random.randint(0, limit)
    random_activity = trip_list[random_number]
    return random_activity

def user_input():
    has_acceped = False
    while has_acceped == False:
        users_response = input('enter yes or no: ')
        if users_response == 'yes':
            has_acceped = True
            return has_acceped
        elif users_response == 'no':
            has_acceped = False
            
        else:
            print('invalid input')

def select_destination():
    city = randomize_list(destinations)
    print(f'your destination is {city}, is this ok?')
    has_acceped = user_input()
    if has_acceped == False:
        select_destination()
    else:
        print(f'your destination is now {city} now!')
        return city

def select_transportation():
    ride = randomize_list(transportation)
    print(f'your transportation will be by {ride}, is this ok?')
    has_acceped = user_input()
    if has_acceped == False:
        select_transportation()
    else:
        print(f'your transportation will be by {ride} now!')
        return ride

def select_restuarant():
    food = randomize_list(restaurants)
    print(f'you will go to a {food} for food, is this ok?')
    has_acceped = user_input()
    if has_acceped == False:
        select_restuarant()
    else:
        print(f'your going to a {food} to eat now!')
        return food

def select_entertainment():
    thing_to_do = randomize_list(entertainment)
    print(f'your entertainment will be {thing_to_do}, is this ok?')
    has_acceped = user_input()
    if has_acceped == False:
        select_entertainment()
    else:
        print(f'{thing_to_do} will now be your activity in your trip!')
        return thing_to_do

def trip_comfirmation():
    city = select_destination()
    ride = select_transportation()
    food = select_restuarant()
    thing_to_do = select_entertainment()
    print(f'In your trip you will go to {city} and travel around by {ride}.')
    print(f'while there you will eat at a {food} and go {thing_to_do} for fun, is this ok?')
    has_acceped = user_input()
    if has_acceped == False:
        trip_comfirmation()
    else:
        print(f'have a safe trip! ') 

trip_comfirmation()