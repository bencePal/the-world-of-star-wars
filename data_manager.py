import requests
from flask import Markup


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
    result_list = []

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
