# -*- coding:utf-8 -*-

import json
import os
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt



total=pd.read_excel('./Data/Modality_Custom_compare.xlsx')
DHH_total=pd.read_excel('./Data/Modality_Custom_DHH_compare.xlsx')
writer=pd.ExcelWriter('./Result/Modality_Custom.xlsx', engine='openpyxl')
DHH_writer=pd.ExcelWriter('./Result/Modality_Custom_DHH.xlsx', engine='openpyxl')

haptic_prefer=total[total["prefer"]=='haptic']
visual_prefer=total[total["prefer"]=='visual']
L_understand=DHH_total[DHH_total["understand"]=="L"]
M_understand=DHH_total[DHH_total["understand"]=="M"]
H_understand=DHH_total[DHH_total["understand"]=="H"]
L_understand.describe().to_excel(DHH_writer, "L_understand")
M_understand.describe().to_excel(DHH_writer, "M_understand")
H_understand.describe().to_excel(DHH_writer, "H_understand")
DHH_writer.save()

col=total.columns
DHH_col=DHH_total.columns

def auditory(): 
    print(L_understand)
    for i,  c in enumerate(DHH_col):
        if i>2:
            fig, ax = plt.subplots()
            ax.boxplot([L_understand[c], M_understand[c], H_understand[c]], labels=["L", "M", "H"])
            plt.title("Understand L vs M vs H "+c)
            # plt.savefig("D vs HH "+c)
            plt.show()
            



def prefer():
    for i, c in enumerate(col):
        if i>1:
            fig, ax=plt.subplots()
            ax.boxplot([haptic_prefer[c], visual_prefer[c]], labels=["haptic_prefer", "visual_prefer"])
            plt.title("haptic prefer vs visaul prefer "+c)
            plt.savefig("haptic prefer vs visaul prefer "+c)
            # plt.show()


# writer.save()

def make_df(test):
    df = pd.DataFrame(test)
    # df.columns=['haptic', 'visual']
    print(df)

def chi_square():
    piano_shape=[[3, 4, 1, 2, 2], [7, 1, 0, 0, 2]]
    piano_texture=[[6, 4, 0, 2], [6, 2, 2, 0]]
    drum_shape=[[2, 3, 1, 1, 5], [5, 1, 1, 0, 3]]
    drum_texture=[[6, 2, 1, 3], [7, 3, 0, 0]]
    shape=[[5, 7, 2, 3, 7], [12, 2, 1, 0, 5]]
    texture=[[12, 6, 1, 5], [13, 5, 2, 0]]
    TestList = [piano_shape, piano_texture, drum_shape, drum_texture,  shape, texture]
    # res=stats.chi2_contingency(shape)
    # print(res)
    for target in TestList:
        # make_df(target)
        res=stats.chi2_contingency([target[0], target[1]])
        print(res)
        
# prefer()
auditory()
# chi_square()

