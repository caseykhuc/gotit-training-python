import json
from practice_4.storefront_config import StorefrontConfig
from practice_4.validate_json import delete_trailing_comma


class FileController:
    """Handle read and write json from/to file"""
    def __init__(self):
        pass

    @staticmethod
    def read_file(file_name):
        """Loaded data from file

        Return: StorefrontConfig object containing a corresponding dictionary
        """
        file_content = open(file_name).read()
        file_content = json.loads(delete_trailing_comma(file_content))
        return StorefrontConfig(file_content)

    @staticmethod
    def write_file(obj, file_name):
        """Write data from StorefrontConfig obj to file"""
        f = open(file_name, 'w')
        f.write(json.dumps(obj.data, indent=4))
