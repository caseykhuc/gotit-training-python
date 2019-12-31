import json
from storefront_config import StorefrontConfig


class FileController():
    # read_file(file_name: string): StorefrontConfig
    @staticmethod
    def read_file(file_name):
        content = json.loads(open(file_name).read())
        return StorefrontConfig(content)

    # write_file(object: StorefrontConfig, file_name: string)
    @staticmethod
    def write_file(object, file_name):
        f = open(file_name, 'w')
        f.write(json.dumps(object.data, indent=4))
