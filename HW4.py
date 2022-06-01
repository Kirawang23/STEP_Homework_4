##### Homework 4

#### Question1：  Google"から"渋谷"までをたどる方法をDFSとBFSで探す

import collections

class GraphSearch(object):

    #initialize
    def __init__(self):
        return

    #get dictionary of pages(id to title)
    def id_to_tittle(self, path):
        pages = {}
        with open(path, encoding='utf-8') as f:
            for data in f.read().splitlines():
                page = data.split('\t')
                # page[0]: id, page[1]: title
                pages[page[0]] = page[1]
        return pages

    #get dictionary of edges
    def link_dict(self, path):
        links = {}
        with open(path, encoding='utf-8') as f:
            for data in f.read().splitlines():
                link = data.split('\t')
                # link[0]: id (from), links[1]: id (to)
                if link[0] in links:
                    links[link[0]].add(link[1])
                else:
                    links[link[0]] = {link[1]}
        return links

    #find tittle from page dictionary
    def find_title(self, pages, title_name, ):
        # Googleをタイトルとするページのidが表示されます
        for k, v in pages.items():
            if v == title_name:
                print(title_name, k)
                return k

    # search path from start node to target node by DFS algorithm
    def dfs(self,node, start, target):
        # stack
        container = collections.deque()
        visited = set() #save the id that has been visited
        result = {}
        container.append(start)
        visited.add(start)

        while len(container) > 0:
            v = container.pop() # read the last id
            if v == target:
                return True, result
            if v in node:
                for follow in node[v]:
                    if follow not in visited:
                        visited.add(follow)
                        container.append(follow)
                        result[follow] = v
        return False, result

    # search path from start node to target node by BFS algorithm
    def bfs(self,node, start, target):
        # stack
        container = collections.deque()
        visited = set() #save the id that has been visited
        result = {}
        container.append(start)
        visited.add(start)

        while len(container) > 0:
            v = container.popleft() # read the first id
            if v == target:
                return True, result
            if v in node:
                for follow in node[v]:
                    if follow not in visited:
                        visited.add(follow)
                        container.append(follow)
                        result[follow] = v
        return False, result

if __name__ == "__main__":
    graph = GraphSearch()
    page_list = graph.id_to_tittle('data/pages.txt')
    start_node = graph.find_title(page_list, 'Google')  # 457783
    end_node = graph.find_title(page_list, '渋谷')  # 22557
    nodes = graph.link_dict('data/links.txt')
    dfs_result = graph.dfs(nodes,start_node, end_node)
    bfs_result = graph.bfs(nodes,start_node, end_node)


