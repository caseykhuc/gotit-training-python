"""update dictionary by a dictionary"""
def update(current, changes):
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


""" Class model entities for data """
class StorefrontConfig:
    # __init__(data: object)
    def __init__(self, data):
        self.data = data

    # update(modify_data: object)
    def update(self, modify_data):
        update(self.data, modify_data)