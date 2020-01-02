import json
from storefront_config import StorefrontConfig
from validate_json import delete_trailing_comma

# handle read and write from file
class FileController:
    def __init__(self):
        pass

    # read_file(file_name: string): StorefrontConfig
    @staticmethod
    def read_file(file_name):
        file_content = open(file_name).read()
        file_content = json.loads(delete_trailing_comma(file_content))
        return StorefrontConfig(file_content)

    # write_file(object: StorefrontConfig, file_name: string)
    @staticmethod
    def write_file(object, file_name):
        f = open(file_name, 'w')
        f.write(json.dumps(object.data, indent=4))
