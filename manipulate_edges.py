import osmnx as ox
from dijkstra_shortest_path import remove_right_turn_edges 
from dijkstra_shortest_path import dijkstra

def manipulate_graph(factor: int):
    
    #Value for edge iteration
    i = 0
    
    #Identify left/straight edge lengths and change by factor 
    #Not changing right turns by factor
    for edge in no_right_turns:
        this_dict = no_right_turns[i][2]
        this_dict["length"] = (this_dict["length"] * factor)
        
        #Iterate through edges    
        i = i + 1
        
    return G_new.edges

if __name__ == "__main__":
    
    #Getting map and list of edges
    G_new = ox.graph.graph_from_xml("map-uni.osm", bidirectional=True)
    ox.bearing.add_edge_bearings(G_new)
    edges = list(G_new.edges(data = True))
    no_right_turns = remove_right_turn_edges(edges)
    
    #Call edge manipulation method to increase lengths
    #Set factor in method call --> Default = 1 (no change)
    manipulate_graph(1)
    

    