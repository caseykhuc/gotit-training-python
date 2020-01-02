import re

# delete_trailing_comma(str): str
def delete_trailing_comma(str):
    quote = False
    regex = re.compile(r''',(?!\s*[{["'])''')

    # list of all trailing commas
    commas = [i.start() for i in regex.finditer(str)]

    # list of commas to delete
    result_str = ""

    # loop through str to avoid commas in the middle of string value
    for i, char in enumerate(str):
        if char == '"':
            if i > 0 and str[i-1] == '\\':
                result_str += char
                continue
            quote = not quote

        # char is outside of any quotes
        if not quote and i in commas:
            continue
        result_str += char

    return result_str

if __name__ == "__main__":
    delete_trailing_comma(open('data.json').read())