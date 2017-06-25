import requests
import queries
import re
from flask import Markup, session


def parse_planets_data(page_id):
    response = requests.get('http://swapi.co/api/planets/?page={}'.format(page_id)).json()
    result = response['results']
    prev_button = response['previous']
    next_button = response['next']

    if prev_button is not None:
        prev_page_id = prev_button.split('=')[1].strip()
    if next_button is not None:
        next_page_id = next_button.split('=')[1].strip()
    if prev_button is None:
        prev_page_id = None
    if next_button is None:
        next_page_id = None

    title_list = ['Name', 'Diameter', 'Climate', 'Terrain', 'Water', 'Population', 'Residents']
    name_list = get_value('name', result)
    diamater_list = get_value('diameter', result)
    climate_list = get_value('climate', result)
    terrain_list = get_value('terrain', result)
    surface_water_list = get_value('surface_water', result)
    population_list = get_value('population', result)
    residents_list = get_value('residents', result)
    planet_url_list = get_value('url', result)
    result_list = []

    if 'username' in session:
        title_list.append('Vote')
        planet_url_list = get_value('url', result)
        user_id = queries.get_user_id(session['username'])[0][0]

    # concatenate and modify list items
    for i in range(len(name_list)):
        result_list.append([])
        result_list[i].append(name_list[i])
        if diamater_list[i] == 'unknown':
            result_list[i].append(diamater_list[i])
        else:
            formatted_string = format_numbers(diamater_list[i])
            result_list[i].append(formatted_string + ' km')
        result_list[i].append(climate_list[i])
        result_list[i].append(terrain_list[i])
        if surface_water_list[i] == 'unknown':
            result_list[i].append(surface_water_list[i])
        else:
            result_list[i].append(str(surface_water_list[i]) + ' %')
        if population_list[i] == 'unknown':
            result_list[i].append(population_list[i])
        else:
            formatted_string = format_numbers(population_list[i])
            result_list[i].append(formatted_string + ' people')
        if residents_list[i] == []:
            result_list[i].append('No known residents')
        else:
            result_list[i].append(Markup(
                        '<button class="btn-default btn-xs residents" ' +
                        'data-residents="' + str(', '.join(residents_list[i])) + '" ' +
                        'data-planet-name="' + str(name_list[i]) + '" ' +
                        'data-toggle="modal" data-target="#residents">' +
                        str(len(residents_list[i])) + ' residents</button>'))
        if 'username' in session:
            result_list[i].append(Markup('<button class="btn-warning btn-xs add-vote" ' +
                                         'data-planet-id="' + str(get_planet_id(planet_url_list[i])) + '" ' +
                                         'data-user-id="' + str(user_id) + '">Add vote</button>'))

    result_list.insert(0, title_list)

    return {'result_list': result_list,
            'next_page_id': next_page_id,
            'prev_page_id': prev_page_id,
            'response': response}


def get_value(string_key, result):
    value_list = []
    for item in result:
        for key, value in item.items():
            if key == str(string_key):
                value_list.append(value)
    return value_list


def format_numbers(number_string):
    reversed_string = ''
    for i in range(len(number_string)):
        reversed_string += number_string[-i - 1]
        if (i + 1) % 3 == 0 and i != len(number_string) - 1:
            reversed_string += ','
    return reversed_string[::-1]


def get_planet_id(_string):
    return re.search(r"\d+", _string).group(0)
