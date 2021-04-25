from laboratorium4.priority_queue import PriorityQueue


def test_default_priority_queue():
    queue = PriorityQueue()

    assert queue.empty()

    queue.insert(5)
    queue.insert(-1)
    queue.insert(10)
    queue.insert(2)

    assert queue.top() == 10
    assert queue.extract() == 10

    assert queue.top() == 5
    assert not queue.empty()

    queue.extract()
    queue.extract()
    queue.extract()

    assert queue.empty()


def test_min_priority_queue():
    queue = PriorityQueue([10, 15, 5, 20, 25], reverse=True)

    assert queue.extract() == 5
    assert queue.extract() == 10
    assert queue.extract() == 15

    queue.insert(-10)
    queue.insert(10)

    assert queue.top() == -10


def test_custom_key_priority_queue():
    queue = PriorityQueue(('abcd', '123', 'ab', 'qwerty'), key=len)

    assert queue.extract() == 'qwerty'
    assert queue.extract() == 'abcd'
    assert queue.extract() == '123'
    assert queue.extract() == 'ab'
