# -*- coding:utf-8 -*-

from cProfile import label
import json
import os
from turtle import title
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

participants= {1:'김민지', 2:'유승민', 3:'차진선', 4:'김도영', 5:'허성지', 6:'윤상철', 7:'권용진', 8:'김선우', 9:'노지현', 10:'성지훈', 11:'고단아', 12:'이민희',
            14:'정원철', 15:'장세일', 16:'서영희', 17:'김상운', 18:'김향미', 19:'왕재완', 20:'박명기', 21:'박승언', 22:'최수백', 23:'서미금'}

info_answer={"A" :[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 2, 2],
             "B" :[2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 3, 3],
             "C" :[1, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1],
             "D" :[1, 1, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3, 1, 1]}

logged=dict()
total=dict()
conclude_sound=dict()
scored=dict()

for p in participants.keys():
    total[p]=[]
    conclude_sound[p]=[]


def raw_load(num, name, round):
    path='./Data/P'+str(num)+'_'+name+'/'+str(round)+'회기/'
    file_list=os.listdir(path)
    for file_name in file_list:
        if('Group' in file_name):
            # print(str(num)+name+str(round)+file_name)
            save_bool=False
            with open(path+file_name) as f:
                json_object=json.load(f)
                data=[]
                for key, value in json_object.items():
                    value=value.split('#')
                    group=file_name.split("Group")
                    if(len(value)==5):
                        if value[3]!='Submit':
                            save_bool=True
                        data.append([value[1], value[3], value[4], group[1][0]])
            if save_bool:
                df=pd.DataFrame(data, columns=['TimeStamp', 'Action', 'Answer', 'Group'])
                logged["P"+str(num)+"R"+str(round)]=df


def test_scoring(participant_num, round_num):
    logged_info=logged["P"+str(participant_num)+"R"+str(round_num)]
    score=[]
    time= []
    click=[]
    answer_candi=0
    clicking=0
    time_stamp=int(logged_info['Answer'][0])
    for i in range(len(logged_info)):
        clicking+=1
        G_type=logged_info['Group'][i]
        if logged_info['Action'][i]=="SelectedAnswer":
            answer_candi=int(logged_info['Answer'][i])
        elif logged_info['Action'][i]=="Submit":
            clocking=int(logged_info['TimeStamp'][i])-time_stamp
            time.append(round(clocking/1000, 2))
            click.append(clicking-1)
            q_num=int(logged_info['Answer'][i])
            if answer_candi==0:
                # 답 제출 x 
                score.append(0)
            elif(answer_candi==info_answer[G_type][q_num]):
                # 정답
                score.append(1)
            else:
                # 오답
                score.append(0)
            time_stamp=int(logged_info['TimeStamp'][i])
            answer_candi=0
            clicking=0
    # 2, 3, 4 회기에서 문제 추가로 푼사람 score 0 설정 
    # if((round_num!=1)&(round_num!=5)):
    print(score)
    score[17]=0
    score[16]=0
    time[17]=0
    time[16]=0
    if round_num==1:
        conclude_sound[participant_num][0]=sum(score)
        conclude_sound[participant_num][2]=sum(time)
        conclude_sound[participant_num][4]=sum(click)
    elif round_num==5: 
        conclude_sound[participant_num][1]=sum(score)
        conclude_sound[participant_num][3]=sum(time)
        conclude_sound[participant_num][5]=sum(click)
    for i in range(len(score)):
        if(i%2==0):
            score[i]=0
            time[i]=0
            click[i]=0

    total[participant_num].append([score, time, click])
    

    scored[participant_num][round_num-1]=sum(score)
    scored[participant_num][round_num+4]=sum(time)
    scored[participant_num][round_num+9]=sum(click)

def wilcoxon(before_round, after_round, df_name):
    target=["score"]
    for t in target:
        before=df_name[str(before_round)+"R_"+t]
        after=df_name[str(after_round)+"R_"+t]
        wilcoxon_result=stats.wilcoxon(before, after)
        print(t+" - "+str(before_round)+"Round vs "+str(after_round)+"Round  :  ", wilcoxon_result)

def paired_ttest(before_round, after_round, df_name):
    target=["time", "click"]
    for t in target:
        before=df_name[str(before_round)+"R_"+t]
        after=df_name[str(after_round)+"R_"+t]
        paired_ttest_result=stats.ttest_rel(before, after)
        print(t+" - "+str(before_round)+"Round vs "+str(after_round)+"Round  :  ", paired_ttest_result)
    print("\n")

def visualization(type):
    target=["score", "time", "click"]
    if type=="before-after compare":
        for t in target:
            fig, ax=plt.subplots()
            ax.boxplot([conclude_df["1R_"+t], conclude_df["5R_"+t]], 
                    labels=["1R", "5R"])
            plt.title("1Round vs 5Round "+t)
            # plt.show()
            # sns.boxplot(x="1R_"+t, y="5R_"+t, data=conclude_df)
            

    elif type=="two round compare":
        for t in target: 
            for i in range(4):
                sns.boxplot(x=str(i+1)+"R_"+t, y=str(i+2)+"R_"+t, data=scored_df)
                plt.title(str(i+1)+"Round vs "+str(i+2)+"Round "+t)
                # if t=="score":
                #     plt.axis([0, 9, 0, 9])
                # plt.show()
    elif type=="total round compare":
        for t in target:
            fig, ax=plt.subplots()
            ax.boxplot([scored_df["1R_"+t],scored_df["2R_"+t], scored_df["3R_"+t], scored_df["4R_"+t], scored_df["5R_"+t]], 
                    labels=["1R", "2R", "3R", "4R", "5R"])
            plt.title("Total Round Compare  "+t)
            # plt.show()



for key, value in participants.items():
    scored[key]=[[] for _ in range(15)]
    conclude_sound[key]=[[] for _ in range(6)]
    for i in range(5):
        raw_load(key, value, i+1)
        test_scoring(key, i+1)

writer=pd.ExcelWriter('./Result/InfoTest Result except9Q.xlsx', engine='openpyxl')


# sound 문제 포함 결과
conclude_df =pd.DataFrame(conclude_sound)
conclude_df=conclude_df.transpose()
conclude_df.columns=["1R_score", "5R_score", "1R_time", "5R_time", "1R_click", "5R_click"]

# (sound 문제 포함) 1R/5R score, time, click 분석 
conclude_df.to_excel(writer, "rawdata - round1 vs round 5")
conclude_df.describe().to_excel(writer, "result - round1 vs round 5")
wilcoxon(1, 5, conclude_df)
paired_ttest(1, 5, conclude_df)

# sound 문제 미포함 결과 
scored_df=pd.DataFrame(scored)
scored_df=scored_df.transpose()
scored_df.columns=["1R_score", "2R_score", "3R_score", "4R_score", "5R_score", "1R_time", "2R_time", "3R_time", "4R_time", "5R_time", "1R_click", "2R_click", "3R_click", "4R_click", "5R_click"]
# 더 자세한 옵션 프린팅 more options can be specified also
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
#     print(scored_df)

# (sound 문제 미포함) 1R/2R 2R/3R 3R/4R 4R/5R score, time, click 분석 
for i in range(4):
    scored_df.to_excel(writer, "rawdata - round"+str(i+1)+" vs round"+str(i+2))
    scored_df.describe().to_excel(writer, "round"+str(i+1)+" vs round"+str(i+2))
    wilcoxon(i+1, i+2, scored_df)
    paired_ttest(i+1, i+2, scored_df)
writer.save()

# 데이터 box plot 시각화 
visualization("before-after compare")
visualization("two round compare")
visualization("total round compare")
