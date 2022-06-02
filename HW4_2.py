import networkx as nx
import matplotlib.pyplot as plt


class GraphSearch(object):

    def __init__(self):
        return

    def id_to_title(self, path):
        pages = {}
        with open(path, encoding='utf-8') as f:
            for data in f.read().splitlines():
                page = data.split('\t')
                # page[0]: id, page[1]: title
                pages[page[0]] = page[1]
        return pages

    #get dictionary of edges
    def link_list(self, path):
        links = []
        with open(path, encoding='utf-8') as f:
            for data in f.read().splitlines():
                link = data.split('\t')
                pair = (int(link[0]),int(link[1])) #convert to int
                if pair[0] != pair[1]:
                    links.append(pair)
        return links

    #find id from page dictionary
    def find_id(self, pages, title_name):
        # Googleをタイトルとするページのidが表示されます
        for k, v in pages.items():
            if v == title_name:
                print(title_name, k)
                return k

    #find title from page dictionary
    def find_title(self, pages, idname):
        # Googleをタイトルとするページのnameが表示されます
        for k, v in pages.items():
            if k == idname:
                print(idname, v)
                return v

    def gen_graph(self, node_list=[], edge_list=[()]):
        graph = nx.MultiDiGraph()
        graph.add_nodes_from(node_list)
        graph.add_edges_from(edge_list)
        nx.draw(graph, with_labels=True)
        plt.show()
        graph_dict = {}
        for node in node_list:
            graph_dict[node] = [next_node[1] for next_node in edge_list if next_node[0] == node]
        return graph_dict

    def bfs_traverse(self, graph, start_node):
        queue = [start_node]
        visited = set()
        visited.add(start_node)
        while len(queue) > 0:
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for next_node in nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
            print(vertex)

    def dfs_traverse(self, graph, start_node):
        stack = [start_node]
        visited = set()
        visited.add(start_node)
        while len(stack) > 0:
            vertex = stack.pop()
            nodes = graph[vertex]
            for next_node in nodes:
                if next_node not in visited:
                    stack.append(next_node)
                    visited.add(next_node)
            print(vertex)

if __name__ == "__main__":
    graph = GraphSearch()
    page_list = graph.id_to_title('data/pages.txt')
    link_list = graph.link_list('data/links.txt')
    query = ['Google','人工知能','パソコン','アニメ','ロボット','ハンバーグ','ゲーム','スターバックス','カフェ','企業','タピオカ']
    node_list = [] # covert the word in query to id
    for word in query:
        id = graph.find_id(page_list,word)
        if id != None: # delete the word that not in the list
            node_list.append(int(id))
    edge_list = []
    for i in link_list:
        if i[0] in node_list and i[1] in node_list: # check the link that contains the id
            edge_list.append(i)
    graph_dict = graph.gen_graph(node_list, edge_list)
    print(graph_dict)
    bfs = graph.bfs_traverse(graph_dict, node_list[0])
    print(bfs)
    dfs =graph.dfs_traverse(graph_dict, node_list[0])
    print(dfs)
    # Question : I find it difficult to covert each node from id to title in my graph.