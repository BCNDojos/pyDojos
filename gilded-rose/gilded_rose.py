# -*- coding: utf-8 -*-

aged_brie = "Aged Brie"
backstage = "Backstage passes to a TAFKAL80ETC concert"
sulfuras = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != aged_brie and item.name != backstage:
                if item.quality > 0:
                    if item.name != sulfuras:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == backstage:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != sulfuras:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != aged_brie:
                    if item.name != backstage:
                        if item.quality > 0:
                            if item.name != sulfuras:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
