# -*- coding : utf-8 -*-
import os
import json
from turtle import Shape
from typing import Text
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

Dataframe = pd.read_excel('Customization_Cluster.xlsx')
CustomOptionList = ['piano_shape', 'piano_texture', 'piano_palette', 'piano_interval', 'piano_line', 'drum_shape', 'drum_texture',
                    'drum_color_h', 'drum_color_l', 'haptic_sensitivity', 'haptic_intensity']
ShapeOption = {0:'circle', 1:'square', 2:'triangle', 3:'star', 4:'decagon'}
TextureOption = {0:'none', 1:'paper', 2:'wood', 3:'stone'}
PaletteOption = {0:'saturation', 1:'luminance', 2:'RGB', 3:'OGV', 4:'YCP', 5:'GBP', 6:'Rainbow', 7:'Red-Yellow', 8:'Green-Cyan', 9:'Blue-Violet', 10:'Nothing'}
LineOption = {1:True, 0:False}


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
clusters = [
            [0, 0, 6, 90, 1, 0, 0, 2, 98, 91, 84],
            [0, 1, 6, 60, 1, 0, 3, 17, 54, 29, 23],
            [0, 0, 6, 58, 1, 4, 0, 2, 99, 28, 19],
            [1, 0, 6, 19, 1, 0, 0, 252, 97, 40, 15],
            [3, 0, 6, 89, 1, 1, 3, 119, 60, 65, 57],
            [4, 1, 1, 42, 0, 4, 0, 79, 63, 36, 13],
            [0, 0, 0, 60, 1, 0, 1, 319, 52, 36, 36],
            [0, 0, 2, 51, 1, 4, 0, 185, 51, 17, 10],
            [1, 0, 6, 79, 1, 0, 0, 231, 54, 67, 48]
            ]

for index, cluster in enumerate(clusters):
    print(ShapeOption[cluster[0]], TextureOption[cluster[1]], PaletteOption[cluster[2]], cluster[3], LineOption[cluster[4]], ShapeOption[cluster[5]], TextureOption[cluster[6]], cluster[7], cluster[8], cluster[9], cluster[10])
    Dataframe_Cluster = Dataframe[Dataframe['cluster']==index]
    # print(clusters[index])
    print(Dataframe_Cluster.loc[:,['Round']].to_numpy().T)

# for i in range(9):
#     Dataframe_Cluster = Dataframe[Dataframe['cluster']==i]
#     print(clusters[i])
#     print(Dataframe_Cluster.loc[:,['Round']])

