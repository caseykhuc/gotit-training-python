import re


def convert_sessions(s, sessions):
    d = {'1': 'one',
         '2': 'two',
         '3': 'three',
         '4': 'four',
         '5': 'five',
         '6': 'six',
         '7': 'seven',
         '8': 'eight',
         '9': 'nine'}
    return s.replace(sessions, d[sessions])


def convert_stars(s, stars):
    d = {'one': '1',
         'two': '2',
         'three': '3',
         'four': '4',
         'five': '5'}
    return s.replace(stars, d[stars])


def convert(s):
    regex = re.compile(r'^I completed (.*?) sessions and I rated my expert (.*?) stars$')
    number_of_sessions, number_of_stars = regex.match(inp).groups()

    return convert_stars(convert_sessions(s, number_of_sessions), number_of_stars)


inp = 'I completed 2 sessions and I rated my expert five stars'
print(convert(inp))