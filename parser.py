import requests
import json
from classes import Challenge


def delimiter(text):
    text = text.split('\n')
    return text


def find_needed_line(text):
    for line in text:
        if 'data-react-props=' in str(line):
            index1 = line.find('props=') + 7
            index2 = line.find('"></div>')
            new_line = (line[index1:index2])
            return new_line


def find_needed_line_2(text):
    inform_for_result = []
    for i in text:
        if '<title>' in i:
            name = i.strip('<title>').strip('</')
            inform_for_result.append(name)
    for i in range(len(text)):
        if "<span class='challenge-date'>" in text[i]:
            date = text[i + 1]
            inform_for_result.append(date)
    for i in text:
        if '<strong>' in i:
            description = i.strip('<strong>').strip('</')
            inform_for_result.append(description)
    return inform_for_result


def common_function(id_number):
    res = requests.get('https://www.strava.com/challenges/' + str(id_number))
    all_inform = res.text
    if 'data-react-props=' in all_inform:
        pre_json = find_needed_line(delimiter(all_inform))

        json_file = pre_json.replace('&quot;', '"')
        final_json = json.loads(json_file)

        challenge = Challenge(final_json)

        result = challenge.title + '\n' * 2
        result += challenge.date + '\n' * 2
        result += ', '.join(list(map(lambda x: x.text, challenge.activities))) + '\n' * 2
        result += 'https://www.strava.com/challenges/' + str(id_number)
    else:
        name = find_needed_line_2(delimiter(all_inform))[0]
        date = find_needed_line_2(delimiter(all_inform))[1].replace('</strong>', '').replace('<strong>', '')
        description = find_needed_line_2(delimiter(all_inform))[2]
        result = name + '\n' * 2
        result += date + '\n' * 2
        result += description + '\n' * 2
        result += 'https://www.strava.com/challenges/' + str(id_number)

    return result
