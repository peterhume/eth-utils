from eth_utils.functional import compose


def test_composition_no_functions():
    fn = compose()
    assert fn(5) == 5


def test_composition_single_function():
    def fn(x):
        return x * 2

    assert compose(fn)(5) == 10


def test_composition_multiple_function():
    def fn(x):
        return x + 1

    assert compose(fn, fn, fn)(5) == 8


def test_ordering_is_preserved():
    assert compose(
        lambda v: v * 3,
        lambda v: v + 1,
    )(1) == 4
