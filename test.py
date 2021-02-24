import pytest
from main import Friend

def test_age():
    a = Friend("a")
    a.celebrate_birthday()
    assert a.age == 1