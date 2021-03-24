import pytest
from labolatorium1.general_lib import Machine, Task

def test_init_test():
    expected = 12
    machine = Machine(expected)

    assert machine.tasks == []
    assert machine.get_id() == expected

def test_empty_task_list():
    machine = Machine(0)

    assert machine.get_number_of_tasks() == 0

def test_basic_example():
    machine = Machine(0)
    a = Task(1)
    b = Task(2)

    machine.add_task_duration(a, 10)
    machine.add_task_duration(b, 20)

    machine.add_task(a)
    machine.add_task(b)

    assert machine.get_number_of_tasks() == 2

