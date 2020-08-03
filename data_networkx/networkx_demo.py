#import load data functions stored in utility_functions.py (see git repository)
import utility_functions as util
import pandas as pd
#import networkx and matpolotlib
import networkx as nx
import matplotlib

#Load the data -- courtesy of https://www.baseball-reference.com/teams/MIN/2019-schedule-scores.shtml
data=util.loadCSVfile('Twins2019Schedule.csv')
opacity_table = util.loadCSVfile('hex_opacity_table.csv')

#instantiate the Network X graph object
G=nx.Graph()

#Add a node for the Twins -- I am going to make it blue so it is distinguished.  Color is added as a property of the node.  You will see why this is important when the network diagram is rendered.

G.add_node('MIN',color='#0000FF',size=500)

#create weights lookup table to distinguish Teams played more in the schedule.  This will naturally depict in the graph by the distance from the central node.  The more times the opposing Team plays the Twins, the closer they will reside to MIN.  To make even more visually easier to see, the size of each entry will also be proportional to the number of games played.

opponent_dic = data['Opp'].value_counts().to_dict()

#List the percentage games played against the Twins in a dictionary

opponent_percent = {}
for i in opponent_dic:
    opponent_percent[i]=round((opponent_dic[i]/162)*100)

#Add nodes for the opposing Teams.  To make it easier to see I've added opposing Teams ad red. The size of the nodes gets larger proportional to the number of games played against the Twins.  In other words, larger dot, more games played.

for i in range(len(data)):
    G.add_node(data.iloc[i,5], color='red',size=opponent_dic[data.iloc[i,5]]*100)


#Add the connections or 'edges' to the network diagram.

for i in range(len(data)):
    G.add_edges_from([(data.iloc[i,3],data.iloc[i,5],{'weight': opponent_dic[data.iloc[i,5]]})])

#assign colors and node sizes.  This iterates through each node object and creates a list showing the colors and sizes cooresponding to the in the G object.  Given the index of the list matches the index of the object, when we render the image in later steps the color and sizes are assigned to the correct node.

node_color=[]
node_size=[]
for node in G.nodes():
    color = G.nodes[node]['color']
    node_color.append(color)
    size = G.nodes[node]['size']
    node_size.append(size)

#draw the network digram!

nx.draw(G, with_labels=True,node_color= node_color,node_size=node_size)