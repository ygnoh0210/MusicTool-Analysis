# -*- coding:utf-8 -*-

import json
import os
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


shape = pd.DataFrame({'Modality': ['(ST)Sound+Tactile', '(SV)Sound + Visual'],
                   'circle': [37.5, 65],
                   'square': [33.33, 15], 
                   'triangle':[4.16, 10],
                   'pentagram':[16.66, 0],
                   'decagram':[8.33, 10]})
texture = pd.DataFrame({'Modality': ['(ST)Sound+Tactile', '(SV)Sound + Visual'],
                   'none': [50, 65],
                   'paper': [25, 25], 
                   'wood':[4.16, 10],
                   'stone':[20.83, 0]})
colorset=pd.DataFrame({'Modality': ['(ST)Sound+Tactile', '(SV)Sound + Visual'],
                   'level 1': [0, 0],
                   'level 2': [0, 20], 
                   'level 3':[25, 30],
                   'level 4':[0, 0],
                   'level 5': [75, 50]})

sns.set(style="white")
shape.set_index('Modality').plot(kind='bar', stacked=True)
plt.title("Shape")
plt.ylabel("(%)")
plt.xlabel("Preference of Modality")
plt.xticks(rotation=0)
plt.show()

sns.set(style="white")
texture.set_index('Modality').plot(kind='bar', stacked=True)
plt.title("Shape")
plt.ylabel("(%)")
plt.xlabel("Preference of Modality")
plt.xticks(rotation=0)
plt.show()

sns.set(style="white")
colorset.set_index('Modality').plot(kind='bar', stacked=True)
plt.title("Shape")
plt.ylabel("(%)")
plt.xlabel("Preference of Modality")
plt.xticks(rotation=0)
plt.show()