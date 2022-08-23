# -*- coding : utf-8 -*-
import os
import json
import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.cluster import KMeans
from kmodes.kprototypes import KPrototypes
from sklearn.manifold import TSNE

Dataframe = pd.read_excel('Customization.xlsx')
English_Round = ['3Round', '4Round', '5Round']
CustomOptionList = ['piano_shape', 'piano_texture', 'piano_palette', 'piano_interval', 'piano_line', 'drum_shape', 'drum_texture',
                    'drum_color_h', 'drum_color_l', 'haptic_sensitivity', 'haptic_intensity']
Categorical_CustomOption = ['piano_shape', 'piano_texture', 'piano_palette', 'piano_line', 'drum_shape', 'drum_texture']
Numeric_CustomOption = ['piano_interval', 'drum_color_h', 'drum_color_l', 'haptic_sensitivity', 'haptic_intensity']

ShapeOption = {0:'circle', 1:'square', 2:'triangle', 3:'star', 4:'decagon'}
TextureOption = {0:'none', 1:'paper', 2:'wood', 3:'stone'}
PaletteOption = {0:'saturation', 1:'luminance', 2:'RGB', 3:'OGV', 4:'YCP', 5:'GBP', 6:'Rainbow', 7:'Red-Yellow', 8:'Green-Cyan', 9:'Blue-Violet', 10:'Nothing'}
LineOption = {1:True, 0:False}

Round3_Column = []
Round4_Column = []
Round5_Column = []
for i in CustomOptionList:
    Round3_Column.append('3Round_'+i)
    Round4_Column.append('4Round_'+i)
    Round5_Column.append('5Round_'+i)

Round3_Dataframe = Dataframe.loc[:, Round3_Column]
Round4_Dataframe = Dataframe.loc[:, Round4_Column]
Round5_Dataframe = Dataframe.loc[:, Round5_Column]

Round3_Dataframe.columns = CustomOptionList
Round4_Dataframe.columns = CustomOptionList
Round5_Dataframe.columns = CustomOptionList

pd.set_option('display.max_rows', None)
Whole_Dataframe = pd.concat([Round3_Dataframe, Round4_Dataframe, Round5_Dataframe])
Whole_Array = Whole_Dataframe.to_numpy(dtype=np.float32)

def plot_elbow_curve(start, end, data):
    no_of_clusters = list(range(start, end+1))
    cost_values = []
    
    for k in no_of_clusters:
        test_model = KPrototypes(n_clusters=k, init='Huang', random_state=42)
        test_model.fit_predict(data, categorical=[0, 1, 2, 4, 5, 6])
        cost_values.append(test_model.cost_)
        
    sns.set_theme(style="whitegrid", palette="bright", font_scale=1.2)
    
    plt.figure(figsize=(15, 7))
    ax = sns.lineplot(x=no_of_clusters, y=cost_values, marker="o", dashes=False)
    ax.set_title('Elbow curve', fontsize=18)
    ax.set_xlabel('No of clusters', fontsize=14)
    ax.set_ylabel('Cost', fontsize=14)
    ax.set(xlim=(start-0.1, end+0.1))
    plt.show()
    
# Plotting elbow curve for k=2 to k=12
# plot_elbow_curve(2,12,Whole_Dataframe)

# print(Whole_Dataframe)

def clustering(k):
    # KProtypeModel = KPrototypes(n_clusters=9, init='Huang', random_state=42)
    KProtypeModel = KPrototypes(n_clusters=k, init='Huang', random_state=42)
    clusters = KProtypeModel.fit_predict(Whole_Array, categorical=[2])
    # print(clusters)
    centroids = KProtypeModel.cluster_centroids_
    print("K is ",k)
    print(centroids)
    for i in centroids:
        centroid = []
        for item in i:
            centroid.append(round(item))

        real_centroid = [centroid[0], centroid[1], centroid[10], centroid[2], centroid[3], centroid[4], centroid[5], centroid[6], centroid[7], centroid[8], centroid[9]]
        print(centroid[0], "#", centroid[1],"#", centroid[10], "#", centroid[2], "#",centroid[3], "#",centroid[4], "#",centroid[5], "#",centroid[6], "#",centroid[7], "#",centroid[8],"#", centroid[9])
        # print(ShapeOption[real_centroid[0]], "#", TextureOption[real_centroid[1]],  "#", PaletteOption[real_centroid[2]],  "#", real_centroid[3],  "#", LineOption[real_centroid[4]],  "#", ShapeOption[real_centroid[5]], "#",  TextureOption[real_centroid[6]],  "#", real_centroid[7], "#",  real_centroid[8],  "#", real_centroid[9],  "#", real_centroid[10])
        # print(len(i), real_centroid)
    print("===========")
    return clusters

# kmeanModel = KMeans(n_clusters=8)
# kmeanModel.fit(Whole_Dataframe)
# print(kmeanModel.cluster_centers_)
clusters=clustering(4)
Cluster_Dataframe = Whole_Dataframe.copy()
Cluster_Dataframe['cluster'] = clusters
Cluster_Dataframe.to_excel("Customization_Cluster.xlsx")





#------------------------------------------------------------
Xtsne = TSNE(n_components=2).fit_transform(Whole_Dataframe)
Xtsne_Dataframe = pd.DataFrame(Xtsne)




fig, axes = plt.subplots(1, 3)
for i, k in enumerate([4, 9]):
    cluster = clustering(k)
    Xtsne_Dataframe_copy = Xtsne_Dataframe.copy()
    Xtsne_Dataframe_copy['cluster'] = cluster
    Xtsne_Dataframe_copy.columns = ['x1', 'x2', 'cluster']
    # print(Xtsne_Dataframe_copy)
    # ColorPalette = sns.color_palette("husl", 9)
    ColorPalette = sns.color_palette("Set1", k)
    sns.scatterplot(data=Xtsne_Dataframe_copy, x='x1',y='x2',s=200, hue='cluster', palette=ColorPalette, legend="full",alpha=0.5, ax=axes[i])
    # sns.scatterplot(data=Xtsne_Dataframe, x='x1',y='x2',s=200, hue='cluster', legend="full",alpha=0.5)
plt.show()


# distortions = []

# K = range(1, 15)
# for k in K:
#     kmeanModel = KMeans(n_clusters=k)
#     kmeanModel.fit(Whole_Dataframe)
#     distortions.append(kmeanModel.inertia_)

# plt.figure(figsize=(16,8))
# plt.plot(K, distortions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Distortion')
# plt.title('The Elbow Method showing the optimal k')
# plt.show()

# Optimal Amounts of Clusters are 8