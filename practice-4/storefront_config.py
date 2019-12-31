class StorefrontConfig():
    # __init__(data: object)
    def __init__(self, data):
        self.data = data

    # update(modify_data: object)
    def update(self, modify_data):
        self.data.update(modify_data)
