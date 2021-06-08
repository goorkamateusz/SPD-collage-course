from laboratorium4.priority_queue import PriorityQueue


def test_default_priority_queue():
    queue = PriorityQueue()

    assert queue.empty()

    queue.append(5)
    queue.append(-1)
    queue.append(10)
    queue.append(2)

    assert queue.top() == 10
    assert queue.pop() == 10

    assert queue.top() == 5
    assert not queue.empty()

    queue.pop()
    queue.pop()
    queue.pop()

    assert queue.empty()


def test_min_priority_queue():
    queue = PriorityQueue([10, 15, 5, 20, 25], reverse=True)

    assert queue.pop() == 5
    assert queue.pop() == 10
    assert queue.pop() == 15

    queue.append(-10)
    queue.append(10)

    assert queue.top() == -10


def test_custom_key_priority_queue():
    queue = PriorityQueue(('abcd', '123', 'ab', 'qwerty'), key=len)

    assert queue.pop() == 'qwerty'
    assert queue.pop() == 'abcd'
    assert queue.pop() == '123'
    assert queue.pop() == 'ab'
