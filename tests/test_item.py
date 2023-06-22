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

def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_item_string_to_number():
    assert Item.string_to_number('523') == 523

def test_item_repr(smartphone):
    assert repr(smartphone) == "Item('Смартфон', 10000, 20)"

def test_item_str(smartphone):
    assert str(smartphone) == "Смартфон"