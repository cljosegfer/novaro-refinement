#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:42:03 2022

@author: jose
"""

import pandas as pd

# read probabilities table
DATA_PATH = 'probabilities/'

normal = pd.read_csv(DATA_PATH + 'normal.csv', index_col = 0)
ws = pd.read_csv(DATA_PATH + 'ws.csv', index_col = 0)
enriched = pd.read_csv(DATA_PATH + 'enriched.csv', index_col = 0)

class refinement:
    def __init__(self, item_type, item, material = 20, enriched = 7000, bs = 10000):
        # refinement mode
        self.item_type = item_type
        
        # values
        self.item = item
        self.material = material
        self.enriched = enriched
        self.bs = bs
    
    def calculate(self, calc_mode, upgrade, ref_mode):
        if calc_mode == 'analytical':
            return self.analytical(upgrade, ref_mode)
        # elif calc_mode == 'simulation':
        #     return simulation(upgrade)
    
    def analytical(self, upgrade, mode):
        if mode == 'normal':
            p = normal.loc[upgrade, self.item_type]
            C = (self.item + self.material) / p
        elif mode == 'ws':
            p = ws.loc[upgrade, self.item_type]
            C = (self.item + self.material) / p
        elif mode == 'enriched':
            p = ws.loc[upgrade, self.item_type]
            C = (self.item + self.material + self.enriched) / p
        elif mode == 'enriched + bs':
            p = ws.loc[upgrade, self.item_type]
            C = (self.material + self.enriched + self.bs) / p
        return C
    
    