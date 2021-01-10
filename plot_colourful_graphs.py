"""
Given a TSP path (e.g. [4,3,1,0,2] on Liverpool graph, plot each sub-route with a diff colour (GitHub Issue #8 - https://github.com/rahul-kothari/TSP-Left-Turns/issues/8))
"""
import osmnx as ox

def eachLegInDifferentColour(G, path_idx, route_matrix):
    routes = []
    for i in range(len(path_idx)):
        routes.append(route_matrix[i-1][i])

    colours = ['r', 'g', 'b', 'y', 'c'] #, 'm', 'k', 'darkorange', 'turquoise', 'grey']
    ox.plot.plot_graph_routes(G, routes, colours)


def fullPathInOneColour(G, selected_node_ids, path_idx, route_matrix):
    final_tsp_route = [selected_node_ids[path_idx[-1]]] 

    for i in range(len(path_idx)):
        # start index/origin index is the last elemet on parth_idx. Go from path_idx[-1] to path_idx[0]. Then path_idx[0] to path_idx[1] and so on..
        from_node_idx = path_idx[i-1]
        to_node_idx = path_idx[i]
        print("Get path from node", from_node_idx, "to node", to_node_idx)#, ": ", route_matrix[from_node_idx][to_node_idx])
        # remove the first element in route as it was the prev to_node
        final_tsp_route.extend(route_matrix[from_node_idx][to_node_idx][1:])

    ox.plot.plot_graph_route(G, final_tsp_route)
    return final_tsp_route

if __name__ == "__main__":
    from experiments.data_algorithm_bottleneck_10_nodes import route_matrix_10_nodes_after_weight

    G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
    ox.bearing.add_edge_bearings(G)

    n1 = G.nodes[416913103]
    n2 = G.nodes[338834142]
    n3 = G.nodes[423810866]
    n4 = G.nodes[27207873]
    n5 = G.nodes[60179781]
    node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]

    # TSP path.
    path_idx = [2,0,1,3,4]

    eachLegInDifferentColour(G, path_idx, route_matrix_after_weight)
    fullPathInOneColour(G, node_ids, path_idx, route_matrix_after_weight)
