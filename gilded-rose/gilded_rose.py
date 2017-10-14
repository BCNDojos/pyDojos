# -*- coding: utf-8 -*-

aged_brie = "Aged Brie"
backstage = "Backstage passes to a TAFKAL80ETC concert"
sulfuras = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            delta = 0
            if item.name == sulfuras:
                continue
            elif item.name == aged_brie:
                if item.quality < 50:
                    delta = delta + 1
                if item.sell_in <= 0 and item.quality + delta < 50:
                    delta = delta + 1
            elif item.name == backstage:
                if item.quality < 50:
                    delta = delta + 1
                if item.sell_in < 11 and item.quality + delta < 50:
                    delta = delta + 1
                if item.sell_in < 6 and item.quality + delta < 50:
                    delta = delta + 1
                if item.sell_in <= 0:
                    delta = -item.quality
            else:
                if item.quality > 0:
                    delta = -1
                if item.sell_in <= 0 and item.quality + delta > 0:
                    delta = delta - 1
            item.quality = item.quality + delta
            item.sell_in = item.sell_in - 1
