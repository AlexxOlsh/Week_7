import requests
import datetime


url = 'https://66095c000f324a9a28832d7e.mockapi.io/users'


def get_user_id_by_name(name):
    response = requests.get(f'{url}?name={name.replace(" ", "%20" )}')
    result = response.json()
    if len(result) > 0:
        print(f'I find {name}')
        for item in result:
            print(item['id'])
    else:
        print(f'No {name} found')
    print('-------------------')


def get_usercount_state(count):
    params = {'limit': count}
    response = requests.get(url, params=params)
    result = response.json()
    i = 0
    state = 0
    for item in result:
        if i < 76:
            state += float(item['state'])
            i += 1
    print(f'{count} users state is {round(state, 2)}')
    print('-------------------')


def create_new_user(name, state):
    response = requests.post(url, data={'name': name, "state": state})
    if response:
        print(f'User {name} added')
        print('-------------------')


def get_oldest_user():
    params = {'orderBy': 'birth', 'order': 'asc'}
    response = requests.get(url, params=params)
    if response:
        result = response.json()
        print(f'The oldest user is {result[0]['name']}: {result[0]['birth']}')
        print('-------------------')


def get_poorest_user():
    response = requests.get(url)
    if response:
        result = response.json()
        res = min(result, key=lambda x: float(x['state']))
        print(f'The poorest user is {res['name']}: {res['state']}')
        print('-------------------')


def get_user_birth_by_month(month):
    months_map = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    response = requests.get(url)
    if response:
        result = response.json()
        count = 0
        for item in result:
            if item['birth'].split('-')[1] == month:
                count += 1
        print(f'The number of users born in {months_map[month]} is {count}')


get_user_id_by_name('Wilson VonRueden')
get_usercount_state(76)
create_new_user('Tom Holland', "1000000")
get_oldest_user()
get_poorest_user()
get_user_birth_by_month('04')
