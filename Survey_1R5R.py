# -*- coding:utf-8 -*-

import os
import pandas as pd
import openpyxl
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

participants= {1:'김민지', 2:'유승민', 3:'차진선', 4:'김도영', 5:'허성지', 6:'윤상철', 7:'권용진', 8:'김선우', 9:'노지현', 10:'성지훈', 11:'고단아', 12:'이민희',
               13:'이현아', 14:'정원철', 15:'장세일', 16:'서영희', 17:'김상운', 18:'김향미', 19:'왕재완', 20:'박명기', 21:'박승언', 22:'최수백', 23:'서미금'}

conditions=['only music', 'music + visual', 'music + haptic', 'music + visual + haptic']
music_num=['1번', '2번', '3번', '4번']

def raw_load():
    global total_1R5R
    total_1R5R=pd.read_excel('./Data/ListeningSurvey_1R5R.xlsx')

def question_ttest():
    for q in range(9):
        quest='Q'+str(q+1)
        result=stats.ttest_ind(first_total[quest], fifth_total[quest])
        print("T-test Q"+str(q+1), result)


def making_combination_df():
    global combination_df
    combination_df=first_total.copy()
    pd.set_option('display.max_columns', 0)
    pd.set_option('display.max_rows', 0)

    for j in range(9):
        combination_df["after Q"+str(j+1)]=0

    for p in participants.keys():
        for m in music_num:
            for c in conditions:
                target=fifth_total[(fifth_total['이름']==p)&(fifth_total['음악']==m)&(fifth_total['조건']==c)]
                if len(target)!=0:
                    target_index = combination_df.loc[(combination_df['이름']==p)&(combination_df['음악']==m)&(combination_df['조건']==c)].index
                    for q in range(9):
                        # combination_df.loc[(combination_df['이름']==p)&(combination_df['음악']==m)&(combination_df['조건']==c), "after Q"+str(q+1)]=target["Q"+str(q+1)]
                        value = int(target["Q"+str(q+1)].iloc[0])
                        combination_df.loc[target_index, "after Q"+str(q+1)] = value


def question_paired_ttest():
    # print(combination_df)
    for q in range(9):
        # combination_df[["Q"+str(q+1) , "after Q"+str(q+1)]].display()
        before=combination_df["Q"+str(q+1)]
        after=combination_df["after Q"+str(q+1)]
        paired_ttest_result=stats.ttest_rel(before, after)
        print("Paired T-test Q"+str(q+1), paired_ttest_result)


def question_wilcoxon():
     for q in range(9):
        before=combination_df["Q"+str(q+1)]
        after=combination_df["after Q"+str(q+1)]
        wilcoxon_result=stats.wilcoxon(before, after)
        print("Wilcoxon Q"+str(q+1), wilcoxon_result)
        # sns.boxplot(x="Q"+str(q+1), y="after Q"+str(q+1), data=combination_df)
        # plt.show()



# 데이터 로드
raw_load()

# 1회기, 5회기 전체 data 
first_total=total_1R5R[total_1R5R['회기']=='1회차']
fifth_total=total_1R5R[total_1R5R['회기']=='5회차']

# Question 마다 1R vs 5R ttest
print("Listening Survey 1 Round vs 5 Round\n\n\n")

question_ttest()
print("\n")
making_combination_df()
question_paired_ttest()
print("\n")
question_wilcoxon()