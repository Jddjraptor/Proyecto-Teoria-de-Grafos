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
#nx.draw(C1)
print(C1.size())

P11,Pxx = nx.check_planarity(C1,True)
print(P11)
#nx.draw(Pxx)



K3_3 = nx.complete_multipartite_graph(3,3)
#nx.draw(K3_3)

P2,Py = nx.check_planarity(K3_3,True)
print("\n",P2)
#nx.draw(Py)

print(list(nx.nodes(K3_3)))
print(list(nx.all_neighbors(K3_3,0)))

K3_30 = nx.MultiGraph(K3_3)
C2 = nx.contracted_edge(K3_30, (0, 3))
#nx.draw(C2)
print(C2.size())

P22,Pyy = nx.check_planarity(C2,True)
print(P22)
#nx.draw(Pyy)



Peter = nx.petersen_graph()
#nx.draw(Peter)

P3,Pz = nx.check_planarity(Peter,True)
print("\n",P3)
#nx.draw(Pz)

print(list(nx.nodes(Peter)))
print(list(nx.all_neighbors(Peter,0)))

Peter0 = nx.MultiGraph(Peter)
C3 = nx.contracted_edge(Peter0, (0, 1))
#nx.draw(C3)
print(C3.size())

P33,Pzz = nx.check_planarity(C3,True)
print(P33)
#nx.draw(Pzz)

print(list(nx.nodes(C3)))
print(list(nx.all_neighbors(C3,0)))

C33 = nx.contracted_edge(C3, (0, 4))
#nx.draw(C33)
print(C33.size())

P333,Pzzz = nx.check_planarity(C33,True)
print(P333)
#nx.draw(Pzzz)

print(list(nx.nodes(C33)))
print(list(nx.all_neighbors(C33,0)))

C4 = nx.contracted_edge(C33, (0, 5))
#nx.draw(C4)
print(C4.size())

P4,Pw = nx.check_planarity(C4,True)
print(P4)
#nx.draw(Pw)
