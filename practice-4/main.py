from modify_data import modify_data
from file_controller import FileController

file_controller = FileController()
config = file_controller.read_file("data.json")
config.update(modify_data)
file_controller.write_file(config, "result.json")
