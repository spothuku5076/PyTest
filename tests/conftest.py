import pytest

from source.circle import *
# conftest is a global for fixtures, these fixtures are accessed by all the files in this package.
@pytest.fixture
def my_circle():
    c=Circle(10)
    return c


@pytest.fixture
def my_rectangle():
    r=Rectangle(10,20)
    return r