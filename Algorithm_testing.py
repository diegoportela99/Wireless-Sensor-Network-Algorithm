import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

for x in range(1,50):
    G = nx.barabasi_albert_graph(10, 2)

    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(1,10)

    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    
    fig.canvas.draw()
    print(list(G.nodes))
    print(list(G.edges(data=True)))
    
    plt.pause(0.5)
    fig.clear()
    G.clear()
    
    
