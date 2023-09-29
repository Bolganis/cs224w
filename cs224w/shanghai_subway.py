import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

#定一个可视化函数
def dram(G,pos,measures,measure_name):
    plt.figure(figsize=(20,20))
    node = nx.draw_network_nodes(G,pos,node_size=250,cmap=plt.cm.plasma,node_color=list(measure.values()),nodelist=measures.key())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01,linscale=1,base=10))
    edge = nx.draw_networkx_edges(G,pos)

    plt.title(measure_name,fontsize=30)
    plt.axis('off')
    plt.show

#定义一个按值排序的字典
def dict_sort_by_value(dict_input):
    return sorted(dict_input.items(),key=lambda x : x[1] ,reverse=True )

df = pd.read_csv('./csv/shanghai_subway.csv')

#创建无向图
G = nx.Graph()

for idx,row in df.iterrows():
    G.add_edges_from([(row['前一站'],row['后一站'])],line=row['地铁线'],time=row['时间'])

# a = len(G)
# b = len(G.nodes)
# c = len(G.edges)
# print(a,b,c)



f = input('请输入出发站点：')
g = input('请输入目的站点：')

#最短路径
# nx.has_path(G,source=f,target=g)
totalstation = nx.shortest_path_length(G,source=f,target=g,weight='time')


shorted_path_list = nx.shortest_path(G,source=f,target=g,weight='time' )

a = 0
for i in range(len(shorted_path_list)-1):
    previous_station = shorted_path_list[i]
    next_station = shorted_path_list[i+1]
    line_id = G.edges[(previous_station,next_station)]['line']
    if a != 0:
        if a != line_id :
            line_id != a 
            print('\n请在{}站换乘{}号线！！！'.format(previous_station,line_id))
    a = line_id
    time = G.edges[(previous_station,next_station)]['time']
    print('{}--->{} {}号线 {}分钟'.format(previous_station,next_station,line_id,time))
    

#最短路径长度   
print('\n共计{}分钟'.format(nx.shortest_path_length(G,source=f,target=g,weight='time')))
print('共经过{}个站点'.format(len(shorted_path_list)-1))