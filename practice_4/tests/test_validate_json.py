from practice_4.validate_json import delete_trailing_comma
import pytest


@pytest.mark.parametrize("string, validated",
                         [
                             ('''{
                                  "id": 300,
                                  "name": "One",
                              }''',
                              '''{
                                  "id": 300,
                                  "name": "One"
                              }'''),
                             ('{"name": "abc,",}', '{"name": "abc,"}')
                         ])
def test_delete_trailing_comma(string, validated):
    assert delete_trailing_comma(string) == validated
