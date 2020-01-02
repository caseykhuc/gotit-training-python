def update(current, changes):
    """Update current dict by changes dict"""
    if type(changes) == list:
        for i in range(len(changes)):
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

    # update(modify_data: object)
    def update(self, modify_data):
        """Update"""
        update(self.data, modify_data)