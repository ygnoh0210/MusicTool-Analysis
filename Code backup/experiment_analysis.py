#!/usr/bin/env python
# coding: utf-8

# # 실험 데이터 전체 분석

# In[1]:


import pandas as pd
import csv

phase_1 = pd.read_csv('../Desktop/phase_15.csv', encoding='cp949')
phase_234 = pd.read_csv('../Desktop/phase_234.csv')
phase_5 = pd.read_csv('../Desktop/phase_15.csv', encoding='cp949')


# In[2]:


phase_one = phase_1[phase_1['회기'] == '1회차']
phase_one_all = phase_one[phase_one['조건 '] == 'music + visual + haptic']
phase_one_all = phase_one_all.drop(['조건 '], axis=1)
phase_one_all


# In[3]:


phase_two = phase_234[phase_234['회차'] == '2회차']


# In[4]:


phase_three = phase_234[phase_234['회차'] == '3회차']


# In[5]:


phase_four = phase_234[phase_234['회차'] == '4회차']


# In[6]:


phase_five = phase_5[phase_5['회기'] == '5회차']
phase_five_all = phase_five[phase_five['조건 '] == 'music + visual + haptic']
phase_five_all = phase_five_all.drop(['조건 '], axis=1)


# In[7]:


def mean_by_questions(dataframe, columns):
    for i in range(4, len(columns)):
        print(columns[i], dataframe[columns[i]].mean())


# In[8]:


def question_lst_maker(dataframe, columns):
    question_lst = []
    for i in range(4, len(columns)):
        question_lst.append(columns[i])
    return question_lst


# In[9]:


def answer_lst_maker(dataframe, columns):
    answer_lst = []
    for i in range(4, len(columns)):
        answer_lst.append(dataframe[columns[i]].mean())
    return answer_lst


# In[10]:


def df_maker(dataframe, columns):
    question_lst = question_lst_maker(dataframe, columns)
    answer_lst = answer_lst_maker(dataframe, columns)
    df = pd.DataFrame(zip(question_lst, answer_lst), columns = ['Question', 'Answer'])
    return df


# ## 2,3,4 회기 전체 정리

# In[11]:


# phase_one_onlymusic = phase_one[phase_one['조건 '] == 'only music']
# phase_one_visual = phase_one[phase_one['조건 '] == 'music + visual']
# phase_one_haptic = phase_one[phase_one['조건 '] == 'music + haptic']
# phase_one_everything = phase_one[phase_one['조건 '] == 'music + visual + haptic']


# In[12]:


phase_two_columns = phase_two.columns
phase_three_columns = phase_three.columns
phase_four_columns = phase_four.columns


# In[13]:


two_df = df_maker(phase_two, phase_two_columns)
two_df


# In[14]:


three_df = df_maker(phase_three, phase_three_columns)
three_df


# In[15]:


four_df = df_maker(phase_four, phase_four_columns)
four_df


# In[16]:


df_by_234 = pd.concat([two_df, three_df, four_df], axis=1)
df_by_234


# In[17]:


df_by_234.to_excel('234phase_all.xlsx')


# ## 1, 5회기 전체 정리

# In[18]:


phase_one_columns = phase_one_all.columns
phase_five_columns = phase_five_all.columns


# In[19]:


one_df = df_maker(phase_one_all, phase_one_columns)
one_df


# In[20]:


five_df = df_maker(phase_five_all, phase_five_columns)
five_df


# In[21]:


df_by_12345 = pd.concat([one_df, two_df, three_df, four_df, five_df], axis=1)
df_by_12345.columns = ['질문', '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
df_by_12345 = df_by_12345.drop(['Question'], axis=1) 
df_by_12345.to_excel('12345_all.xlsx')


# In[22]:


df_by_12345


# In[23]:


# onlymusic_df = df_maker(phase_one_onlymusic, phase_one_columns)
# visual_df = df_maker(phase_one_visual, phase_one_columns)
# haptic_df = df_maker(phase_one_haptic, phase_one_columns)
# every_df = df_maker(phase_one_everything, phase_one_columns)


# In[24]:


# df_by_questions = pd.concat([onlymusic_df, visual_df, haptic_df, every_df], axis=1)
# df_by_questions.columns = ['Question', 'OnlyMusic', 'Question', 'Music+Visual', 'Question', 'Music+Haptic', 'Question', 'Music+Visual+Haptic']


# In[ ]:





# # 음악별 문항 점수 평균

# 전체 참여자 수: 23명
# - 분석1: 새로운 노래(5,6,7번 노래)를 들은 각 회기별로 점수 변화 비교 (2,3,4회기) 
# - 분석2: 전체 회기별로 동일한 노래(1,2,3,4번 노래)의 점수가 어떻게 변했나 비교 (1,2,3,4,5회기)

# ### 각 회기별 음악 점수 정의

# In[25]:


# 1회기
phase_one_all_1 = phase_one_all[phase_one_all['음악'] == '1번']
phase_one_all_2 = phase_one_all[phase_one_all['음악'] == '2번']
phase_one_all_3 = phase_one_all[phase_one_all['음악'] == '3번']
phase_one_all_4 = phase_one_all[phase_one_all['음악'] == '4번']


# In[26]:


# 2회기
phase_two_1 = phase_two[phase_two['노래 '] == 1]
phase_two_2 = phase_two[phase_two['노래 '] == 2]
phase_two_3 = phase_two[phase_two['노래 '] == 3]
phase_two_4 = phase_two[phase_two['노래 '] == 4]
phase_two_5 = phase_two[phase_two['노래 '] == 5]


# In[27]:


# 3회기
phase_three_1 = phase_three[phase_three['노래 '] == 1]
phase_three_2 = phase_three[phase_three['노래 '] == 2]
phase_three_3 = phase_three[phase_three['노래 '] == 3]
phase_three_4 = phase_three[phase_three['노래 '] == 4]
phase_three_6 = phase_three[phase_three['노래 '] == 6]


# In[28]:


# 4회기
phase_four_1 = phase_four[phase_four['노래 '] == 1]
phase_four_2 = phase_four[phase_four['노래 '] == 2]
phase_four_3 = phase_four[phase_four['노래 '] == 3]
phase_four_4 = phase_four[phase_four['노래 '] == 4]
phase_four_7 = phase_four[phase_four['노래 '] == 7]


# In[29]:


# 5회기
phase_five_all_1 = phase_five_all[phase_five_all['음악'] == '1번']
phase_five_all_2 = phase_five_all[phase_five_all['음악'] == '2번']
phase_five_all_3 = phase_five_all[phase_five_all['음악'] == '3번']
phase_five_all_4 = phase_five_all[phase_five_all['음악'] == '4번']


# ### 분석 1. new 노래별 비교한 데이터 프레임 만들기

# In[30]:


new_five_music = df_maker(phase_two_5, phase_two_columns)
new_five_music


# In[31]:


new_six_music = df_maker(phase_three_6, phase_three_columns)
new_six_music


# In[32]:


new_seven_music = df_maker(phase_four_7, phase_four_columns)
new_seven_music


# In[33]:


df_by_newmusic = pd.concat([new_five_music, new_six_music, new_seven_music], axis=1)
df_by_newmusic.columns = ['질문', '5번 음악', 'Question', '6번 음악', 'Question', '7번 음악']
df_by_newmusic = df_by_newmusic.drop(['Question'], axis=1) 
df_by_newmusic


# In[ ]:





# ### 분석 2. 공통 음악별 데이터프레임 만들기

# In[35]:


# 1번 음악
one_1_df = df_maker(phase_one_all_1, phase_one_columns)
two_1_df = df_maker(phase_two_1, phase_two_columns)
three_1_df = df_maker(phase_three_1, phase_three_columns)
four_1_df = df_maker(phase_four_1, phase_four_columns)
five_1_df = df_maker(phase_five_all_1, phase_five_columns)


# In[36]:


# 2번 음악
one_2_df = df_maker(phase_one_all_2, phase_one_columns)
two_2_df = df_maker(phase_two_2, phase_two_columns)
three_2_df = df_maker(phase_three_2, phase_three_columns)
four_2_df = df_maker(phase_four_2, phase_four_columns)
five_2_df = df_maker(phase_five_all_2, phase_five_columns)


# In[37]:


# 3번 음악
one_3_df = df_maker(phase_one_all_3, phase_one_columns)
two_3_df = df_maker(phase_two_3, phase_two_columns)
three_3_df = df_maker(phase_three_3, phase_three_columns)
four_3_df = df_maker(phase_four_3, phase_four_columns)
five_3_df = df_maker(phase_five_all_3, phase_five_columns)


# In[38]:


# 4번 음악
one_4_df = df_maker(phase_one_all_4, phase_one_columns)
two_4_df = df_maker(phase_two_4, phase_two_columns)
three_4_df = df_maker(phase_three_4, phase_three_columns)
four_4_df = df_maker(phase_four_4, phase_four_columns)
five_4_df = df_maker(phase_five_all_4, phase_five_columns)


# ### 데이터프레임 엑셀로 만들기

# In[39]:


df_by_music1 = pd.concat([one_1_df, two_1_df, three_1_df, four_1_df, five_1_df], axis=1)
df_by_music1.columns = ['1번 음악 질문', '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
df_by_music1 = df_by_music1.drop(['Question'], axis=1) 
df_by_music1.to_excel('music1_all.xlsx')


# In[40]:


df_by_music2 = pd.concat([one_2_df, two_2_df, three_2_df, four_2_df, five_2_df], axis=1)
df_by_music2.columns = ['2번 음악 질문', '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
df_by_music2 = df_by_music2.drop(['Question'], axis=1) 
df_by_music2.to_excel('music2_all.xlsx')


# In[41]:


df_by_music3 = pd.concat([one_3_df, two_3_df, three_3_df, four_3_df, five_3_df], axis=1)
df_by_music3.columns = ['3번 음악 질문', '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
df_by_music3 = df_by_music3.drop(['Question'], axis=1) 
df_by_music3.to_excel('music3_all.xlsx')


# In[42]:


df_by_music4 = pd.concat([one_4_df, two_4_df, three_4_df, four_4_df, five_4_df], axis=1)
df_by_music4.columns = ['4번 음악 질문', '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
df_by_music4 = df_by_music4.drop(['Question'], axis=1) 
df_by_music4.to_excel('music4_all.xlsx')


# In[43]:


# def music_df_maker_by_music(music_number):
#     df_by_music_music_number = pd.concat([one_music_number_df, two_music_number_df, three_music_number_df, four_music_number_df, five_music_number_df %music_number], axis=1)
#     df_by_music_music_number.columns = ['%d번 음악 질문'%music_number, '1회기', 'Question', '2회기', 'Question', '3회기', 'Question', '4회기', 'Question', '5회기']
#     df_by_music_music_number = df_by_musicmusic_number.drop(['Question'], axis=1)
#     df_by_music_music_number.to_excel('music%d_all.xlsx'%music_number)
#     return


# In[44]:


# phase_one_onlymusic_1 = phase_one_onlymusic[phase_one_onlymusic['음악'] == '1번']
# phase_one_onlymusic_2 = phase_one_onlymusic[phase_one_onlymusic['음악'] == '2번']
# phase_one_onlymusic_3 = phase_one_onlymusic[phase_one_onlymusic['음악'] == '3번']
# phase_one_onlymusic_4 = phase_one_onlymusic[phase_one_onlymusic['음악'] == '4번']


# In[45]:


# phase_one_visual_1 = phase_one_visual[phase_one_visual['음악'] == '1번']
# phase_one_visual_2 = phase_one_visual[phase_one_visual['음악'] == '2번']
# phase_one_visual_3 = phase_one_visual[phase_one_visual['음악'] == '3번']
# phase_one_visual_4 = phase_one_visual[phase_one_visual['음악'] == '4번']


# In[46]:


# phase_one_haptic_1 = phase_one_haptic[phase_one_haptic['음악'] == '1번']
# phase_one_haptic_2 = phase_one_haptic[phase_one_haptic['음악'] == '2번']
# phase_one_haptic_3 = phase_one_haptic[phase_one_haptic['음악'] == '3번']
# phase_one_haptic_4 = phase_one_haptic[phase_one_haptic['음악'] == '4번']


# In[47]:


# phase_one_everything_1 = phase_one_everything[phase_one_everything['음악'] == '1번']
# phase_one_everything_2 = phase_one_everything[phase_one_everything['음악'] == '2번']
# phase_one_everything_3 = phase_one_everything[phase_one_everything['음악'] == '3번']
# phase_one_everything_4 = phase_one_everything[phase_one_everything['음악'] == '4번']


# In[ ]:





# ### 2-1. (only music) 1회기 1번 음악

# In[48]:


# onlymusic_df_1 = df_maker(phase_one_onlymusic_1, phase_one_columns)
# visual_df = df_maker(phase_one_visual_1, phase_one_columns)
# haptic_df = df_maker(phase_one_haptic, phase_one_columns)
# every_df = df_maker(phase_one_everything, phase_one_columns)


# In[49]:


# df_maker(phase_one_onlymusic_1, phase_one_columns)


# In[ ]:




