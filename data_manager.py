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

    result_list = []
    title_list = ['Name', 'Diameter', 'Climate', 'Terrain', 'Water', 'Population', 'Residents']
    name_list = []
    diamater_list = []
    climate_list = []
    terrain_list = []
    surface_water_list = []
    population_list = []
    residents_list = []

    for contents in result:
        for key, value in contents.items():
            if key == 'name':
                name_list.append(value)
            if key == 'diameter':
                if value == 'unknown':
                    diamater_list.append(value)
                else:
                    formatted_string = format_numbers(value)
                    diamater_list.append(formatted_string + ' km')
            if key == 'climate':
                climate_list.append(value)
            if key == 'terrain':
                terrain_list.append(value)
            if key == 'surface_water':
                if value == 'unknown':
                    surface_water_list.append(value)
                else:
                    surface_water_list.append(value + ' %')
            if key == 'population':
                if value == 'unknown':
                    population_list.append(value)
                else:
                    formatted_string = format_numbers(value)
                    population_list.append(formatted_string + ' people')
            if key == 'residents':
                if value == []:
                    residents_list.append('No known residents')
                else:
                    residents_list.append(Markup(
                        '<button class="btn-default btn-xs residents" data-residents="' + str(value) + '"' +
                        'data-planet-name="shit" data-toggle="modal" data-target="#residents">' +
                        str(len(value)) +
                        ' residents' +
                        '</button>'))

    for i in range(len(name_list)):
        result_list.append([])
        result_list[i].append(name_list[i])
        result_list[i].append(diamater_list[i])
        result_list[i].append(climate_list[i])
        result_list[i].append(terrain_list[i])
        result_list[i].append(surface_water_list[i])
        result_list[i].append(population_list[i])
        result_list[i].append(residents_list[i])

    result_list.insert(0, title_list)

    return {'result_list': result_list,
            'next_page_id': next_page_id,
            'prev_page_id': prev_page_id,
            'response': response}


def result_to_list(list_name):
    pass


def format_numbers(number_string):
    reversed_string = ''
    for i in range(len(number_string)):
        reversed_string += number_string[-i - 1]
        if (i + 1) % 3 == 0 and i != len(number_string) - 1:
            reversed_string += ','
    return reversed_string[::-1]
