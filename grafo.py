import igraph

class Grafo():

    def __init__(self):

        #self.grafo = igraph.read('dados/cond-mat.gml')
        #self.grafo = igraph.read('dados/polblogs.gml')
        self.grafo = igraph.read('dados/polbooks.gml')

if __name__=='__main__':

    g = Grafo()
    print("Número de vértices: ", g.grafo.vcount())
    print("Número de arestas: ", g.grafo.ecount())
    print("Densidade do grafo: ", g.grafo.density())
    #print("Grau dos vértices: ", g.grafo.degree())
    print("Grau médio dos 10 primeiros vértices (método usado: igraph.Graph().knn()): ")
    for i, j in zip(g.grafo.knn()[0][:10], g.grafo.knn()[1][:10]):
        print(i," - ", j)
    print("Grau médio de clusterização da rede: ", g.grafo.transitivity_undirected())
    
    print("\nCalculando a centralidade dos vértices: ")
    lista = []
    for v, i in zip(g.grafo.vs, g.grafo.eigenvector_centrality()):
        lista.append([v['label'], i])
    
    lista.sort(key=lambda x: x[1], reverse=True)
    for i in lista[:20]:
        print(i[0], i[1])

    print("Imprimindo a rede...")
    # Calculando o grau de cada vértice.
    cont = 0
    for i in g.grafo.degree():
        g.grafo.vs[cont]["size"] = 7+i*1.5
        cont += 1
    # Layouts testados para melhorar o plot.
    #layout = g.grafo.layout_reingold_tilford()
    #layout = g.grafo.layout_lgl()
    #layout = g.grafo.layout_circle()
    layout = g.grafo.layout_kamada_kawai()
    #"""
    try:
        igraph.plot(g.grafo,"plots/rede.pdf", layout=layout, bbox = (2500, 2500))
    except:
        igraph.plot(g.grafo, layout=layout).save("grafo.png")
    #"""

    print("\nCalculando o pagerank da rede (Google Page Rank): ")
    lista = []
    for v, i in zip(g.grafo.vs, g.grafo.pagerank()):
        lista.append([v['label'], i])
    
    lista.sort(key=lambda x: x[1], reverse=True)
    
    for i in lista[:20]:
        print(i[0], i[1])
    
