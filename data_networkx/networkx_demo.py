#import load data functions stored in utility_functions.py (see git repository)
import utility_functions as util
import pandas as pd
#import networkx and matpolotlib
import networkx as nx
import matplotlib

#Load the data courtesy of https://www.baseball-reference.com/teams/MIN/2019-schedule-scores.shtml
data=util.loadCSVfile('Twins2019Schedule.csv')

#Instantiate the Network X graph object.
G=nx.Graph()

#Add a node for the Twins.  I am going to make it blue and a size of 500 so it is distinguished.  Color is added as a property of the node.  You will see why this is important and used in laters steps to provide color to the image.

G.add_node('MIN',color='#0000FF',size=500)

#Create a weights lookup table to distinguish teams played more in the schedule.  This will naturally depict in the graph by the distance from the central node.  The more times the opposing Team plays the Twins, the closer they will reside to MIN on the network map.  To make even more visually easier to see, the size of each entry will also be proportional to the number of games played.

#To make that possible to turn the column of the data 'Opp' to a data dictionary indexed by Team.

opponent_dic = data['Opp'].value_counts().to_dict()

#Add nodes for the opposing teams. To make it easier to see I've added opposing Teams as red and made the size of the nodes proportional to the number of games played against the Twins.  In other words, a larger dot equates more games played.

for i in range(len(data)):
    G.add_node(data.iloc[i,5], color='red',size=opponent_dic[data.iloc[i,5]]*100)

#Add the connections or 'edges' to the network diagram.  Similar to the size of the node, the distance of the node from the center is proportional to the number of games played against the Twins.  This is done by assigning a property 'weight' to each edge.  The closer the node to the center, the more games played.

for i in range(len(data)):
    G.add_edges_from([(data.iloc[i,3],data.iloc[i,5],{'weight': opponent_dic[data.iloc[i,5]]})])

#Create list of assigned node sizes and colors. This step iterates through each node object and creates a list showing the node colors and sizes.  Given the index of the list matches the index of the nodes in the G object, when we render the image in the next step the color and sizes are assigned to the correct node.

node_color=[]
node_size=[]
for node in G.nodes():
    color = G.nodes[node]['color']
    node_color.append(color)
    size = G.nodes[node]['size']
    node_size.append(size)

#Draw the network digram assigning node_color and node_size using the lists established in the previous step.

nx.draw(G, with_labels=True,node_color= node_color,node_size=node_size)