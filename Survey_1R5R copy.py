# -*- coding:utf-8 -*-

import os
import pandas as pd
import openpyxl

participants= {1:'김민지', 2:'유승민', 3:'차진선', 4:'김도영', 5:'허성지', 6:'윤상철', 7:'권용진', 8:'김선우', 9:'노지현', 10:'성지훈', 11:'고단아', 12:'이민희',
               13:'이현아', 14:'정원철', 15:'장세일', 16:'서영희', 17:'김상운', 18:'김향미', 19:'왕재완', 20:'박명기', 21:'박승언', 22:'최수백', 23:'서미금'}

conditions=['only music', 'music + visual', 'music + haptic', 'music + visual + haptic']
first_score= [[]for _ in range(4)]
last_score=[[]for _ in range(4)]

def raw_load():
    global total_1R5R
    total_1R5R=pd.read_excel('./Data/ListeningSurvey_1R5R.xlsx')

def extract(round_num):
    round_name=str(round_num)+"회차"
    target=total_1R5R[total_1R5R['회기']==round_name]
    for i, c in enumerate(conditions):
        temp=target[target['조건']==c]
        for q in range(9):
            quest="Q"+str(q+1)
            if round_num==1: 
                first_score[i].append(temp[quest])
            elif round_num==5: 
                last_score[i].append(temp[quest])
            
    

def p_confirm():
    for i, key in enumerate(participants.keys()):
        tttemp=total_1R5R[total_1R5R['이름']==key]
        print(key, participants[key], len(tttemp))
        print(tttemp)
        print("\n\n\n")


# 데이터 로드
raw_load()

# 사용자별 데이터 프린팅 
# p_confirm()

# 회기별 데이터 추출
extract(1)
# print(first_score)
extract(5)

for i, c in enumerate(conditions):
    # print("\nCondition : ", c)
    for q in range(9):
        # print(first_score[i][q], "#", last_score[i][q])
        print("Q"+str(q+1)+", 1회기:"+str(first_score[i][q])+", 5회기:"+str(last_score[i][q]))
    # print("Total, 1회기:"+str(round(sum(first_score[i])/9, 2))+", 5회기:"+str(round(sum(last_score[i])/9, 2)))





