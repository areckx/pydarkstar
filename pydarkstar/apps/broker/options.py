# -*- coding: utf-8 -*-
"""
Buy and sell items on the auction house.
"""
from ..basicoptions import BasicOptions
from ..inputoptions import InputOptions
from ..sqloptions import SQLOptions
from ..ahoptions import AHOptions


class Options(AHOptions, InputOptions, SQLOptions, BasicOptions):
    """
    Reads options from config file, then from command line.
    """
    def __init__(self):
        super(Options, self).__init__(description=__doc__)
        self.restock = 3600  # restock tick
        self.tick = 30  # buying interval
        self.add_argument('--restock', type=int, default=self.restock, metavar='int', help='restock interval (seconds)')
        self.add_argument('--tick', type=int, default=self.tick, metavar='int', help='buying interval (seconds)')


if __name__ == '__main__':
    pass
