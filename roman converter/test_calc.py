from calc import *
import pytest

@pytest.fixture(scope="module")
def initial():
    dict_of_vars = {
        'is_an_int': 12,
        'is_a_string': 'hello',
        'error_checker': ErrorChecker(),
        'calc_good_12': Calculator(12),
        'clac_good_12223': Calculator(12223),
        'calc_bad': Calculator('hi'),
    }
    return dict_of_vars


def test_is_int(initial):
    error_checker = initial['error_checker']
    assert error_checker._is_int(initial['is_an_int'], 'is_an_int') is True
    with pytest.raises(TypeError):
        error_checker._is_int(initial['is_a_string'], 'not_an_int')


def test_make_string(initial):
    assert initial['calc_good_12']._make_string() == '12'
    with pytest.raises(TypeError):
        initial['calc_bad']._make_string()

@pytest.fixture(scope="module")
def calc():
    yield Calculator(12)


def test_get_length(calc):
    calc_12345 = Calculator(12345)
    assert calc._get_length() == 2
    assert calc_12345._get_length() == 5


def test_get_dec(calc):
    assert calc._get_dec(1) == 10


def test_make_roman():
    calc_1 = Calculator(1)
    assert calc_1.make_roman() == 'I'

    calc_2231 = Calculator(2231)
    assert calc_2231.make_roman() == 'MMCCXXXI'

    calc_6 = Calculator(6)
    assert calc_6.make_roman() == 'VI'

    calc_large_num = Calculator(1066)
    assert calc_large_num.make_roman() == 'MLXVI'

    calc_9 = Calculator(9)
    assert calc_9.make_roman() == 'IX'

    calc_8 = Calculator(8)
    assert calc_8.make_roman() == 'VIII'

    calc_99 = Calculator(99)
    assert calc_99.make_roman() == 'XCIX'

    clac_49 = Calculator(49)
    assert clac_49.make_roman() == 'XLIX'

    calc_9999 = Calculator(9999)
    assert calc_9999.make_roman() == 'MMMMMMMMMCMXCIX'

    calc_too_long = Calculator(100000)
    with pytest.raises(UserWarning):
        calc_too_long.make_roman()


def test_remainder(calc):
    assert calc._remainder(6, 5) == 1
    assert calc._remainder(80, 50) == 30

def test_check_for_nine(calc):
    assert calc._check_for_nine(9, 10) is True
    assert calc._check_for_nine(8, 10) is False
    assert calc._check_for_nine(90, 100) is True

def test_how_many_times(calc):
    assert calc._how_many_times(6, 2) == 3
    assert calc._how_many_times(10, 2) == 5
    assert calc._how_many_times(2, 10) == 0
    assert calc._how_many_times(1000, 1000) == 1

@pytest.fixture(scope="module")
def roman():
    return RomanSymbols()


def test_roman_values(roman):
    roman_values = roman.get_roman_values()
    assert roman_values['I'] == 1
    assert roman_values['C'] == 100


def test_roman_keys(roman):
    roman_keys = roman.get_keys_in_order()
    assert roman_keys[0] == 'M'
    assert roman_keys[-1] == 'I'
