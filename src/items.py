#!/usr/bin/env python3

from classes import Item
from collections import OrderedDict


# unlock chapter of -1 will help indicate a non-buyable item
items = OrderedDict([('potion', Item(name='potion',
                                     price=10,
                                     is_use=True,
                                     desc='restore 10 hp',
                                     unlock_chapter=1)),
                     ('coffee', Item(name='coffee',
                                     price=50,
                                     is_use=True,
                                     desc='too fast',
                                     unlock_chapter=2)),
                     ('poison flask', Item(name='poison flask',
                                           price=50,
                                           is_use=True,
                                           desc='deal extra poison damage',
                                           unlock_chapter=2)),
                     ('protein shake', Item(name='protein shake',
                                            price=50,
                                            is_use=True,
                                            desc='temporary hp increase',
                                            unlock_chapter=2)),
                     ('sharpening oil', Item(name='sharpening oil',
                                             price=50,
                                             is_use=True,
                                             desc='temporary damage increase',
                                             unlock_chapter=2)),
                     ('energy bar', Item(name='energy bar',
                                         price=50,
                                         is_use=True,
                                         desc='???',
                                         unlock_chapter=2)),
                     ('leather helmet', Item(name='leather helmet',
                                             price=5,
                                             is_equip=True,
                                             desc='to put on the head',
                                             unlock_chapter=1,
                                             equip_type='head',
                                             equip_bonus=1)),
                     ('leather armor', Item(name='leather armor',
                                            price=5,
                                            is_equip=True,
                                            desc='wear it proudly',
                                            unlock_chapter=1,
                                            equip_type='body',
                                            equip_bonus=2)),
                     ('leather shin guards', Item(name='leather shin guards',
                                                  price=5,
                                                  is_equip=True,
                                                  desc='no table injuries',
                                                  unlock_chapter=1,
                                                  equip_type='legs',
                                                  equip_bonus=1)),
                     ('stone hammer', Item(name='stone hammer',
                                           price=5,
                                           is_equip=True,
                                           desc='to hit on the head',
                                           unlock_chapter=1,
                                           equip_type='weapon',
                                           equip_bonus=3)),
                     ('dyslexia potion', Item(name='dyslexia potion',
                                              price=20,
                                              is_use=True,
                                              desc='pretty beet',
                                              unlock_chapter=1)),
                     ('beef jerky', Item(name='beef jerky',
                                         price=20,
                                         is_use=True,
                                         desc='satisfies your hunger',
                                         unlock_chapter=1)),
                     ('alphabet soup', Item(name='alphabet soup',
                                            price=20,
                                            is_use=True,
                                            desc='only the right letters',
                                            unlock_chapter=1)),
                     ('sharpie', Item(name='sharpie',
                                      price=20,
                                      is_use=True,
                                      desc='scratch that',
                                      unlock_chapter=1)),
                     ('hero trophy', Item(name='hero trophy',
                                          price=0,
                                          is_special=True,
                                          desc='present from the king',
                                          unlock_chapter=-1)),
                     ])

use_items = OrderedDict([(name, item) for name, item in items.items()
                         if item.is_use])
