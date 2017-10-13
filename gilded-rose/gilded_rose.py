# -*- coding: utf-8 -*-

aged_brie = "Aged Brie"
backstage = "Backstage passes to a TAFKAL80ETC concert"
sulfuras = "Sulfuras, Hand of Ragnaros"


def arrange_quality(item):
    if item.quality > 50:
        item.quality = 50
    if item.quality < 0:
        item.quality = 0


def get_quality_differential(item, thresholds=None, expired=False):
    quality_differential = 1
    if thresholds is None:
        thresholds = []
    if expired:
        quality_differential = -item.quality
    else:
        for threshold in thresholds:
            if item.sell_in < threshold:
                quality_differential += 1
    return quality_differential


def increase_quality(item, thresholds=None, expired=None):
    quality_differential = get_quality_differential(item, thresholds, expired)
    item.quality += quality_differential
    arrange_quality(item)


def decrease_quality(item, thresholds):
    item.quality -= get_quality_differential(item, thresholds)
    arrange_quality(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == sulfuras:
                continue
            elif item.name == aged_brie:
                increase_quality(item, [1])
            elif item.name == backstage:
                increase_quality(item, [11, 6], item.sell_in < 1)
            elif item.name.startswith("Conjured"):
                decrease_quality(item, [item.sell_in + 1])
            else:
                decrease_quality(item, [1])
            item.sell_in -= 1
