import pytest

from loto import generate_unique_numbers

# tests for: generate_unique_numbers

testlen = 80
testmin = 0
testmax = 100


def test_positiveinput_lencorrect():
    actual = generate_unique_numbers(testlen, testmin, testmax)
    assert len(actual) == testlen


def test_positiveinput_correctvalues():
    actual = generate_unique_numbers(testlen, testmin, testmax)
    for item in actual:
        assert (testmin <= item <= testmax)


def test_positiveinput_uniquevalues():
    actual = generate_unique_numbers(testlen, testmin, testmax)
    assert len(set(actual)) == testlen


def test_positiveinput_maxpossiblecount():
    maxpossiblelen = 101
    actual = generate_unique_numbers(maxpossiblelen, testmin, testmax)
    assert len(actual) == maxpossiblelen


def test_positiveinput_lentoobig():
    impossiblelen = 102
    with pytest.raises(ValueError):
        generate_unique_numbers(impossiblelen, testmin, testmax)


def test_countzero_resultempty():
    assert len(generate_unique_numbers(0, testmin, testmax)) == 0


def test_maxlessthanmin_raises():
    with pytest.raises(ValueError):
        generate_unique_numbers(100, 2000, 1500)
