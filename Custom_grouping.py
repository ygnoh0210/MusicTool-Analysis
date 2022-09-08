# -*- coding:utf-8 -*-

import json
import os
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt




total=pd.read_excel('./Data/Modality_Custom_DHH_compare.xlsx')
writer=pd.ExcelWriter('./Result/Custom_Combination.xlsx', engine='openpyxl')


# L_understand=DHH_total[DHH_total["understand"]=="L"]
# M_understand=DHH_total[DHH_total["understand"]=="M"]
# H_understand=DHH_total[DHH_total["understand"]=="H"]
# DHH_writer.save()

# col=total.columns
col=total.columns
            
def compare():
    Haptic_Low=total[(total["prefer"]=='haptic')&(total["understand"]=='L')]
    Haptic_High=total[(total["prefer"]=='haptic')&(total["understand"]=='H')]
    Visual_Low=total[(total["prefer"]=='visual')&(total["understand"]=='L')]
    Visual_High=total[(total["prefer"]=='visual')&(total["understand"]=='H')]
    Haptic_Low.describe().to_excel(writer, "Haptic Low")
    Haptic_High.describe().to_excel(writer, "Haptic High")
    Visual_Low.describe().to_excel(writer, "Visual Low")
    Visual_High.describe().to_excel(writer, "Visual High")
    writer.close()
    

    # print(Haptic_High)
    for i, c in enumerate(col):
        if i>2: 
            fig, ax=plt.subplots()
            ax.boxplot([Haptic_Low[c], Haptic_High[c], Visual_Low[c], Visual_High[c]], labels=["Haptic Low", "Haptic High", "Visual Low", "Visual High"])
            plt.title("Combination "+c)
            # plt.savefig("Combination"+c)




compare()