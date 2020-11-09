import sys
import osmnx as ox
import networkx as nx

def remove_right_turn_edges(edges: list):
    """
    For each edge, if bearing > 225 and bearing < 315 -> then edge is a right turn. Filter out such edges.

    Parameter:
    edges - each element is:
    (7997806716, 7997806715, {
        'osmid': 24729811, 
        'highway': 'footway', 
        'oneway': False, 
        'length': 13.687, 
        'bearing': 264.7
    })

    Returns:
    edges - list of edges.
    """
    return list(filter(lambda edge: not (edge[2]['bearing'] < 315 and edge[2]['bearing'] > 225), edges))

# 
def dijkstra(G: nx.MultiDiGraph, src_id, target_id, avoid_right_turn=False):
    """
    Implement dijkstra but optionally avoid right turns.
    https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

    Parameters:
    Graph - nx.MultiDiGraph
    src_id - Starting node id
    target_id - destination node id
    avoid_right_turns - boolean

    Returns:
    Path - list 
        List of nodes to traverse from src to target.
    """
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {src_id: (None, 0)}
    current_node_id = src_id
    visited = set()
    
    while current_node_id != target_id:
        visited.add(current_node_id)
        out_edges = list(G.edges(current_node_id, data=True))

        if (avoid_right_turn):
            # remove all edges that classify as right turn
            out_edges = remove_right_turn_edges(out_edges)

        weight_to_current_node = shortest_paths[current_node_id][1]

        for edge in out_edges:
            next_node_id = edge[1]
            weight = edge[2]['length'] + weight_to_current_node
            if next_node_id not in shortest_paths:
                shortest_paths[next_node_id] = (current_node_id, weight)
            else:
                current_shortest_weight = shortest_paths[next_node_id][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node_id] = (current_node_id, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return []
        # next node is the destination with the lowest weight
        current_node_id = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node_id is not None:
        path.append(current_node_id)
        next_node_id = shortest_paths[current_node_id][0]
        current_node_id = next_node_id
    # Reverse path
    path = path[::-1]
    return path


G = ox.graph.graph_from_xml("map-uni.osm")
ox.bearing.add_edge_bearings(G)
nodes =  list(G.nodes(data=True))

# Get the shortest route (dijkstra algorithm) from 1 node to another.
starting_node_id = nodes[-1][0]
destination_node_id = nodes[0][0]
route1 = ox.distance.shortest_path(G, starting_node_id, destination_node_id, weight = 'length')
print("Route according to osmnx: \t", route1)

route2 = dijkstra(G, starting_node_id, destination_node_id)
print("Route according to our dijkstra: \t", route2)

ox.plot.plot_graph_route(G, route1)
