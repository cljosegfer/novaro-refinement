#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:34:43 2022

@author: jose
"""

import pandas as pd
from refinement import refinement

# input
calc_mode = 'analytical'

item_type = 'lvl4'
ref_mode = 'ws'

item_value = 850 / 0.7 / 0.5 / 0.5 / 0.3
material_value = 20
enriched_value = 7200
bs_value = 10000


# calculate
pilebunker = refinement(item_type, 
                        item_value, material_value, enriched_value, bs_value)
upgrade = 9
print(pilebunker.calculate(calc_mode, upgrade, ref_mode))
