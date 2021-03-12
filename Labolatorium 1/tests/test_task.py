import pytest
from labolatorium1.general_lib import Task

def test_basic_not_eq():
    a = Task(2)
    b = Task(1)

    assert a.get_id() != b.get_id()
    assert a != b

def test_basic_eq():
    a = Task(1)
    b = Task(1)

    assert a.get_id() == b.get_id()
    assert a == b
