# -*- coding:utf-8 -*-

import json
import os
import pandas as pd

participants= {3:'차진선', 4:'김도영', 6:'윤상철', 9:'노지현', 10:'성지훈', 16:'서영희', 17:'김상운', 18:'김향미', 19:'왕재완', 20:'박명기', 21:'박승언', 22:'최수백', 23:'서미금'}
info_answer={"A" :[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 2, 2],
             "B" :[2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 3, 3],
             "C" :[1, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1],
             "D" :[1, 1, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 3, 3, 1, 1]}
logged=dict()
total=dict()
for p in participants.keys():
    total[p]=[]


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
            click.append(clicking)
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
    if((round_num!=1)&(round_num!=5)):
        for i in range(len(score)):
            if(i%2==0):
                score[i]=0
    total[participant_num].append([score, time, click])
    print(key,"P", value, round_num, "회기, 점수", sum(total[key][round_num-1][0]), ", 문제 Type:", G_type)
    print("score: ", total[key][round_num-1][0])
    print("time: ", total[key][round_num-1][1])
    print("click: ", total[key][round_num-1][2])
    print('\n')


for key, value in participants.items():
    for i in range(5):
        raw_load(key, value, i+1)
        test_scoring(key, i+1)
        # print(key, "#", value, "#", i+1, "#", sum(total[key][i][0]))

        
    print('\n')
    




