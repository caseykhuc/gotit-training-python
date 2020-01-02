from practice_2.step import Step
from practice_2.exception import InvalidValueException
import pytest


def test_init():
    # Arrange
    step = Step(2, 'five')

    # Act

    # Assert
    assert step.number_of_sessions == 'two'
    assert step.number_of_stars == '5'


def test_make_step():
    step = Step(2, 'five')

    assert step.make_step() == "I completed two sessions and I rated my expert 5 stars"


def test_invalid_value_exception():
    with pytest.raises(InvalidValueException) as e:
        Step(0, 'five')

    with pytest.raises(InvalidValueException):
        Step(2, 'ten')
