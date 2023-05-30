import networkx as nx

K5 = nx.complete_graph(5)
#nx.draw(K5)

P1,Px = nx.check_planarity(K5,True)
print("\n",P1)
#nx.draw(Px)

print(list(nx.nodes(K5)))
print(list(nx.all_neighbors(K5,0)))

K50 = nx.MultiGraph(K5)
C1 = nx.contracted_edge(K50, (0, 1))
nx.draw(C1)
print(C1.size())

K3_3 = nx.complete_multipartite_graph(3,3)
#nx.draw(K3_3)

P2,Py = nx.check_planarity(K3_3,True)
print("\n",P2)
#nx.draw(Py)

print(list(nx.nodes(K3_3)))
print(list(nx.all_neighbors(K3_3,0)))

Peter = nx.petersen_graph()
#nx.draw(Peter)

P3,Pz = nx.check_planarity(Peter,True)
print("\n",P3)
#nx.draw(Pz)

print(list(nx.nodes(Peter)))
print(list(nx.all_neighbors(Peter,0)))
