from project import get_city_data
from project import get_weather
from project import get_emoji
import pytest


def main():
    test_get_city_data()
    test_get_weather()
    test_get_emoji()


def test_get_city_data():
    with pytest.raises(ValueError):
        get_city_data('not a city')
    with pytest.raises(ValueError):
        get_city_data('United States')
    with pytest.raises(ValueError):
        get_city_data('Loas Angeles')

def test_get_weather():
    assert get_weather("burbank", "bcfc2df24a378133f58290e10a59a5e0")
    assert get_weather("San Diego    ", "bcfc2df24a378133f58290e10a59a5e0")
    assert get_weather("Mecca", "bcfc2df24a378133f58290e10a59a5e0")


def test_get_emoji():
    assert get_emoji(0) == 'π₯Άπ₯Άπ₯Ά'
    assert get_emoji(40) == 'πππ'
    assert get_emoji(70) == 'πππ'
    assert get_emoji(100) == 'π₯΅π₯΅π₯΅'


if __name__ == "__main__":
    main()
