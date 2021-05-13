import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

#Variables
numberOfNodes = 30
weightMax = 15

#default as node 0
sourceNode = 0

#best path map
mapPath = []

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = fig.add_subplot(111)

#in range of nodes, select one at random for target node.
sourceNode = (random.randint(1, numberOfNodes))

color_map = []

#Generate random graph structure to represent different scenario
G = nx.barabasi_albert_graph(numberOfNodes, 1)

for (u,v,w) in G.edges(data=True):
    w['weight'] = random.randint(1,weightMax)

mapPath = nx.shortest_path(G, source=numberOfNodes-1, target=0)
ax2.set_title(label=mapPath, fontsize=20, color="red")
    
for node in G:
    if node in mapPath:
        color_map.append('red')
    else: 
        color_map.append('black') 

    
pos=nx.spring_layout(G)
nx.draw(G, pos, node_size=500, node_color=color_map,  with_labels=True)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    
fig.canvas.draw()

print("source node is: " + str(numberOfNodes-1))
print("sink node is: 0")
print("Optimal Route " + str(mapPath))
    

