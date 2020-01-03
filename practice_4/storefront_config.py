def update(current, changes):
    """Update current dict by changes dict"""

    if type(changes) == list:
        for i in range(len(changes)):
            # recursively update each element if changes/current is a list of list/dictionary
            update(current[i], changes[i])
        return
    if type(current) == dict:
        for k, v in changes.items():
            if type(v) != dict and type(v) != list:
                # assign to new value when v is not of collection types
                current[k] = changes[k]
            else:
                update(current[k], changes[k])
        return


class StorefrontConfig:
    """Class model entities for data

    Attributes:
        data: string
    """

    def __init__(self, data):
        """Init class with data"""
        self.data = data

    def update(self, modify_data):
        """Update"""
        update(self.data, modify_data)


if __name__ == "__main__":
    store = StorefrontConfig({"id": 300})
    store.update({"id": 200})
    print(store.data)