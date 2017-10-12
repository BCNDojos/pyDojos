# -*- coding: utf-8 -*-

from gilded_rose import GildedRose
from item import Item


def test_normal_items():
    # Arrange
    test_case = (
        Item("+5 Dexterity Vest", 2, 4),
        Item("+5 Dexterity Vest", 1, 3),
    )
    items = [test_case[0]]
    gilded_rose = GildedRose(items)
    # Act
    gilded_rose.update_quality()
    # Assert
    for item in items:
        assert item.sell_in == test_case[1].sell_in
        assert item.quality == test_case[1].quality
