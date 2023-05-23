"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def smartphone():
    return Item('Смартфон', 10000, 20)


def test_item_calculate_total_price(smartphone):
    smartphone.calculate_total_price()
    assert smartphone.total_price == 200000

def test_item_apply_discount(smartphone):
    smartphone.apply_discount()
    assert smartphone.price == 10000