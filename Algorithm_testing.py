import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

#Variables
graphsToTest = 50
numberOfNodes = 10
weightMax = 10

#default as node 0
sourceNode = 0

#best path map
mapPath = []

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

#in range of nodes, select one at random for target node.
sourceNode = (random.randint(1, numberOfNodes))

color_map = []

#Generate random graph structures to represent different scenarios
for x in range(1,graphsToTest):
    G = nx.barabasi_albert_graph(numberOfNodes, 2)

    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(1,weightMax)
        color_map.append('blue')

    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    nx.draw_networkx_nodes(G, pos, node_size=1, node_color='red')
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    
    fig.canvas.draw()
    #print(list(G.nodes))
    #print(list(G.edges(data=True)))

    
    print("source node is: " + str(numberOfNodes-1))
    print("sink node is: 0")
    #for each node, find best route to sink
    print(nx.shortest_path(G, source=numberOfNodes-1, target=0))
 
    plt.pause(10)
    fig.clear()
    G.clear()
    

