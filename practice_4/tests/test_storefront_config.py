from practice_4.storefront_config import StorefrontConfig
import pytest


@pytest.mark.parametrize("data",
                         ['abc', 'xyz'])
def test_init(data):
    store = StorefrontConfig(data)
    assert store.data == data


@pytest.mark.parametrize("data, modified_data",
                         [
                             ({"id": 300}, {"id": 200}),
                             ({
                                  "id": 300,
                                  "name": "One"
                              },
                              {
                                  "id": 200,
                                  "name": "One"
                              })
                         ])
def test_update(data, modified_data):
    store = StorefrontConfig(data)
    store.update({"id": 200})
    assert store.data == modified_data
