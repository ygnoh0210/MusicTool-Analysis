# -*- coding:utf-8 -*-

import os
import pandas as pd
import openpyxl
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


participants= {1:'김민지', 2:'유승민', 3:'차진선', 4:'김도영', 5:'허성지', 6:'윤상철', 7:'권용진', 8:'김선우', 9:'노지현', 10:'성지훈', 11:'고단아', 12:'이민희',
              14:'정원철', 15:'장세일', 16:'서영희', 17:'김상운', 18:'김향미', 19:'왕재완', 20:'박명기', 21:'박승언', 22:'최수백', 23:'서미금'}
conditions=[1, 2, 3, 4]
music_num=['1번', '2번', '3번', '4번']

def raw_load():
    global total_1R5R
    total_1R5R=pd.read_excel('./Data/ListeningSurvey_1R5R.xlsx')

def p_confirm():
    for i, key in enumerate(participants.keys()):
        tttemp=total_1R5R[total_1R5R['이름']==key]
        print(key, participants[key], len(tttemp))
        print(tttemp)
        print("\n\n\n")

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
    #  conclude_df.to_excel(writer, "rawdata - round1 vs round 5")-
     for q in range(9):
        before=combination_df["Q"+str(q+1)]
        after=combination_df["after Q"+str(q+1)]
        
        wilcoxon_result=stats.wilcoxon(before, after)
        print("Wilcoxon Q"+str(q+1), wilcoxon_result)
        # sns.boxplot(x="Q"+str(q+1), y="after Q"+str(q+1), data=combination_df)
        # plt.show()

def condition_wilcoxon():
    for q in range(9):
        for c in conditions:
            before_temp=combination_df[combination_df['조건']==c]
            before=before_temp["Q"+str(q+1)]
            after_temp=combination_df[combination_df['조건']==c]
            after=after_temp["after Q"+str(q+1)]
            wilcoxon_result=stats.wilcoxon(before, after)
            print("Wilcoxon Condition:"+str(c)+"   Question:"+str(q+1), wilcoxon_result)
        print("\n")

# def q_and_c_wilcoxon():
    # sum result adding 
    


# 데이터 로드
raw_load()
p_confirm()
writer=pd.ExcelWriter('./Result/Suvey1R5R Result_v2.xlsx', engine='openpyxl')
# 1회기, 5회기 전체 data 
first_total=total_1R5R[total_1R5R['회기']=='1회차']
fifth_total=total_1R5R[total_1R5R['회기']=='5회차']

making_combination_df()

# question별 통계 분석 - wilcoxon
question_wilcoxon()
combination_df.to_excel(writer, "rawdata - Question 1 to 9")
combination_df.describe().to_excel(writer, "result - Question 1 to 9")
first_total.describe().to_excel(writer, "result - 1R")
fifth_total.describe().to_excel(writer, "result - 5R")

# condition별 통계분석 - wilcoxon 
condition_wilcoxon()
combination_df[combination_df['조건']==1].describe().to_excel(writer, "result c1 only music")
combination_df[combination_df['조건']==2].describe().to_excel(writer, "result c2 music + visual")
combination_df[combination_df['조건']==3].describe().to_excel(writer, "result c3 music + haptic")
combination_df[combination_df['조건']==4].describe().to_excel(writer, "result c4 music + visual + haptic")

# question 합산 결과 condition별 통계분석 - wilcoxon
q_and_c_wilcoxon()


writer.save()
