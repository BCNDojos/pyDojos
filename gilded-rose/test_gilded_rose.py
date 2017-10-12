# -*- coding: utf-8 -*-

from gilded_rose import GildedRose
from item import Item


def update_arrange(test_cases):
    # Arrange
    items = [test_case[0] for test_case in test_cases]
    gilded_rose = GildedRose(items)
    return items, gilded_rose


def update_assert(items, test_cases):
    # Assert
    for i, item in enumerate(items):
        assert item.sell_in == test_cases[i][1].sell_in
        assert item.quality == test_cases[i][1].quality


def test_normal_items():
    # Arrange
    test_cases = [
        (
            Item("+5 Dexterity Vest", 2, 4),
            Item("+5 Dexterity Vest", 1, 3),
        ),
        (
            Item("+5 Dexterity Vest", 1, 3),
            Item("+5 Dexterity Vest", 0, 2),
        ),
        (
            Item("+5 Dexterity Vest", 0, 2),
            Item("+5 Dexterity Vest", -1, 0),
        ),
        (
            Item("+5 Dexterity Vest", -1, 0),
            Item("+5 Dexterity Vest", -2, 0),
        ),
    ]
    items, gilded_rose = update_arrange(test_cases)
    # Act
    gilded_rose.update_quality()
    # Assert
    update_assert(items, test_cases)


def test_aged_brie_items():
    # Arrange
    test_cases = [
        (
            Item("Aged Brie", 2, 4),
            Item("Aged Brie", 1, 5),
        ),
        (
            Item("Aged Brie", 1, 5),
            Item("Aged Brie", 0, 6),
        ),
        (
            Item("Aged Brie", 0, 6),
            Item("Aged Brie", -1, 8),
        ),
        (
            Item("Aged Brie", -1, 49),
            Item("Aged Brie", -2, 50),
        ),
    ]
    items, gilded_rose = update_arrange(test_cases)
    # Act
    gilded_rose.update_quality()
    # Assert
    update_assert(items, test_cases)


def test_backstage_passes_items():
    # Arrange
    test_cases = [
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 20, 4),
            Item("Backstage passes to a TAFKAL80ETC concert", 19, 5),
        ),
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 5),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 7),
        ),
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 6),
            Item("Backstage passes to a TAFKAL80ETC concert", 4, 9),
        ),
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 6),
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 0),
        ),
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 9, 50),
        ),
        (
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 4, 50),
        ),
    ]
    items, gilded_rose = update_arrange(test_cases)
    # Act
    gilded_rose.update_quality()
    # Assert
    update_assert(items, test_cases)


def test_sulfuras_items():
    # Arrange
    test_cases = [
        (
            Item("Sulfuras, Hand of Ragnaros", 20, 4),
            Item("Sulfuras, Hand of Ragnaros", 20, 4),
        ),
        (
            Item("Sulfuras, Hand of Ragnaros", 0, 54),
            Item("Sulfuras, Hand of Ragnaros", 0, 54),
        ),
    ]
    items, gilded_rose = update_arrange(test_cases)
    # Act
    gilded_rose.update_quality()
    # Assert
    update_assert(items, test_cases)
