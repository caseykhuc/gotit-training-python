import re


def delete_trailing_comma(string):
    """Return json-like string without any trailing commas"""
    quote = False
    regex = re.compile(r''',(?!\s*[{["'])''')

    # list of all trailing commas
    commas = [i.start() for i in regex.finditer(string)]

    # list of commas to delete
    result_string = ""

    # loop through string to avoid commas in the middle of stringing value
    for i, char in enumerate(string):
        if char == '"':
            if i > 0 and string[i-1] == '\\':
                result_string += char
                continue
            quote = not quote

        # char is outside of any quotes
        if not quote and i in commas:
            continue
        result_string += char

    return result_string
